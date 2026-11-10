"""Build or refresh a provenance-preserving IP overview from local open databases.

Only reads local datasets. No IP targets, DNS resolvers or paid APIs are contacted.
"""
import argparse,collections,csv,datetime as dt,hashlib,ipaddress,json,math,pathlib,sys,urllib.parse
from ip_enrichment import IP_TYPES,extract_ip,is_public,lookup_asn_sorted,confidence_for_records,latest_reported_timestamp

def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,obj):p.parent.mkdir(parents=True,exist_ok=True);temp=p.with_suffix(p.suffix+'.tmp');temp.write_bytes((json.dumps(obj,ensure_ascii=False,separators=(',',':'))+'\n').encode());temp.replace(p)
def vals(value):
    if not value:return []
    if isinstance(value,list):return value
    return [x.strip() for x in str(value).split(';') if x.strip()]
def source_dates(records,field):
    out=set()
    for r in records:
        out.update(vals(r.get(field)))
        if field=='source_published_date':out.update(x['published_date'] for x in r.get('source_references',[]) if x.get('published_date'))
    return sorted(out)
def read_csv(path):
    if not path.exists():return []
    with path.open(encoding='utf-8-sig',newline='') as f:
        return [{k.strip().lower():v for k,v in r.items() if k is not None} for r in csv.DictReader(f)]
def write_csv(path,rows):
    primary=['ip','timestamp','asn','hosting','location','latitude','longitude','confidence_score','confidence_basis']
    fields=primary+[k for k in dict.fromkeys(k for r in rows for k in r) if k not in primary]
    temp=path.with_suffix('.csv.tmp')
    with temp.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader()
        for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False,separators=(',',':')) if isinstance(v,(list,dict)) else v for k,v in r.items()})
    temp.replace(path)

def main():
    a=argparse.ArgumentParser();a.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);a.add_argument('--db-dir',type=pathlib.Path,default=pathlib.Path('work/enrichment-data'));a.add_argument('--seed-from-catalog',action='store_true');a.add_argument('--input-csv',type=pathlib.Path);args=a.parse_args()
    root=args.root.resolve();dbdir=args.db_dir.resolve();index=load(root/'data/index.json');records=[];inputs=[]
    for rel in index['record_files']+index.get('supplementary_record_files',[]):
        b=(root/rel).read_bytes();rr=json.loads(b);records+=rr;inputs.append({'path':rel,'sha256':hashlib.sha256(b).hexdigest(),'records':len(rr)})
    canonical_ips={p[0] for r in records if r['indicator_type'] in IP_TYPES and (p:=extract_ip(r['indicator'],r['indicator_type']))}
    master_path=root/'data/ALL-FOUND-master.csv';master_bytes=master_path.read_bytes();master_rows=read_csv(master_path)
    inputs.append({'path':'data/ALL-FOUND-master.csv','sha256':hashlib.sha256(master_bytes).hexdigest(),'records':len(master_rows),'purpose':'Only scalar IPs absent from the curated catalog; historical master-only leads, never promoted to C2.'})
    master_only=set()
    for entry in master_rows:
        try:ip=str(ipaddress.ip_address(entry['value']))
        except ValueError:continue
        if ip in canonical_ips or ip in master_only:continue
        master_only.add(ip)
        records.append({'record_id':'MASTER-'+hashlib.sha256((entry['type']+'|'+entry['value']).encode()).hexdigest()[:12].upper(),'indicator_type':entry['type'],'indicator':ip,'framework':entry['frameworks'],'publication_category':'master-only-passive-lead','role':entry['roles'],'origin':'historical_master_index','primary_source_url':entry['source_urls'],'first_seen':entry.get('first_seen',''),'last_seen':entry.get('last_seen',''),'india_relevance':'unestablished','source_published_date':''})
    lookup=collections.defaultdict(list);ports=collections.defaultdict(set);ranges=[];domain_count=0
    for r in records:
        if r['indicator_type']=='ipv4_range':ranges.append({k:r.get(k) for k in ['record_id','indicator','role','primary_source_url']});continue
        if r['indicator_type'] not in IP_TYPES:continue
        try:parsed=extract_ip(r['indicator'],r['indicator_type'])
        except ValueError as e:raise ValueError(r['record_id']+': '+str(e)) from e
        if parsed is None:domain_count+=1;continue
        ip,port=parsed;lookup[ip].append(r)
        if port is not None:ports[ip].add(port)
    infile=args.input_csv or root/'data/ip-overview.csv';existing=read_csv(infile);submitted={}
    prior_output={r['ip']:r for r in load(root/'data/ip-overview.json')} if (root/'data/ip-overview.json').exists() else {}
    cross_checks={r['ip']:r for r in load(root/'data/enrichment/ipinfo-cross-checks.json')} if (root/'data/enrichment/ipinfo-cross-checks.json').exists() else {}
    for r in existing:
        ip=str(ipaddress.ip_address(r['ip'].strip()))
        if ip in submitted:raise ValueError('Duplicate input CSV IP: '+ip)
        submitted[ip]=r
    addresses=set(lookup)|set(submitted) if args.seed_from_catalog else set(submitted)
    if not addresses:raise ValueError('No IPs. Seed with --seed-from-catalog or supply --input-csv.')
    snapshots=[x for x in load(dbdir/'snapshots.json') if x['file'].startswith(('ip2asn-','dbip-'))];snapby={s['file']:s for s in snapshots}
    asn4=lookup_asn_sorted([int(ipaddress.ip_address(ip)) for ip in addresses if ipaddress.ip_address(ip).version==4 and is_public(ip)],dbdir/'ip2asn-v4-u32.tsv.gz')
    asn6=lookup_asn_sorted([int(ipaddress.ip_address(ip)) for ip in addresses if ipaddress.ip_address(ip).version==6 and is_public(ip)],dbdir/'ip2asn-v6.tsv.gz',ipv6=True)
    geoentry=next(x for x in snapshots if x['file'].endswith('.mmdb.gz'));geofile=dbdir/geoentry['uncompressed_file']
    import maxminddb
    c2={x['record_id'] for x in load(root/'india/c2-infrastructure-targeting-india.json')};delivery={x['record_id'] for x in load(root/'india/delivery-infrastructure-targeting-india.json')};config={x['record_id'] for x in load(root/'india/c2-configuration-resources-targeting-india.json')}
    now=dt.datetime.now(dt.timezone.utc).isoformat();result=[]
    with maxminddb.open_database(str(geofile)) as reader:
        geo_build=dt.datetime.fromtimestamp(reader.metadata().build_epoch,dt.timezone.utc).isoformat()
        for ip in sorted(addresses,key=lambda v:(ipaddress.ip_address(v).version,int(ipaddress.ip_address(v)))):
            rr=lookup.get(ip,[]);inp=submitted.get(ip,{});version=ipaddress.ip_address(ip).version;public=is_public(ip)
            asn=(asn4 if version==4 else asn6).get(int(ipaddress.ip_address(ip)),{}) if public else {}
            geo=(reader.get(ip) or {}) if public else {};loc=geo.get('location',{});lat,lon=loc.get('latitude'),loc.get('longitude')
            valid=all(isinstance(v,(float,int)) and math.isfinite(v) for v in [lat,lon]) and -90<=lat<=90 and -180<=lon<=180
            if not valid:lat=lon=None
            country=geo.get('country',{});city=geo.get('city',{}).get('names',{}).get('en','');regions=geo.get('subdivisions',[]);region=regions[0].get('names',{}).get('en','') if regions else ''
            cc=country.get('iso_code','');place=', '.join(x for x in [city,region,cc] if x)
            score,basis,score_ids=confidence_for_records(rr);method='evidence-rubric-v1';manual_score=inp.get('manual_score','').strip();manual_basis=inp.get('manual_confidence_basis','').strip()
            if manual_score:
                if not manual_basis:raise ValueError('manual_score requires manual_confidence_basis: '+ip)
                score=int(manual_score)
                if not 0<=score<=100:raise ValueError('manual_score out of bounds: '+ip)
                basis=manual_basis;method='contributor_manual_review';score_ids=[]
            timestamp,basis_time=latest_reported_timestamp(rr)
            if inp.get('timestamp','').strip():
                timestamp=inp['timestamp'].strip();basis_time=inp.get('timestamp_basis','').strip() or 'contributor_supplied_unverified'
                if ip in prior_output and timestamp!=prior_output[ip].get('timestamp',''):basis_time='contributor_supplied_unverified'
            cats=sorted({r['publication_category'] for r in rr}) or ['unverified-manual-submission'];role_values=sorted({r['role'] for r in rr});nroles=set()
            for r in rr:
                rid=r['record_id'];cat=r['publication_category']
                if rid in c2:nroles.add('c2')
                if rid in delivery:nroles.add('delivery')
                if rid in config:nroles.add('c2_configuration')
                if cat=='deployment-leads':nroles.add('deployment_lead')
                if cat=='master-only-passive-lead':nroles.add('master_only_passive_lead')
                if cat=='sample-derived-observables':nroles.add('sample_static_configuration')
                if cat=='legitimate-service-context':nroles.add('legitimate_service')
            row={'ip':ip,'timestamp':timestamp,'asn':('AS'+str(asn['asn'])) if asn.get('asn') else '','hosting':asn.get('asn_org','') if asn.get('asn') else '', 'location':place,'latitude':lat,'longitude':lon,'confidence_score':score,'confidence_basis':basis,'timestamp_basis':basis_time,'enriched_at_utc':now,'asn_org':asn.get('asn_org',''),'hosting_basis':'ASN network description from IPtoASN; reseller/tenant and hosting-service classification are not inferred.','ip_version':version,'asn_country_code':asn.get('asn_country_code',''),'country_code':cc,'country_name':country.get('names',{}).get('en',''),'region':region,'city':city,'geo_status':'matched_approximate' if valid else ('not_public' if not public else 'unmatched'),'coordinate_basis':'DB-IP City Lite approximate coordinates' if valid else 'unknown','enrichment_status':'complete' if asn.get('asn') and valid else ('not_public' if not public else 'partial_or_unmatched'),'asn_range_start':str(ipaddress.IPv6Address(asn['range_start']) if version==6 else ipaddress.IPv4Address(asn['range_start'])) if asn else '', 'asn_range_end':str(ipaddress.IPv6Address(asn['range_end']) if version==6 else ipaddress.IPv4Address(asn['range_end'])) if asn else '','asn_source':'https://iptoasn.com/','geo_source':'https://db-ip.com/db/download/ip-to-city-lite','asn_dataset_last_modified':snapby['ip2asn-v4-u32.tsv.gz' if version==4 else 'ip2asn-v6.tsv.gz'].get('last_modified_header',''),'geo_dataset_build_utc':geo_build,'first_seen_values':source_dates(rr,'first_seen'),'last_seen_values':source_dates(rr,'last_seen'),'source_publication_dates':source_dates(rr,'source_published_date'),'record_ids':sorted({r['record_id'] for r in rr}),'frameworks':sorted({v for r in rr for v in vals(r['framework'])}),'campaigns':sorted({r['campaign'] for r in rr if r.get('campaign')}),'publication_categories':cats,'roles':role_values,'network_roles':sorted(nroles),'india_targeting_scopes':sorted({r.get('india_targeting_scope',r.get('india_relevance','unestablished')) for r in rr}) or ['unestablished'],'india_campaign_c2_supported':any(r['record_id'] in c2 and r.get('india_targeting_scope')=='campaign' and r.get('india_evidence_url') for r in rr),'self_derived':any(r.get('origin','').startswith('analyst_') for r in rr),'confidence_method':method,'confidence_record_ids':score_ids,'confidence_is_probability':False,'source_urls':sorted({u for r in rr for u in r.get('primary_source_url','').split('; ') if u}),'input_origin':'master_only' if ip in master_only else ('catalog' if rr else 'manual_csv'),'manual_score':manual_score,'manual_confidence_basis':manual_basis}
            check=cross_checks.get(ip,{})
            row.update(ipinfo_source_url=check.get('url',''),ipinfo_company=check.get('company',''),ipinfo_asn=check.get('asn',''),ipinfo_location=', '.join(v for v in [check.get('city'),check.get('country_code')] if v),ipinfo_evidence_date=(check.get('provider_measurement') or {}).get('date',''),ipinfo_reviewed_at_utc=check.get('reviewed_at_utc',''))
            result.append(row)
    output=root/'data';write(output/'ip-overview.json',result);write_csv(output/'ip-overview.csv',result)
    sources={'generated_at_utc':now,'databases':snapshots,'asn_license':{'name':'PDDL 1.0','url':'https://iptoasn.com/'},'geolocation_license':{'name':'CC BY 4.0','attribution':'IP Geolocation by DB-IP','url':'https://db-ip.com','license_url':'https://creativecommons.org/licenses/by/4.0/','changes':'Matched subset joined with research evidence; English labels extracted; no full database redistributed.'},'catalog_inputs':inputs,'geo_build_utc':geo_build}
    write(output/'enrichment/sources.json',sources)
    summary={'generated_at_utc':now,'selection_mode':'catalog_seed_plus_existing_csv' if args.seed_from_catalog else 'input_csv','unique_ips':len(result),'ipv4':sum(r['ip_version']==4 for r in result),'ipv6':sum(r['ip_version']==6 for r in result),'mapped_ips':sum(r['latitude'] is not None for r in result),'asn_matched_ips':sum(bool(r['asn']) for r in result),'self_derived_ips':sum(r['self_derived'] for r in result),'master_only_ips':sum(r['input_origin']=='master_only' for r in result),'manual_ips':sum(r['input_origin']=='manual_csv' for r in result),'unknown_location_ips':[r['ip'] for r in result if r['latitude'] is None],'domain_host_records_not_resolved':domain_count,'ranges_unexpanded':ranges,'new_threat_indicator_claims':0,'censys_calls':0,'shodan_calls':0,'target_requests':0,'dns_queries':0,'score_rubric':'evidence-rubric-v1; ordinal evidence strength, not a maliciousness probability; geography and ASN never increase the score.'}
    write(output/'enrichment/summary.json',summary);print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
