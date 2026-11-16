# 16 November 2026: deeper artifact and source review

This pass adds **19 evidence memberships**: four own corroborations of existing values and 15 externally sourced memberships. The external set adds **12 distinct values**, including **three historical web attack-source IPs**. Current totals become **12,830 canonical records** and **16,348 master values**. All **35 unresolved findings** were revisited; **none was resolved**.

## Our artifact work

We reconstructed the exact **372-byte representation** of the supporting `p1.ps1` script displayed in [Kaspersky's original report](https://securelist.com/tr/cyberstrikeai-attacks/121715/). Its three locally computed hashes match the publisher's named MD5, SHA-1 and SHA-256 identities. Static inspection corroborates its existing TCP destination `185[.]186[.]245[.]144:5501`.

These are four new evidence memberships for existing values, with score 60 for exact static artifact evidence. No original script file, CyberStrikeAI beacon or controller binary was downloaded, and nothing was executed. No new malicious C2 IP was discovered. [Scientific evidence and method](../../../research/analyst-derived/2026-11-16-cyberstrikeai-publisher-script/README.md) preserve the identity bridge, offsets and limits; raw script bytes and image copies remain private.

## Source aggregation

| Evidence class | Memberships | Confidence scope |
|---|---:|---|
| Source-reported campaign context | 12 | Historical tool/attack-source roles; score ceiling 55 |
| Legitimate Certipy supporting hashes | 3 | File identity and supporting context; score 0 |
| Our supporting-script corroborations | 4 | Exact static artifact facts; score ceiling 60 |

[Scutum's original report](https://www.scutum.jp/information/waf_tech_blog/2026/10/waf-blog-085.html) identifies `38[.]54[.]56[.]121`, `185[.]196[.]220[.]130` and `192[.]236[.]229[.]229` as attack sources against Japanese companies. **They are not reported C2 servers or attributed to ARTEX/CyberStrikeAI.** Its AI-agent assessment uses an unpublished vendor method that we did not independently validate. The source warns that legitimate traffic may also use the addresses. Its October 10–14 monitoring window provides no per-IP absolute event times.

[Hunt's MD5 table](https://hunt.io/blog/papercut-attacker-ai-toolkit-exploit-code-second-rce) and [GreyNoise's report](https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf) anchor the PaperCut tool roles. Four existing public OTX computed-file objects supply explicit MD5/SHA1/SHA256/size bridges. These are provider-reported identities, not locally acquired sample bytes. [Compact bridge evidence](publisher-hash-bridges.json) keeps Certipy separate from malicious-implant claims. Five previously private algorithm questions were clarified; these were not five of the public 35 unresolved findings.

## Remaining uncertainty

The [35-record snapshot](remaining-unverified.json) preserves prior history and current source locators: 24 ARTEX/source discrepancies, nine JPCERT mixed-framework relationships and two certificate-transparency siblings. Original Japanese sources, four full-resolution figures, a seven-page NICT advisory and linked reports do not map the nine JPCERT addresses to individual frameworks. Initial publication on October 8 is separate from the October 23 Case-E addition; its JST ranges can mean observed attacks or estimated infrastructure operation.

Empty OTX associations for `static.fastcdn.bar` and `www.fastcdn.bar` establish neither maliciousness nor benignness. Two passive-DNS requests returned HTTP429 and were not retried. Historical certificate identity remains separate from campaign attribution.

The [ARTEX channel review](artex-source-review.json) examines MalwareMustDie's pinned 113-row curated pack. Its **Appendix F chronology** disclaims new IOCs, samples and primary telemetry; this does not mean the entire pack is empty. Generic markers and neighboring prefixes were not imported as malicious IOCs. No exact requested ARTEX malware bytes were recovered through the finite reviewed routes.

## Coverage and map

The aggregation lane completed 14 targeted live-web queries and documented exact source/artifact windows. This is finite coverage, without an all-internet completeness claim. No paid calls, target requests, DNS lookups, malware execution, new scans or submissions occurred.

After refresh, the selected map inventory contains **6,493 IPs**, including **22 with our source/artifact evidence**. These counts do not represent newly discovered C2s. Hosting enrichment does not increase role confidence. The [map](https://ella-bakshi.github.io/ai-attacker-threat-research/) retains its existing interface and evidence distinctions.

[Records JSON](records.json) · [Records CSV](records.csv) · [Source context](sourced-iocs.csv) · [Supporting tools](supporting-tools.csv) · [Own corroborations](sample-derived-observables.csv) · [Unresolved CSV](remaining-unverified.csv)
