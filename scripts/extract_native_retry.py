"""Verify a small default-retry slice in the already acquired exact ELF; never execute it."""
import argparse,hashlib,json,struct
from pathlib import Path

EXPECTED='cbf1045bb2d4de52142b68d825d265588e1c94ec7d4132284deea8fef67fe4d4'


def derive(path):
    b=path.read_bytes()
    if hashlib.sha256(b).hexdigest()!=EXPECTED:raise ValueError('Only the exact admitted ELF sample is supported')
    if b[:6]!=b'\x7fELF\x02\x01':raise ValueError('Expected little-endian ELF64')
    phoff=struct.unpack_from('<Q',b,32)[0];size,count=struct.unpack_from('<HH',b,54);segments=[]
    for n in range(count):
        typ,flags,off,va,pa,filesz,memsz,align=struct.unpack_from('<IIQQQQQQ',b,phoff+n*size)
        if typ==1:segments.append((va,off,filesz,memsz))
    def read(va,length):
        start,off,filesz,_=next(s for s in segments if s[0]<=va and va+length<=s[0]+s[2])
        pos=off+va-start;return pos,b[pos:pos+length]
    pos,raw=read(0x98b2f8,8);seconds=struct.unpack('<Q',raw)[0]
    if seconds!=5:raise ValueError('Unexpected default interval')
    evidence=[]
    for va,target in [(0x65708b,0x658900),(0x657090,0x479880),(0x657095,0x6589e0)]:
        off,code=read(va,5)
        if code[0]!=0xe8 or va+5+struct.unpack('<i',code[1:])[0]!=target:raise ValueError('Unexpected native call target')
        evidence.append({'va':hex(va),'file_offset':off,'instruction_bytes':5,'instruction_sha256':hashlib.sha256(code).hexdigest(),'call_target_va':hex(target)})
    off,code=read(0x658925,7)
    if code[:3]!=b'\x48\x69\xc0' or struct.unpack('<I',code[3:])[0]!=1_000_000_000:raise ValueError('Expected seconds-to-nanoseconds multiplication')
    evidence.append({'va':'0x658925','file_offset':off,'instruction_bytes':7,'instruction_sha256':hashlib.sha256(code).hexdigest(),'operation':'Multiply the zero-jitter seconds interval by1000000000'})
    jitter=next(s for s in segments if s[0]<=0x9f7b00<s[0]+s[3]);is_bss=0x9f7b00>=jitter[0]+jitter[2]
    return {'sample_sha256':EXPECTED,'method':'Static ELF64 program-header mapping, x86-64 relative CALL resolution and narrow literal validation; no execution.','interval_global_va':'0x98b2f8','interval_global_file_offset':pos,'interval_global_uint64':seconds,'interval_units':'seconds before time.Duration conversion','jitter_global_va':'0x9f7b00','jitter_zero_initialized_at_load':is_bss,'instruction_evidence':evidence,'runtime_limit':'Server responses may change interval/jitter; five-second behavior is generic and not a standalone compromise indicator.'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--sample',required=True,type=Path);p.add_argument('--out',required=True,type=Path);a=p.parse_args();result=derive(a.sample);a.out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result,indent=2))
