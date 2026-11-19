# 19 November 2026: exact public beacon recovery and source hunt

We recovered **two exact public CyberStrikeAI-lineage ELF payloads** and independently verified their static configuration. This pass adds **125 memberships: 19 own derivations and 106 external memberships**, representing **122 new type/value pairs** and three existing-value corroborations. Totals: **13,388 canonical records**, **16,861 master values**, **6,625 selected IPs** and **23 IPs with our artifact evidence**.

| Evidence class | Memberships | Scope |
| --- | ---: | --- |
| Our exact sample identities/configuration | 18 | Two acquired files, hashes and native request operands; score 60 |
| Our reported-public-key derivation | 1 | Deterministic SSH fingerprint; ownership remains source-assessed |
| External campaign/workbench context | 14 | CyberStrikeAI-associated workbench; unauthorized activity assessed at moderate confidence |
| External sourced incident observables | 68 | Separate PHP2Shell AI-assisted campaign; no ARTEX/CyberStrikeAI attribution |
| External supporting tools | 14 | Public tools and staged components; shared bytes do not connect campaigns |
| External host/persistence artifacts | 8 | Contextual matching required |
| External software fingerprint | 1 | Default workspace path, not maliciousness proof |
| External shared host-comment context | 1 | Nonindicative hostname; score 0 |

## Our recovered payloads

The [sample analysis](../../../research/analyst-derived/2026-11-19-cyberstrikeai-public-beacons/README.md) preserves exact hashes, archive members, acquisition times, size, pinned source comparisons and native offsets. An offline search of **87 retained public archive inventories / 53,114 entries** selected two files by size. Size was only a candidate filter; acquired bytes, specific code correspondence and native operands establish the accepted observations.

| Exact sample SHA256 | Configured destination |
| --- | --- |
| `395ff8ba0708845abed2e6d4a3fc5b3c70702582d8a8f970ab46edb395f8509b` | `116.228.56.131:8443`, new to our repository |
| `5a8d7ca92610b3bb9d573e4aaf2dfec3e66f274e9609a7117ef6eab1a724cd2b` | `23.254.195.48:8443`, existing address, new exact-sample evidence |

Both use HTTPS POST `/check_in` and `/result`, with GET `/tasks?session_id=` and `/file/` prefixes. Dynamic IDs, keys and implant tokens are omitted. All **66 recovered application functions per file** were reconstructed offline, within **6,372 total Go functions per file**; the remaining 6,306 runtime/dependency functions were not all decompiled. Complete semantic understanding is not claimed. Independent native checks verify URL pointers, lengths, methods and constructor calls. Specific function correspondence and embedded `v1.7.18+dirty` metadata support lineage; the modified working tree prevents asserting an exact generating revision.

Score **60** means exact static configuration examined. It does not prove malicious use, successful callbacks, an operator, victims, current operation or country targeting. These files differ from the still-missing exact Kaspersky samples. No global first-discovery claim is made.

The [public-key supplement](../../../research/analyst-derived/2026-11-19-cyberstrikeai-workbench-key/README.md) independently parses a researcher-published ed25519 blob, reproduces the reported 101-byte public-file SHA256 and derives its OpenSSH fingerprint. This is another representation of a reported public key, separate from malware recovery or proof of ownership.

## Aggregation

[The Hunter's Ledger INV-2026-080](https://the-hunters-ledger.com/reports/inv-2026-080-cyberstrike-ad-workbench/) supplies 26 source memberships, including `199.247.13.103` with distinct port roles. Supporting tools and default software paths remain separate. The displayed publication date and later source-control chronology are retained separately; no victim-side telemetry or agent trace was available to us.

[SOCRadar's 18 November investigation](https://socradar.io/blog/php2shell-ai-agents-credential-harvesting/) supplies 80 reviewed observables from a separate maq/modified-omp campaign. Three IPs, explicit endpoints, hashes and SSH fingerprints retain source roles. The publisher's moderate-confidence unauthorized/financial assessment and low actor-identity confidence are preserved. Common paths, staged public exploits and a host-comment name remain qualified. [Source evidence](socradar-source-evidence.json).

**Five addresses join the map**: one exact static configuration, one reported workbench and three separate incident infrastructure addresses. The known `23.254.195.48` retains prior memberships and gains this sample's evidence. Scores are ordinal evidence strength, not maliciousness probabilities. The interface, footer and India-view geometry are preserved.

## Missing artifacts and unresolved relationships

The exact encrypted BLOODALCHEMY payload `364251838edfcf5ef1107fa692da3c5bd9a540482449f645992830134bf807ab` remains unacquired. A new filename-only staging hypothesis has no verified file hashes/bytes and conflicting port claims; it stays private. Archive searches yielded no payload; Common Crawl failed. No plaintext/configuration was invented from the previously acquired loader.

The trojanized ARTEX `d5070f...` executable and requested exact Kaspersky bytes were not recovered. Fourteen new report-backed artifact hashes had no exact match in the retained inventories. Failed or restricted routes were not bypassed.

The **25 private Censys leads** and **35 canonical relationship questions** remain unresolved. New configurations and source values provide no exact bridge. Earlier review dates remain in the [carry-forward CSV](remaining-unverified.csv); negative searches do not establish benignness. Coverage is finite, with private query/acquisition ledgers and recorded gaps. No candidate contact, scanning, sample execution/submission, Censys call or paid-provider call occurred. The schedule remains paused. The mixed inventory is not an automatic block list.

[Full JSON](records.json) · [CSV](records.csv) · [Summary](summary.json) · [Own sample facts](sample-derived-observables.csv) · [Sourced incident observables](sourced-iocs.csv) · [Campaign context](campaign-context.csv) · [Supporting tools](supporting-tools.csv) · [Report artifacts](report-artifact-observables.csv) · [Software fingerprints](software-fingerprints.csv) · [Shared context](shared-services-and-generic-markers.csv)
