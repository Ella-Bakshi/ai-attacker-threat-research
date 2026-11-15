# CyberStrikeAI: PEAK public-artifact review — 15 November 2026

One additional Windows artifact was acquired from a public malware archive and statically examined. It adds **three exact hash values for one sample**, with new independent configuration evidence for **seven already cataloged observables**. There are **zero new IP addresses** and **zero newly verified malicious-campaign IOCs** in this supplement. These counts do not describe successful connections or current infrastructure.

## Preparation

**Hypothesis:** a public Windows sample carrying conflicting AdaptixC2 and CyberStrikeAI labels contains a CyberStrikeAI-generated beacon, and native configuration can establish its intended endpoints more reliably than provider tags.

Required proof: exact source-to-sample identity; bounded acquisition; an official source comparison pinned to a revision; generated application metadata plus multiple specific function correspondences; native references and lengths proving that endpoints are request arguments; and benign/component controls. An unreferenced URL, common Go/HTTP marker or label alone would fail admission.

The seed was the [MalwareBazaar entry](https://bazaar.abuse.ch/sample/1b95c2783b667ad5ffbd5b66afc367a92c314f507ba43789ec0bcda5a623a877/). Its Database Entry identifies the hash and size; its ANY.RUN block contains the `cyberstrikeai` tag, while its main signature and Triage block say AdaptixC2. Its Triage config block quotes the already known endpoint. This is source-backed candidate provenance, not acceptance of a vendor family label. The entry warns that database inclusion does not guarantee maliciousness.

## Execution

Only the exact SHA256-named member of the public `2026-10-08.zip` archive was acquired using finite HTTP206 ranges. ZIP identity, uncompressed size, CRC32 and full SHA256 were verified. MD5 and SHA1 were independently computed over the resulting bytes. No other member bodies were downloaded. The artifact was never executed and candidate infrastructure was never contacted.

| Identity | Value |
|---|---|
| SHA256 | `1b95c2783b667ad5ffbd5b66afc367a92c314f507ba43789ec0bcda5a623a877` |
| SHA1 | `dd0152236bf703e6c95cfc66c9d6a4d163abb67f` |
| MD5 | `23d02815c2d88958feb4b314ab3c1b9c` |
| Size / type | 6,314,496 bytes; PE32+ Windows AMD64 |
| Acquired | 2026-11-15T15:19:54.434896Z |
| Provider sample first seen | 2026-10-08T18:40:16Z; sample timestamp only |

Go metadata identifies `cyberstrike-ai/tmp/c2/payloads/build-0a5e557f`, Go1.25.0, Windows/AMD64, and public [base commit d2084a9](https://github.com/AIPentest/CyberStrikeAI/commit/d2084a948195d60fe7d66f8a8f1f5d901bb5dd3f). It also says `vcs.modified=true`. The base commit is independently reachable; the exact generated source and local modifications remain unknown.

The Go table yielded 6,433 function boundaries/names, including 66 `main` functions. Forty-two source-declared function names match the 43 sample base-function names; the remaining `init` is compiler initialization. These are recovered names and selective native operand checks, **not** a claim that every native function was decompiled. Compare the [pinned official beacon template](https://github.com/AIPentest/CyberStrikeAI/blob/d2084a948195d60fe7d66f8a8f1f5d901bb5dd3f/internal/c2/payload_templates/beacon.go.tmpl), including `fetchC2FileByID`, `checkIn`, `fetchTasks`, `reportResult`, `buildTaskReport`, `handleSocks5` and `taskLoadAssembly`.

## Analysis

At native address `0x140260796`, `main.checkIn` loads the URL at file offset3,512,983. The following length argument is34, and the request constructor call at `0x1402607b4` resolves to `net/http.NewRequestWithContext`. Separate native operands identify method POST. The exact URL is `http://23.254.195.48:8443/check_in`.

At `0x140261782`, `main.reportResult` loads `http://23.254.195.48:8443/result` from file offset3,508,108 with length32; call `0x1402617a0` resolves to the same constructor, with method POST. The base descriptor at `0x1403c98a0` points to the25-byte base URL at file offset3,492,414. `/tasks`, `/file/`, the format strings and GET operands corroborate the existing task URL template and file prefix. These establish intended static configuration, not an observed exchange or successful registration.

**Competing explanations:** provider labels may describe overlapping detections, a misclassification or another family relationship. We preserve AdaptixC2 as an alternative provider classification. We conclude high-confidence CyberStrikeAI generated-beacon code lineage from native/source evidence; we do not claim that all alternative labels are disproven. Shared controller configuration with the older ELF sample does not establish the same operator, campaign, victims or current ownership. The new sample is not one of the four exact Kaspersky-reported beacon hashes.

**Negative controls:** the generated-path / two specific application functions / two header-name conjunction is present in this PE and absent as a conjunction in four local references: ARTEX, the official-source local CyberStrikeAI controller, a third-party egress component and the benign Go compiler. Header names also occur in the controller, demonstrating why single generic markers are insufficient. This finite check provides no production false-positive estimate. The existing ELF-only lineage signature misses this Windows artifact; its Linux shell CWD marker is absent. Broad cross-platform coverage must not be claimed.

**Confidence:** exact sample identities are locally verified. The static configured-role evidence uses score60 under the repository rubric; this is ordinal evidence strength, not probability of maliciousness. Native lineage confidence is high; malicious operation, named campaign, India targeting and present liveness remain unestablished.

## Knowledge and coverage limits

The supplement provides three new hash records and evidence additions for seven existing records, whose IDs are retained in the JSON/CSV. No automatic blocking classification is proposed. Whole-source copies, binaries, keys, raw requests, native C and decompiler projects are excluded.

The [Securelist report](https://securelist.com/tr/cyberstrikeai-attacks/121715/) and public Triage overview for SHA256 `1c6498f081ff7a5ef0e851d2c106668aef53e1384b8d0c52fa667e53a5664c33` were revisited. The latter explicitly bridges MD5 `805b9e4ae74c903787416800999b8418` to SHA256, but no new bytes were available. Twenty-one retained public archive inventories (14,498 entries), plus complete Nov12/Nov13 directories (823/669 entries), did not contain that seed. Nov14 returned404. This finite absence is not a claim of universal unavailability.

Detailed Triage task pages and other exact-hash searches returned403; those paths were stopped. URLhaus reference3946443 could not be reviewed because the normal page returned a browser challenge. The MalwareBazaar public web reader returned the substantive entry; a separate direct HTTPS capture returned a browser check and was not treated as metadata evidence. No restriction was bypassed. The remaining Securelist32-hex hashes have no fresh independently confirmed MD5 bridge from this lane. The previously exhausted ELF and historical80-event supplement were not rerun.

Independent peer review on 15 November at 15:28:33Z confirmed the exact hash identities, PE mapping, Go function table and bounded native endpoint/request arguments. The seven existing observable IDs in this analysis are preserved as corroboration targets; the canonical dated supplement gives each new sample observation its own stable ID.

Next steps: seek a lawful public exact-byte/hash bridge for the remaining named Securelist variants; review URLhaus3946443 only if its ordinary public page becomes available. No new campaign or malicious-infrastructure assertion should be made without separate evidence.
