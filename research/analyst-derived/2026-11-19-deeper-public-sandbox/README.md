# CyberStrikeAI public sandbox host summary — 19 November 2026

We independently selected one host-summary entry from an [exact public OTX analysis](https://otx.alienvault.com/api/v1/indicators/file/09e1da2afa1216ecc55648ec8e122d2a/analysis). The explicit MD5/SHA1/SHA256 fields identify the Linux beacon named by MD5 in [Kaspersky's original report](https://securelist.com/tr/cyberstrikeai-attacks/121715/); the nested Cuckoo result repeats the same SHA256.

`/analysis/plugins/cuckoo/result/network/hosts/0/ip` contains `104[.]234[.]26[.]163`, an already-known repository value. This is one own evidence corroboration at score 20, with no new IP or malicious-C2 discovery. [Exact JSON pointers and identity evidence](host-summary-evidence.json) distinguish it from the earlier static URL-string selections.

The retained provider result has no populated TCP, UDP, HTTP, DNS or extended HTTP/TLS flow arrays. Its host summary does not establish a destination port, request, registration, successful connection or current service operation. Raw syscall `connect` entries contain pointers without decoded destination addresses; no endpoint is inferred from those pointers. A provider-reported PCAP digest is retained as source context, but the PCAP was not acquired.

The public JSON was retrieved again on 19 November 2026 and is byte-identical to the retained 15 November capture. Provider analysis timestamps lack explicit timezone and remain separate from review/acquisition UTC and victim activity. Malware bytes were not acquired or executed; no candidate infrastructure, DNS service, scanner or sample-submission service was contacted.
