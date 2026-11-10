# India targeting evidence: ARTEX and CyberStrikeAI

Source snapshots reviewed 10 November 2026 (UTC). **This review found no additional public C2 indicator that satisfies all three requirements: an ARTEX/CyberStrikeAI association, an evidenced C2 role, and an India-targeting campaign link.** This finding is limited to the reviewed public material.

| Finding | Primary source and date | Confidence and scope |
|---|---|---|
| Agentic intrusions affected Indian entities; model-evaluation incidents and financially motivated attacks are separate categories. | [CERT-In CICA-2026-3630, 15 October 2026](https://www.cert-in.org.in/s2cMainServlet?CACODE=CICA-2026-3630&pageid=PUBADV01) | High: government campaign context. The notice supplies no infrastructure indicators. |
| CERT-In names ARTEX, CyberStrikeAI, PentAGI and Cairn in the CRAFTY FALCON campaign. Detailed IOCs, infrastructure fingerprints and rules remain in restricted advisories. | [CERT-In CIAD-2026-0058, 4 November 2026](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES02&VLCODE=CIAD-2026-0058); predecessor [CIAD-2026-0046, 9 October 2026](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES02&VLCODE=CIAD-2026-0046) | High: reported campaign/tool association. It does not identify a public per-endpoint India C2 list. |
| `212.11.64.250` was reported as scanning/exploitation infrastructure and independently observed serving CyberStrikeAI. | [AWS, 20 February 2026](https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/); [Team Cymru, 2 March 2026](https://www.team-cymru.com/post/tracking-cyberstrikeai-usage) | High for these historical source facts. An implant C2 role and India campaign association remain unestablished. |

AWS describes activity across more than 55 countries and broad regions including South Asia, without explicitly naming India or publishing the country list. Team Cymru's country breakdown describes server hosting. Those facts cannot connect this infrastructure to the separate Indian campaign. AWS's activity dates, 11 January–18 February 2026, do not establish current operation.

The [public CERT-In defensive blueprint, 25 May 2026](https://www.cert-in.org.in/PDF/Blueprint_for_Defending_against_AI_Assisted_Exploitation.pdf), contains no IP/hash indicators or named ARTEX/CyberStrikeAI infrastructure in its extracted text. No public IOC annex was linked from the reviewed notices.

High confidence here describes verification of the stated primary-source fact. It does not mean current maliciousness, exclusive attacker control, a named Indian victim, or first public discovery. Hosting geography, shared ASNs, cloud-service addresses and common tool use do not establish India targeting. No restricted material, actor-host access or new active measurements were used.

## ARTEX: stronger provenance for existing India-intent context

The exact host `38.244.50.120` occurs in both [Zscaler's 21 October operator-workspace report](https://www.zscaler.com/es/blogs/security-research/inside-global-ai-assisted-hacking-campaign) and [CrowdStrike's 7 October Korean-finance report](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/). Zscaler describes a jump server/default route in an operation whose recovered target prompts include India; CrowdStrike describes an ARTEX instance/open directory at the same address. Confidence is **High for the exact literal match**, **Medium for the scoped historical operational relationship**. This strengthens existing records `AR-8A5971527C1C` and `AR-B21E50F38F2A`; it does not discover a new address, establish a beacon listener or transfer the separate Korean campaign's IOCs to India.

Zscaler also describes custom image tag `artex-local:perf2-20261003`. This remains a **source-curated software-fingerprint lead**: high confidence that the report describes the string, low standalone detection/maliciousness confidence. No image bytes were acquired; tags can be copied or changed. It is not admitted as a confirmed malicious artifact or an independently discovered C2.

Seven ARTEX primary reports and their available figures were rechecked. Country shading describing hosting, generic/demo screenshots and an inaccessible figure were not used as India-victim evidence. The source-conflicted Microsoft IP variants remain quarantined. This source-review subtask made no network measurements; the separate [first-party observation report](../research/first-party/README.md) documents the two subsequent bounded reads.
