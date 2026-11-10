"""Download the documented open bulk datasets; never contact indicator IPs."""
import argparse,datetime as dt,gzip,hashlib,json,pathlib,re,shutil,urllib.request
from urllib.parse import urlsplit

def allowed_download(url):
    parsed=urlsplit(url)
    return (parsed.scheme=='https' and parsed.hostname in {'iptoasn.com','download.db-ip.com'}
            and parsed.port in {None,443} and not parsed.username and not parsed.password)

class DatasetRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        if not allowed_download(newurl):raise ValueError('Dataset redirect outside approved HTTPS providers')
        return super().redirect_request(req,fp,code,msg,headers,newurl)

def main():
    p=argparse.ArgumentParser();p.add_argument('--db-dir',type=pathlib.Path,default=pathlib.Path('work/enrichment-data'));p.add_argument('--month',default=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m'));p.add_argument('--reuse',action='store_true');a=p.parse_args()
    if not re.fullmatch(r'20\d{2}-(?:0[1-9]|1[0-2])',a.month):raise ValueError('month must be YYYY-MM')
    out=a.db_dir.resolve();out.mkdir(parents=True,exist_ok=True);metadata=out/'snapshots.json'
    prior={r['file']:r for r in json.loads(metadata.read_text(encoding='utf-8'))} if metadata.exists() else {}
    sources=[('ip2asn-v4-u32.tsv.gz','https://iptoasn.com/data/ip2asn-v4-u32.tsv.gz'),('ip2asn-v6.tsv.gz','https://iptoasn.com/data/ip2asn-v6.tsv.gz'),('dbip-city-lite-'+a.month+'.mmdb.gz','https://download.db-ip.com/free/dbip-city-lite-'+a.month+'.mmdb.gz')];result=[]
    for name,url in sources:
        target=out/name;old=prior.get(name)
        if a.reuse and old and target.exists() and hashlib.file_digest(target.open('rb'),'sha256').hexdigest()==old['sha256'] and (not name.endswith('.mmdb.gz') or (out/old['uncompressed_file']).exists()):result.append(old);continue
        print('Downloading '+name,flush=True);temp=target.with_suffix(target.suffix+'.partial');digest=hashlib.sha256();n=0
        opener=urllib.request.build_opener(DatasetRedirectHandler())
        with opener.open(urllib.request.Request(url,headers={'User-Agent':'AI-Attacker-Threat-Research-enrichment/1.0'}),timeout=120) as response,temp.open('wb') as stream:
            if not allowed_download(response.geturl()):raise ValueError('Unexpected download redirect')
            headers=response.headers
            while chunk:=response.read(1024*1024):
                n+=len(chunk)
                if n>200_000_000:raise ValueError('Dataset exceeded download size bound')
                stream.write(chunk);digest.update(chunk)
        temp.replace(target);r={'file':name,'source_url':url,'retrieved_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'http_status':200,'bytes':n,'sha256':digest.hexdigest(),'last_modified_header':headers.get('Last-Modified'),'etag':headers.get('ETag')}
        if name.endswith('.mmdb.gz'):
            unpacked=target.with_suffix('');temp=unpacked.with_suffix('.mmdb.partial');n=0
            with gzip.open(target,'rb') as source,temp.open('wb') as destination:
                while chunk:=source.read(1024*1024):
                    n+=len(chunk)
                    if n>250_000_000:raise ValueError('MMDB exceeded uncompressed size bound')
                    destination.write(chunk)
            temp.replace(unpacked);r.update(uncompressed_file=unpacked.name,uncompressed_bytes=n,uncompressed_sha256=hashlib.file_digest(unpacked.open('rb'),'sha256').hexdigest())
        result.append(r);print('Downloaded '+name+' ('+str(r['bytes'])+' bytes)',flush=True)
    temp=metadata.with_suffix('.json.partial');temp.write_bytes((json.dumps(result,indent=2)+'\n').encode());temp.replace(metadata)
    print('Bulk metadata ready. No target requests or API credentials used.')

if __name__=='__main__':main()
