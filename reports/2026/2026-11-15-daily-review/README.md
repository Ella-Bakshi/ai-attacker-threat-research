# AI Attacker Threat Research — 15 November 2026

**2,681 reviewed records; 591 new type/value entries and 2,090 additional source/analysis memberships.** Counts span evidence classes, not confirmed malicious servers. The 14 November attempt was interrupted; this report uses actual 15 November retrieval/review dates.

| Evidence class | Records |
|---|---:|
| deployment-leads | 2,551 |
| sourced-iocs | 80 |
| supporting-context | 13 |
| shared-services-and-generic-markers | 4 |
| software-fingerprints | 2 |
| report-artifact-observables | 26 |
| artifact-derived-observables | 3 |
| sample-derived-observables | 2 |

[Complete CSV](indicators.csv) · [JSON shard index](records-index.json). Each evidence class has its own CSV.

The initial FBI/Talos/Elastic source batch contributes 495 new exact type/value entries against the 15,349-row master baseline. Additional AWS, historical backfill and independent artifact evidence are included in the report totals above. These are research values, not a count of newly malicious systems.

[Cisco Talos](https://blog.talosintelligence.com/artex-and-beyond/) published 2,546 literal ARTEX-associated IPv4 addresses in a [pinned public list](https://github.com/Cisco-Talos/IOCs/blob/23e72502a454456d17a85f147d0e837edfea9489/2026/11/artex-and-beyond.txt). They remain deployment leads: per-address malicious operations, observation dates, co-located-tool invocation and common ownership were not established. 375 addresses are new to the selected-IP overview; 487 exact IPv4 type/value rows are new to the master. Some IPs were already known through endpoint or other records. The IOC repository uses CC0 1.0.

The [FBI FLASH](https://www.ic3.gov/CSA/2026/261113.pdf) supplies additional source support for 24 IPs and an LLM reseller, plus four legitimate API endpoints retained as shared context. The official PDF exactly matches the user-provided PDF by SHA256. It compiles earlier Microsoft, CrowdStrike and Censys reporting; it is not additional independent telemetry. Proxy/VPN, WISP C2, ARTEX server and reseller roles remain distinct. The grouped October 15-16 VPN window is not invented per-IP first/last seen; active-as-of November 6 remains that statement.

[Elastic](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion) attributes AWS activity to 43[.]240[.]29[.]11 between September 30 and October 16. Two related management-page addresses, 43[.]240[.]29[.]28 and .33, were absent from that AWS investigation. Their certificate/content linkage does not prove campaign participation. Port 8080 is a management interface, not an established beacon protocol. The publisher could not prove an LLM made the decisions and says the interfaces were no longer serving as of November. A serial and FOFA content identifier remain conditional software fingerprints.

All additions here are external-report curation. Raw pages/PDFs, private QA and commercial data remain private. No target contact, DNS lookup, paid provider call, sample execution or first-party incident telemetry was performed.

An additional [AWS primary report](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/) contributes eleven source-table addresses and exact day-precision date ranges. MadPot received agent-memory requests; reported external victim outcomes were not verified. Amazon assesses ARTEX attribution with moderate confidence. Network functions remain unspecified, without a tasking-server inference.

Historical backfill adds [MiniFast / Nimbus Manticore](https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/) campaign hashes/domains, [TuxBot v3](https://unit42.paloaltonetworks.com/tuxbot-v3-evolution-iot-botnet/) sample references and distinct payload/C2 roles, and [CLOSEDQUORUM](https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/) development-chain hashes. MiniFast AI development assistance is vendor-assessed; per-domain delivery versus tasking roles remain unspecified. TuxBot compiled reference variants do not inherit a per-hash victim-deployment claim. Talos explicitly lacked confirmation of CLOSEDQUORUM field deployment.

[Our exact VoidLink artifact analysis](../../../research/analyst-derived/2026-11-15-voidlink/README.md) adds three file-hash identities for one artifact and corroborates a known IP/8080 pair. It preserves the previous variant’s default 443 separately; both allow overrides. No first-party incident telemetry, current liveness or global-first claim is made.

The [tool index](../../../tools/README.md) now holds 37 identities: four additions and five release updates. PenPard has noncommercial source-available terms; it is not labeled OSI open source. No malicious IOC or runtime fingerprint follows from tool inclusion.

Coverage limits: parsed primary Elastic content was reviewed after its raw download timed out. The complete pinned Talos TXT was processed; STIX JSON processing is not claimed. No exact new malicious IOC was returned by the bounded AutoCVE queries. Unreviewed leads remain in the private backlog. No paid/Censys calls, target requests, DNS, external scans, sample submissions or execution.
