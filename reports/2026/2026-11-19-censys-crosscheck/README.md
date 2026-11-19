# 19 November 2026: Censys cross-check and public artifacts

This follow-up adds **24 evidence memberships**: **10 independently derived observations**, **14 externally sourced memberships**, **15 new distinct type/value pairs** and nine existing-value corroborations. Totals: **13,082 canonical records**, **16,575 master values**, **6,503 selected IPs**. There are **seven new map IPs**, all externally reported traffic sources. **No new independently verified malicious C2 IP was found.**

| Evidence class | Memberships | Confidence scope |
|---|---:|---|
| Our exact ARTEX software bytes/assets | 8 | Score 20: four new MD5/SHA1 identities; four SHA256/favicon corroborations |
| Our CyberStrikeAI source derivations | 2 | Score 20: exact stylesheet and untested console hypothesis |
| Sourced exploit-attempt context | 3 | Score 55 historical activity; moderate ARTEX attribution, no C2 |
| Sourced ARTEX-marker observations | 7 | Score 20 client-controlled markers; individual maliciousness unestablished |
| Sourced software/deployment context | 4 | Score 20; no hostile-operation inference |

## Retained leads

All **100 retained ARTEX HTTP-title leads** received exact catalog/list comparisons and targeted public searches. **75 already appear in the [pinned public Talos list](https://github.com/Cisco-Talos/IOCs/blob/23e72502a454456d17a85f147d0e837edfea9489/2026/11/artex-and-beyond.txt); 25 lack an admissible independent public bridge and remain private.** None earned a malicious-C2 promotion. Public software-list membership does not establish current operation or hostile use. No account-only inventory is published.

The earlier CyberStrikeAI session retained a query count, not an address inventory; this follow-up does not claim an individual-address review of that count. No additional Censys or paid-provider calls were made.

## Our findings

Two exact ARTEX-family software artifacts were acquired and examined offline. One is byte-identical to the executable in the maintainer's [13 October ARTEX Global release](https://github.com/jiwoochris/artex-global/releases/tag/v0.3.15-global.1); the ZIP matches its GitHub asset digest. Both contain a known favicon bound to exact Go embedded-file paths and byte ranges. One pinned unrelated Next.js control differs; this finite comparison does not establish global specificity. [Artifact evidence](../../../research/analyst-derived/2026-11-19-crosscheck-software-artifacts/README.md).

[CyberStrikeAI source evidence](../../../research/software-fingerprints/2026-11-19-cyberstrikeai-console/README.md) pins exact stylesheet bytes and an untested three-marker conjunction. These are software references. No new exact campaign-malware sample, malicious configured endpoint or operator relationship was established.

## Aggregation

[Previdian's original 16 November report](https://blog.previdian.com/artex-traffic-previdian-threat-intelligence-report-november-2026/) supplies ten traffic-source addresses: three detailed exploit-attempt contexts and seven weaker marker observations. Seven IPs are new to the map; three already existed. One previously master-only value now has canonical source evidence, reducing the master-only count to 3,739 without adding another IP. Marked UTC dates remain separate from broader source histories, publication and review time. The publisher does not establish common ownership, autonomous selection or successful compromise. None is admitted as C2.

[Spectrum's original 18 November report](https://www.spectrum.security/blog/offensive-ai-tools-in-the-wild) supplies three qualified CyberStrikeAI content markers and an existing ARTEX console corroboration. Its theme-key technique credits Houdin.io. Withheld host lists/provider counts are not imported as malicious IOCs. These records use independent public evidence, not a transformed commercial export.

## Uncertainty and map

The **35 prior unresolved memberships remain separate**: 24 ARTEX/source questions, nine mixed-framework relationships and two certificate siblings. The [carry-forward CSV](remaining-unverified.csv) preserves prior review dates; not every original source was freshly reviewed here. Microsoft's original page still differs between the `.15` hunting-query address and `.16` IOC-table address. New artifact hashes did not bridge these questions. Fresh community-feed C2 claims lacking accessible technical support remain private, separately from the 35 publicly listed unresolved memberships and the 25 account-only leads.

The [map](https://ella-bakshi.github.io/ai-attacker-threat-research/) preserves its interface, geometry, roles and review filters. Only seven new literal IPs are deliberately selected; no domain was resolved into a historical IP claim. Scores are ordinal evidence strength, not maliciousness probabilities. The inventory is not an automatic block list.

Coverage was finite: exact comparisons, targeted live searches, original reports, pinned source and two software artifacts. Verification-gated ThreatFox pages could not be fully reviewed; restrictions were not bypassed. No target DNS/HTTP/TLS requests, scans, sample submissions or artifact execution occurred. The daily schedule remains paused.

[JSON](records.json) · [CSV](records.csv) · [Software references](software-fingerprints.csv) · [Attempt context](campaign-context.csv) · [Marker context](report-host-network-artifacts.csv) · [Deployment context](deployment-leads.csv) · [Summary](summary.json)
