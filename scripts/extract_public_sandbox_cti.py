"""Extract narrowly scoped CTI from public Triage HTML, URLscan search and CT files.

Never loads/executes malware, evaluates JavaScript, submits a scan, or contacts an
actor/victim endpoint. Offline by default; --fetch reads only fixed public sources.
Raw HTML/requests/cookies/tokens stay outside publication. cryptography is needed
only to parse already-public X.509 certificates; the sandbox extractor is stdlib.
"""
import argparse, collections, datetime as dt, hashlib, html, ipaddress, json, re
import statistics, urllib.error, urllib.request
import urllib.parse
from pathlib import Path
from html.parser import HTMLParser

CBF='cbf1045bb2d4de52142b68d825d265588e1c94ec7d4132284deea8fef67fe4d4'
KASP='1c6498f081ff7a5ef0e851d2c106668aef53e1384b8d0c52fa667e53a5664c33'
VENDOR='https://securelist.com/tr/cyberstrikeai-attacks/121715/'
PAGES={'261027-qmb8eaes6q':KASP,'261106-kvkxmaat3v':CBF,'261106-wzxb1a11bs':CBF,'261107-yeacvaex6v':CBF}
DOMAIN='media.fastcdn.bar'
KNOWN_IP='23.254.195.48'


def sha(data): return hashlib.sha256(data).hexdigest()


def embedded_network(payload):
    """Decode a strict JSON literal inside page_data; never evaluate source JS."""
    source=payload.decode('utf-8-sig')
    matches=list(re.finditer(r'^ {8}network:\s*',source,re.M))
    if len(matches)!=1: raise ValueError('Expected one task-report network JSON literal')
    start=matches[0].end();network,end=json.JSONDecoder().raw_decode(source[start:])
    if not isinstance(network,dict) or not all(k in network for k in ('flows','requests')):raise ValueError('Unexpected public-report structure')
    offset=len(source[:start].encode('utf8'));raw=source[start:start+end].encode('utf8')
    return network,{'json_file_byte_offset':offset,'json_byte_length':len(raw),'json_sha256':sha(raw)},raw


def public_fetch(root):
    """Small fixed allowlist; no API keys, login, scan submission or endpoint probes."""
    urls={ident+'.behavioral1.html':'https://tria.ge/'+ident+'/behavioral1' for ident in PAGES}
    urls.update({'urlscan_media_fastcdn.response':'https://urlscan.io/api/v1/search/?q=domain%3Amedia.fastcdn.bar&size=100',
                 'crt_fastcdn.response':'https://crt.sh/?q=%25.fastcdn.bar&output=json',
                 'cloudflare_ipv4.txt':'https://www.cloudflare.com/ips-v4','cloudflare_ipv6.txt':'https://www.cloudflare.com/ips-v6'})
    receipts=[]
    allowed_hosts={'tria.ge','urlscan.io','crt.sh','www.cloudflare.com'}
    def allowed(url):
        parsed=urllib.parse.urlsplit(url)
        return parsed.scheme=='https' and parsed.hostname in allowed_hosts and not parsed.username and not parsed.password and parsed.port in (None,443)
    class AllowlistedRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self,request,fp,code,msg,headers,newurl):
            if not allowed(newurl):raise urllib.error.URLError('Redirect outside fixed public-source allowlist blocked')
            return super().redirect_request(request,fp,code,msg,headers,newurl)
    opener=urllib.request.build_opener(AllowlistedRedirect())
    def get(name,url):
        receipt={'file':name,'url':url,'retrieved_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
        try:
            if not allowed(url):raise ValueError('Outside fixed public-source allowlist')
            req=urllib.request.Request(url,headers={'User-Agent':'Public-CTI-evidence-reproduction/1.0'})
            with opener.open(req,timeout=25) as response:
                data=response.read(3_000_001);receipt['http_status']=response.status
            if len(data)>3_000_000:raise ValueError('Public artifact exceeded 3 MB cap')
            temporary=root/(name+'.part');temporary.write_bytes(data);temporary.replace(root/name);receipt.update(bytes=len(data),sha256=sha(data))
        except (urllib.error.URLError,ValueError) as ex:receipt['error']=type(ex).__name__+': '+str(ex)[:160]
        receipts.append(receipt)
    root.mkdir(parents=True,exist_ok=True)
    for name,url in urls.items():get(name,url)
    ct=root/'crt_fastcdn.response'
    if ct.exists():
        seen=set()
        for entry in json.loads(ct.read_text(encoding='utf8')):
            serial=entry.get('serial_number')
            if serial in seen or len(seen)>=10:continue
            seen.add(serial);ident=int(entry['id']);get(f'crt_certificate_{ident}.response','https://crt.sh/?d='+str(ident))
    (root/'reproduction-fetch-receipts.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf8')
    return receipts


def parse_certificates(root):
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes,serialization
    result=[]
    for path in sorted(root.glob('crt_certificate_*.response')):
        data=path.read_bytes()
        try:
            cert=x509.load_pem_x509_certificate(data) if data.startswith(b'-----BEGIN') else x509.load_der_x509_certificate(data)
            names=cert.extensions.get_extension_for_class(x509.SubjectAlternativeName).value.get_values_for_type(x509.DNSName)
        except ValueError:continue
        ident=int(path.stem.rsplit('_',1)[-1]);der=cert.public_bytes(serialization.Encoding.DER)
        result.append({'crt_sh_id':ident,'source_url':'https://crt.sh/?id='+str(ident),'download_url':'https://crt.sh/?d='+str(ident),
                       'download_file_sha256':sha(data),'der_sha256':cert.fingerprint(hashes.SHA256()).hex(),'der_bytes':len(der),
                       'subject':cert.subject.rfc4514_string(),'issuer':cert.issuer.rfc4514_string(),'dns_san':names,
                       'not_before':cert.not_valid_before_utc.isoformat(),'not_after':cert.not_valid_after_utc.isoformat(),
                       'serial_hex':format(cert.serial_number,'x'),'precertificate':any(e.oid.dotted_string=='1.3.6.1.4.1.11129.2.4.3' for e in cert.extensions)})
    return result


class _Text(HTMLParser):
    def __init__(self):super().__init__();self.values=[]
    def handle_data(self,data):
        if data.strip():self.values.append(data.strip())


def sanitized_reports(root):
    captures=[]
    for ident,digest in PAGES.items():
        path=root/(ident+'.behavioral1.html');payload=path.read_bytes();source=payload.decode('utf8')
        title=re.search(r'<title>(.*?)</title>',source,re.S)
        if not title or digest not in html.unescape(title[1]):raise ValueError('Report title hash does not match the exact requested artifact: '+ident)
        text=_Text();text.feed(source)
        hashes={}
        for label in ('SHA256','MD5','SHA1'):
            values=[text.values[n+1].lower() for n,value in enumerate(text.values[:-1]) if value==label and re.fullmatch(r'[0-9a-fA-F]{32,64}',text.values[n+1])]
            if values:hashes[label.lower()]=values[0]
        if hashes.get('sha256')!=digest:raise ValueError('General-table SHA256 mismatch')
        expected_md5='805b9e4ae74c903787416800999b8418' if digest==KASP else 'ebd36581ed085413ba909a0625efe1c0'
        if hashes.get('md5')!=expected_md5:raise ValueError('General-table MD5 bridge mismatch')
        network,locator,raw=embedded_network(payload)
        submission=re.search(r'h-datetime="([^\"]+)"',source)
        relevant=[f for f in network['flows'] if f.get('tls_sni')==DOMAIN or f.get('domain')==DOMAIN] if digest==KASP else [f for f in network['flows'] if f.get('dst')==KNOWN_IP+':8443']
        ids={f['id'] for f in relevant};flows=[]
        keep={'id','domain','dst','first_seen','last_seen','proto','protocols','rx_bytes','rx_packets','tx_bytes','tx_packets','tls_ja3','tls_ja3s','tls_sni'}
        for flow in relevant:
            sanitized={k:v for k,v in flow.items() if k in keep}
            fragment=json.dumps(flow,separators=(',',':'),ensure_ascii=False).encode('utf8');at=raw.find(fragment)
            sanitized['source_locator']={'json_pointer':'/network/flows/'+str(network['flows'].index(flow)),'flow_id':flow['id'],'literal_byte_offset':locator['json_file_byte_offset']+at if at>=0 else None,'literal_bytes':len(fragment),'literal_sha256':sha(fragment)}
            flows.append(sanitized)
        requests=[];dns=[];response_codes=[]
        for index,event in enumerate(network['requests']):
            if event.get('flow') not in ids:continue
            if 'http_request' in event:
                request=event['http_request'];headers=request.get('headers',[])
                names=[str(h).split(':',1)[0].strip() for h in headers] if isinstance(headers,list) else list(headers)
                requests.append({'flow':event['flow'],'method':request.get('method'),'url':request.get('url'),'header_names':sorted(set(names),key=str.lower),'implant_token_header_present':any(name.lower()=='x-implant-token' for name in names),'source_json_pointer':'/network/requests/'+str(index)+'/http_request'})
            if 'http_response' in event:
                response=event['http_response'];code=response.get('status') or response.get('status_code');response_codes.append(code)
            if 'dns_response' in event:
                for answer in event['dns_response'].get('answers',[]):
                    if answer.get('name')==DOMAIN:dns.append(dict(answer,source_json_pointer='/network/requests/'+str(index)+'/dns_response/answers'))
        tcp=sorted((f for f in flows if f['proto']=='tcp'),key=lambda f:f['first_seen'])
        gaps=[nxt['first_seen']-prev['last_seen'] for prev,nxt in zip(tcp,tcp[1:])]
        captures.append({'report_id':ident,'source_url':'https://tria.ge/'+ident+'/behavioral1','sample_sha256':digest,'general_table_hashes':hashes,'primary_vendor_md5_bridge':'805b9e4ae74c903787416800999b8418' if digest==KASP else None,
                         'html_bytes':len(payload),'html_sha256':sha(payload),'network_json_locator':locator,
                         'sample_submitted_at_utc':submission[1] if submission else None,'flow_times_scope':'milliseconds relative to sandbox run; not victim observation timestamps',
                         'total_capture_flows':len(network['flows']),'selected_flows':flows,'selected_http_requests':requests,'selected_dns_answers':dns,
                         'http_response_codes':response_codes,'registration_success_established':False,'network_simulation_flags':'Not disclosed in the admitted embedded network object; absence of simulation is not established.',
                         'pid_attribution':'Network observations are scoped to the public sandbox task; these flow objects do not attribute a PID.',
                         'completion_to_next_start_ms':{'count':len(gaps),'minimum':min(gaps),'median':statistics.median(gaps),'maximum':max(gaps)} if gaps else None})
    return captures


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--capture-root',required=True,type=Path);ap.add_argument('--out',required=True,type=Path);ap.add_argument('--fetch',action='store_true');args=ap.parse_args()
    root=args.capture_root;out=args.out;out.mkdir(parents=True,exist_ok=True)
    if args.fetch:public_fetch(root)
    captures=sanitized_reports(root);certs=parse_certificates(root)
    scan=json.loads((root/'urlscan_media_fastcdn.response').read_text(encoding='utf8'))
    scans=[]
    for record in scan.get('results',[]):
        task=record['task'];page=record.get('page',{})
        if task.get('domain')!=DOMAIN:continue
        scans.append({'source_url':'https://urlscan.io/result/'+task['uuid']+'/', 'task_time_utc':task['time'],'url':task['url'],
                      'page_ip':page.get('ip'),'http_status':page.get('status'),'server':page.get('server'),'title':page.get('title'),'tls_issuer':page.get('tlsIssuer'),'tls_valid_from':page.get('tlsValidFrom'),
                      'scope':'Historical public search metadata only; result-detail API returned403 during this collection. Not current C2 status or successful implant registration.'})
    nets=[ipaddress.ip_network(s) for version in ('ipv4','ipv6') for s in (root/('cloudflare_'+version+'.txt')).read_text().splitlines() if s]
    ips=sorted({a['value'] for capture in captures if capture['sample_sha256']==KASP for a in capture['selected_dns_answers']}|{s['page_ip'] for s in scans if s.get('page_ip')})
    shared=[{'ip':ip,'in_current_cloudflare_published_ranges':any(ipaddress.ip_address(ip) in net for net in nets if ipaddress.ip_address(ip).version==net.version),'scope':'Shared CDN historical task/DNS context only; not attacker-owned origin or standalone block IOC.'} for ip in ips]
    result={'reviewed_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'captures':captures,'ct_certificates':certs,'urlscan_observations':scans,'urlscan_search_window_days':scan.get('search_date_limit_days'),'shared_cdn_context':shared,
            'limits':['No local execution, PCAP acquisition, authentication bypass, scan submission, actor/victim endpoint requests or Censys queries.','No raw HTTP requests, header values, token values, keys, cookies or binary malware are included.','No India targeting or victim-compromise association established for these artifacts.','The exact Kaspersky sample association comes from its published MD5 and public sandbox hash mapping; that sample binary was not acquired.','The cbf1045 sample is independently verified CyberStrikeAI lineage; the Kaspersky incident, operator and India links remain unestablished.','CT validity/issuance is not proof of deployment or attack timing; a precertificate hash is not a live TLS leaf fingerprint.','Cloudflare shared-edge addresses and CT siblings are context/leads, not malicious infrastructure assertions.']}
    (out/'sanitized-evidence.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps({'captures':len(captures),'matched_http_attempts':sum(len(c['selected_http_requests']) for c in captures),'certificates':len(certs),'shared_context_ips':len(shared),'out':str(out)},indent=2))


if __name__=='__main__':main()
