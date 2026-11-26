# 26 November 2026 daily hunt

This run adds **474 evidence records**, **426 distinct new values** and **366 selected IPs**. The classes below retain their own source roles. [Records](records.json) · [CSV](records.csv) · [Counts](summary.json)

| Evidence class | Records |
| --- | ---: |
| deployment-leads | 416 |
| campaign-context | 23 |
| sourced-iocs | 23 |
| software-fingerprints | 7 |
| report-artifact-observables | 5 |

## Incident reporting

- Huntback's university investigation gives an ARTEX operator host, the exact console and separately described tunnel, staging, and collector endpoints, plus host artifacts. Case activity is reported for 15–19 November. The 16–18 November interval applies to the reported listener group. [Huntback ARTEX case](https://huntback.io/blog/ai-pentest-console-south-korean-university-global-admin)
- A separate Huntback case documents coding-agent abuse. One historical C2 IP and two C2 listener domains are explicitly role-qualified. The remaining addresses retain narrower operator, startup or callback roles. Eight listed SHA-256s retain their file roles. [Huntback coding-agent case](https://huntback.io/blog/fake-ctf-ai-coding-agent-35-real-domains)
- Original reporting provides four GT13 domains, seven Bazuka hashes or configured hostnames and nine ThreeAM file hashes. The shared GT13 VPN egresses are held outside the public list. GreyNoise describes AI assistance as an assessment. ThreatFabric observed model integration in Bazuka's control panel. Bitdefender assessed hybrid activity. [GreyNoise](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) · [ThreatFabric](https://www.threatfabric.com/blogs/bazuka-the-fraud-framework-that-can-do-it-all) · [Bitdefender](https://www.bitdefender.com/en-us/blog/businessinsights/3am-ransomware-hybrid-ai-attack)

## Passive deployments

The once-daily Offensive Agency snapshot added **415** source-qualified passive observations for already indexed tools. Admission requires a registered tool identity and one unambiguous port in the publisher's confirmed software classification. Host-level provider dates remain separate from endpoint timestamps. Earlier qualifying rows that disappeared from today's snapshot remain historical observations. Data attribution **offensive.agency, data by ONYPHE**, under CC BY 4.0. [Offensive Agency methodology and license](https://offensive.agency/about)

## Our findings and the tool index

We independently computed **seven** static application asset fingerprints for PentAGI and AutoCVE. Their record locators preserve pinned source revisions, lengths, Git blob IDs and hash scope. The run yielded zero independently verified malicious IOCs. [Software fingerprints](software-fingerprints.csv)

Shadowserver reports exposure and honeypot telemetry at aggregate level. Its public dashboard has no IP-level evidence. The linked T3MP3ST owning project is newly indexed here with its existing release metadata. [Shadowserver](https://www.shadowserver.org/news/agentic-ai-attack-frameworks-in-the-wild-what-our-scans-and-honeypots-show/) · [Tool registry](../../../tools/README.md)

The 35 prior unresolved catalog relationships and 25 private provider leads retain their existing separate status. No new probe, target request or paid-provider call was used.
