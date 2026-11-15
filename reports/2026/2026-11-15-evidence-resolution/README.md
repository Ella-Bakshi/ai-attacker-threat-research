# AI Attacker Threat Research — evidence resolution, 15 November 2026

All 73 findings separated in the earlier source review were revisited against original reporting, pinned source files and public artifacts. **33 underlying evidence claims are now supported within a narrower, explicit scope; 40 source/relationship questions remain unresolved.** This does not mean 33 new malicious IOCs were verified.

[Record dispositions CSV](review-decisions.csv) · [JSON](review-decisions.json) · [Reviewed records CSV](records.csv) · [JSON](records.json) · [Remaining unresolved CSV](remaining-unverified.csv) · [Current unresolved export](../../../research/unverified-findings/source-review-unresolved.csv)

| Reviewed subset | Supported within scope | Still unresolved |
|---|---:|---:|
| ARTEX, mixed-framework source assignments and disputed-address memberships | 16 | 33 |
| CyberStrikeAI/public sample identities and algorithm qualifications | 10 | 5 |
| Finite signatures, historical measurements and CT relationships | 7 | 2 |
| Total | 33 | 40 |

Eight ARTEX-lane resolutions establish provider-to-publisher identities for four files. Another eight establish pinned dependency/reference facts. They do not prove identical current image contents, malicious maintainers or affected installations. The CyberStrikeAI lane resolves eight source-supported relationships and two exact-artifact identities. Provider facts retain their external origin.

Five authored signatures were reproduced against finite reference files; two historical TLS/timing measurements were reproduced from retained public captures and selected native bytes. **Their operational detection efficacy remains experimental and unvalidated.** They are separately available in [experimental detection hypotheses](../../../research/unverified-findings/experimental-detection-hypotheses.csv), with no production false-positive estimate. The [selected static evidence](bounded-static-evidence.json) preserves reproducible offsets and reference identities rather than raw binaries or private review logs.

## Independently extracted additions

Two exact historical Linux payloads were acquired from a public archive, hashed and inspected without execution. Independent review checked archive-member identity, selected native operands and code-lineage evidence. The artifacts configure HTTP POST requests to **23.254.195.48:18443**, distinct from the 8099 delivery service and the previously examined 8443 configuration.

This adds **seven values new to the catalog/master**: four MD5/SHA-1 crosshashes, one endpoint and two URL paths. It adds **zero new IPs or named malicious-campaign IOCs**. The conclusion is CyberStrikeAI beacon-template lineage; the exact generating revision, operator, campaign, victims and current operation remain unknown. The existing generated-path ELF signature misses these two generic-module variants.

[Artifact analysis](../../../research/analyst-derived/2026-11-15-historical-cyberstrikeai/historical-payload-analysis.md) · [Exact identities and native locators](../../../research/analyst-derived/2026-11-15-historical-cyberstrikeai/historical-payload-static-evidence.json) · [URLhaus source seed](https://urlhaus.abuse.ch/url/3944164/) · [Pinned official template comparison](https://github.com/AIPentest/CyberStrikeAI/blob/b43bdb991c3bee4f433cd1a0a370a90c4e24241e/internal/c2/payload_templates/beacon.go.tmpl)

## Questions that remain open

The remaining 40 records cover 20 AhnLab file/component or host mappings, nine JPCERT per-IP framework assignments, three Microsoft/FBI disputed-octet memberships, one historical repository reference, five hash-algorithm qualifications and two CT sibling-domain relationships. Literal matches or repeated reporting do not resolve those questions. The records preserve sources, review times, limitations and next evidence requirements.

The current `aizhihuxiao/ARTEX` is a new GitHub repository object created after the historical deleted-reference report. Its pinned compose defaults to a different image. The earlier allegation must not transfer to the recreated project. [Identity correction and pinned sources](../../../tools/artex-source-review.md#same-name-repository-correction--15-november).

The earlier [73-row source-review CSV](../2026-11-15-source-review/unverified-findings.csv) remains an explicitly dated historical snapshot. Current canonical records and current category exports carry the later dispositions. No old indicator value, record ID, origin or historical activity date was replaced to increase a count.

This pass used public evidence and bounded offline analysis. It performed no candidate service requests, DNS lookups, scans, executions, submissions or paid-provider calls. Source review is separate from maliciousness, successful communication and current ownership. [Reliability and appropriate use](../../../docs/indicator-reliability.md).

Later review: [deeper source and public-artifact hunt](../2026-11-15-deeper-hunt/README.md) revisits the remaining40 and resolves one digest identity. Its current list has 39 unresolved findings; this folder's dated decision/snapshot exports retain their earlier state.
