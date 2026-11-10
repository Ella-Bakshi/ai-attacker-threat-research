"""Pure, offline IP extraction, evidence scoring and range-lookup helpers."""
import bisect,csv,datetime as dt,gzip,ipaddress,re,urllib.parse

IP_TYPES={'ipv4','ipv6','ipv4_port','network_endpoint','deployment_endpoint','deployment_host','url','url_prefix','url_template'}

def primary_reported_c2(record):
    """Global incident-role classification; conveys no India-targeting assertion."""
    return record.get('publication_category')=='main-iocs' and record.get('origin')=='external_report' and bool(re.search(r'\bc2\b',record.get('role',''),re.I))

def extract_ip(value,kind):
    if kind not in IP_TYPES:return None
    try:return str(ipaddress.ip_address(value)),None
    except ValueError:pass
    parsed=urllib.parse.urlsplit(value if '://' in value else '//'+value)
    if not parsed.hostname:raise ValueError('Missing host')
    try:address=ipaddress.ip_address(parsed.hostname)
    except ValueError:return None
    return str(address),parsed.port

def is_public(address):
    ip=ipaddress.ip_address(address)
    return ip.is_global and not any(getattr(ip,'is_'+n) for n in ['private','loopback','link_local','multicast','reserved','unspecified'])

def lookup_asn_sorted(target_ints,gzipfile,ipv6=False):
    """Inclusive, family-specific interval join; only retain the requested addresses."""
    targets=sorted(set(target_ints));out={};previous_end=-1
    if not targets:return out
    with gzip.open(gzipfile,'rt',encoding='utf-8',newline='') as f:
        for row in csv.reader(f,delimiter='\t'):
            if not row:continue
            start,end=(int(ipaddress.IPv6Address(row[0])),int(ipaddress.IPv6Address(row[1]))) if ipv6 else (int(row[0]),int(row[1]))
            if end<start or start<=previous_end:raise ValueError('ASN ranges must be sorted and non-overlapping')
            previous_end=end
            if start>targets[-1]:break
            pos=bisect.bisect_left(targets,start)
            while pos<len(targets) and targets[pos]<=end:
                asn=int(row[2]);out[targets[pos]]={'asn':asn, 'asn_org':row[4],'asn_country_code':row[3] if row[3]!='None' else '', 'range_start':start, 'range_end':end}
                pos+=1
    return out

def confidence_for_records(records):
    """Ordinal evidence rubric, never a maliciousness probability or GeoIP score."""
    scores=[]
    for r in records:
        cat=r.get('publication_category','');origin=r.get('origin','');role=r.get('role','').lower();locator=r.get('source_locator') or {}
        if cat in {'legitimate-service-context','supporting-context','shared-services-and-generic-markers'}:
            score,basis=0,'Generic/shared service or nonindicative supporting context; no compromise confidence assigned.'
        elif r.get('record_id','').startswith('OWNCTI-') and origin=='analyst_public_sandbox_derivation' and cat=='analyst-derived' and r.get('indicator_type') in {'ipv4','domain_port','network_pattern','http_request_pattern'} and re.fullmatch('[0-9a-f]{64}',locator.get('sample_sha256','')) and (locator.get('tls_flow_ids') or locator.get('sandbox_runs') or locator.get('public_runs')):
            score,basis=60,'Exact-sample public sandbox network relationship independently extracted; capture-level attempts only, with execution environment, operator, live C2 success and India association unestablished.'
        elif r.get('record_id','').startswith('OWNCTI-') and origin=='analyst_ct_certificate_derivation' and cat=='analyst-derived' and r.get('indicator_type')=='tls_certificate_sha256' and locator.get('dns_san') and locator.get('der_bytes') and not locator.get('precertificate'):
            score,basis=40,'Public CT certificate DER identity and domain verified locally; issuance is not proof of deployment, a live TLS leaf or actor ownership.'
        elif r.get('record_id','').startswith('OWNCTI-'):
            score,basis=0,'Contextual fingerprint, generic timing pattern or unverified certificate sibling; no standalone maliciousness confidence assigned.'
        elif cat=='sample-derived-observables' and origin.startswith('analyst_'):
            score,basis=60,'Exact sample configuration examined statically; execution, operator and individual victim unverified.'
        elif cat in {'main-iocs','sourced-iocs'} and (cat=='main-iocs' or re.search(r'\bc2\b',role)):
            score,basis=70,'Primary source reports a historical incident or campaign C2 role; current ownership and live use unverified.'
        elif cat in {'sourced-iocs','campaign-context'}:
            score,basis=55,'Source-reported historical campaign infrastructure/context; role and dates require correlation.'
        elif cat=='report-host-network-artifacts' and re.search(r'\bc2\b',role):
            score,basis=70,'Primary report explicitly describes this historical C2 role; present-day activity unverified.'
        elif cat=='deployment-leads':
            score,basis=20,'Passive software/deployment lead; a sighting does not establish malicious operation.'
        elif cat in {'unverified-findings','master-only-passive-lead'}:
            score,basis=10,'Unresolved or conflicting source attribution; review required.'
        else:
            score,basis=20,'Software/reference or contextual observation; standalone maliciousness unestablished.'
        scores.append((score,basis,r['record_id']))
    if not scores:return 0,'Unreviewed contributor-supplied IP; no verified campaign association.',[]
    best=max(x[0] for x in scores);chosen=[x for x in scores if x[0]==best]
    return best,chosen[0][1],sorted(x[2] for x in chosen)

def latest_reported_timestamp(records):
    values=sorted({str(r.get('last_seen','')).strip() for r in records if r.get('last_seen')})
    aware=[]
    for value in values:
        try:
            parsed=dt.datetime.fromisoformat(value.replace('Z','+00:00'))
            if parsed.tzinfo:aware.append((parsed,value))
        except ValueError:pass
    if aware:return max(aware,key=lambda p:p[0])[1],'source_last_seen_with_explicit_timezone'
    if values:return max(values),'source_last_seen_as_reported_timezone_or_precision_unstated'
    return '','unknown_no_observation_time'
