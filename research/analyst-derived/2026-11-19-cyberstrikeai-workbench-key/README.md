# CyberStrikeAI workbench: original-source review and public-key derivation

Reviewed **19 November 2026**, with source captures at **17:47–17:51 UTC**. This supplement adds a carefully qualified source membership for The Hunter’s Ledger’s **INV-2026-080** workbench case. It adds **no recovered malware sample** and makes **no present-day service or victim-access claim**.

The [original researcher report](https://the-hunters-ledger.com/reports/inv-2026-080-cyberstrike-ad-workbench/) describes CyberStrikeAI workspace artifacts and supporting tools associated with activity against Portuguese government organizations and a hosting provider. The author assesses unauthorized activity at **MODERATE** and holds no victim-side telemetry or agent trace. The framework is legitimate public software; these observations concern the described operator workbench, and do not make every installation malicious.

| Evidence class | Source memberships | Our treatment |
|---|---:|---|
| Reported campaign/workbench context | 14 | Six custom binary hashes, the historical IP and three port-specific endpoints, three reported file/web paths, and one public-key blob; score 55 |
| Supporting tools and host labels | 11 | Three exploit-source hashes, five public-tool builds, a named pipe, an account name and a key comment; stock public tools score 20, qualified case-specific context 55 |
| Software fingerprint | 1 | Default CyberStrikeAI workspace path; score 20 |
| Our public-artifact derivation | 1 | OpenSSH SHA256 fingerprint of the same researcher-reported public key; historical context score 55 |

These are **27 source/derivation memberships and 26 new exact type/value pairs** against the reviewed repository baseline. The stock GodPotato hash `9a8e9d587b570d4074f1c8317b163aa8d0c566efd88f294d9d85bc7776352a28` already occurs in an unrelated source membership. Shared public-tool bytes do not connect the operators or campaigns.

The source’s raw typed feed contains 26 entries. Its web table shows a different total because it counts filenames separately and presents fewer other types. We use the typed raw feed and preserve each role, rather than treating either display total as a count of confirmed malicious C2s. The low-confidence passive-DNS name in the source’s separate “hunt only” section is **not admitted** here; its relationship to this operator remains uncertain.

## Historical infrastructure scope

The researcher describes `199[.]247[.]13[.]103` as a workbench with a directory service on port **8000**, reverse-chisel configuration referencing **8081**, and tool staging on **8090**. These roles stay separate. A reported HTTP 404 on 7 October does not prove a working tunnel, and the directory’s reported first indexing on 26 September is not an operator-tenure or victim-activity date. The address has hosted unrelated historical tenants; ownership and current use remain unresolved.

The six operator-built binary hashes identify components described by the researcher, including a DNS plugin, PwnKit variants and renamed GodPotato forks. We have not obtained these files, recalculated their hashes from binary bytes, or independently reproduced their native behavior. The publisher’s claim that a component was built or staged is not evidence that it ran successfully on a victim.

## Our reproducible public-key observation

We independently derived the OpenSSH fingerprint:

```text
SHA256:8Z2YBFJZXnzgsd4P9WCJuIvCLqIOOkkOQ487Mgr0JU8
```

The input is the explicitly public ed25519 blob at JSON pointer **`/behavioral_indicators/2/pattern`** in the [pinned original publisher feed](https://raw.githubusercontent.com/PixelatedContinuum/Threat-Intel-Reports/327811a25b31768f4b4cc1b227f3f0d18c8b9c2a/ioc-feeds/inv-2026-080-cyberstrike-ad-workbench-iocs.json). Strict Base64 decoding gives **51 bytes**. Parsing its SSH length-prefixed fields yields type `ssh-ed25519` and a **32-byte public key**. SHA256 over the complete decoded blob, encoded as unpadded Base64 with the `SHA256:` prefix, gives the value above. The local OpenSSH fingerprint reader independently returned the same result.

As an identity check, reconstructing `ssh-ed25519 <published-blob> pentest@cyberstrike` followed by one LF yields **101 bytes** and SHA256 **`da51e1172372b6b1db1fec48ee5c8239e52ee3fc0ef498c3b9df85cd2d9a3fae`**, exactly matching the researcher’s public-file hash. This confirms the deterministic reconstruction and fingerprint calculation. It does **not** independently establish key ownership, successful authentication, victim compromise or current infrastructure. The fingerprint is another representation of the same reported key, useful for reviewing historical key and authentication records; it is not a new operator or an independently discovered malicious C2.

## Sources, dates and limits

The [report](https://the-hunters-ledger.com/reports/inv-2026-080-cyberstrike-ad-workbench/) displays **12 November 2026** as its publication/update date. [Source-control history](https://github.com/PixelatedContinuum/Threat-Intel-Reports/commits/main/reports/inv-2026-080-cyberstrike-ad-workbench/index.md) separately shows a first preview on **13 November at 01:52:16 UTC**, a go-live commit at **16:57:27 UTC**, and a later report edit on **14 November at 02:37:46 UTC**. We retain the displayed date and this chronology separately. Neither is an incident or file-execution timestamp.

The [pinned report](https://github.com/PixelatedContinuum/Threat-Intel-Reports/blob/327811a25b31768f4b4cc1b227f3f0d18c8b9c2a/reports/inv-2026-080-cyberstrike-ad-workbench/index.md) and [typed feed](https://raw.githubusercontent.com/PixelatedContinuum/Threat-Intel-Reports/327811a25b31768f4b4cc1b227f3f0d18c8b9c2a/ioc-feeds/inv-2026-080-cyberstrike-ad-workbench-iocs.json) are published by **Joseph Harrison / The Hunter’s Ledger under CC BY 4.0**. Attribution and source links are retained per record. The live and pinned typed feeds were byte-identical when retrieved. Their SHA256 is `e589521c2f555fc4ce8214dc36a3440707b811c87eb69b1177064ab3af473b57`.

All 14 feed hashes were compared offline with **87 previously retained archive directory inventories containing 53,114 entries**, with no exact filename match. That is a finite acquisition check, not evidence that the files are unavailable everywhere. The original publisher’s complete pinned repository tree and release collection offered no relevant binary download. We did not access the operator directory, victims, paid providers, or restricted sample downloads.

Scores describe evidence strength, not the probability of maliciousness. These mixed records are for qualified historical hunting and source review, and are not an automatic block list. No India targeting claim, named-actor attribution, additional malware recovery or resolution of the existing uncertain leads follows from this supplement.
