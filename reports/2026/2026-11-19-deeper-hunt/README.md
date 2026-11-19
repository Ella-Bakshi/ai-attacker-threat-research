# 19 November 2026: deeper artifact and original-source hunt

This pass adds **181 evidence memberships**: **four independently derived observations** and **177 external memberships**. They add **164 distinct type/value pairs** and 17 existing-value memberships. Totals: **13,263 canonical records**, **16,739 master values**, **6,620 selected IPs**. No new exact ARTEX/CyberStrikeAI campaign-malware file or independently verified malicious C2 IP was obtained.

| Evidence class | Memberships | Evidence-strength limit |
|---|---:|---|
| Reported historical operator/incident context | 23 | 55; no new C2 classification |
| Public software/deployment observations | 84 | 20; includes adjacent and stock consoles |
| Shared services and generic markers | 38 | 0; includes 31 shared proxy exits |
| Software/reference patterns | 28 | 20; includes our two native patterns and one public-key representation |
| Qualified incident naming artifacts | 7 | 20; correlation required |
| Our sandbox host-summary corroboration | 1 | 20; no flow, destination port or successful connection established |

## Our reproducible work

The [BLOODALCHEMY loader review](../../../research/analyst-derived/2026-11-19-bloodalchemy-loader-native/README.md) extends an already acquired exact campaign-supporting DLL from 15 selected functions to **333/333 discovered internal functions reconstructed**. This finite inventory includes runtime/library routines and is not a claim of complete behavioral understanding or absence of undiscovered code. Detailed native operands establish a 16-byte AES-128 key prefix/CBC-zero-IV payload format and a conditional fixed host-offset redirection/callback chain. An inert translation matched six synthetic cryptographic reference cases. The actual encrypted payload remains missing; no key/plaintext/C2 was recovered from it. These are sample-specific capability patterns, separate from the ARTEX framework and production detections.

The [CyberStrikeAI public-analysis supplement](../../../research/analyst-derived/2026-11-19-deeper-public-sandbox/README.md) independently extracts one existing host value from an exact, hash-bridged provider JSON. Its populated host summary coexists with empty flow arrays; it does not prove a request or successful C2 exchange. No malware or PCAP bytes were acquired. This is new selection/analysis of a retained public artifact, not new sensor telemetry.

The [Ultra-suite public-key supplement](../../../research/analyst-derived/2026-11-19-ultra-spki/README.md) reconstructs a 91-byte DER SubjectPublicKeyInfo from a displayed P-256 public point. Two encodings reproduce the advertised fingerprint. Full certificate DER acquisition failed; certificate signature, deployment, ownership and a CyberStrikeAI service-port association were not established. Public keys are distinct from private credentials.

## Aggregation and classifications

[Profero's 31 October Ultra-suite report](https://profero.io/blog/ultra-suite-artex-ai-attack-agents/) supplies three qualified operator hosts, domains, shared proxy context and software markers. Its **60 Cairn addresses are explicitly adjacent deployments with no observed use against the investigated targets**; they remain score 20. **31 commercial Thordata exits remain shared context at 0**. No prefix, ASN or advertised proxy pool was expanded. A generic nginx-only watch address was withheld. We retain the report's infrastructure observations without inheriting its broad block-list recommendation.

[Profero's 4 November operator-file case](https://profero.io/blog/inside-the-ai-operator/) is a separate TGSEC context. Exact jump, egress, collection and worker ports are retained; no individual ARTEX or beacon-tasking relationship is invented. [Barracuda's advisory](https://trust.barracuda.com/security/barracuda-xdr-integration-credentials) provides four network indicators, generic clients and seven resource/workflow/branch artifacts. Initial publication on 10 November, the 13 November update and the 1–2 November incident window remain separate; exact per-IP event times are unknown.

[RST Cloud's 2 November report](https://www.rstcloud.com/hunting-ai-harnesses-cairn-artex-pentagi/) contributes 22 memberships from 19 public host rows, all passive software context at 20. Three rows identify multiple frameworks; their row-level ports are not arbitrarily assigned to a particular framework. A November Cairn sighting does not resolve the earlier JPCERT mixed-framework attribution question. [Detailed source context](source-context.md) and [source locators](source-evidence.json) preserve these limits.

The map adds **117 distinct addresses**: 18 historical context nodes at 55, 68 software leads at 20 and31 shared proxy nodes at 0. These are not 117 newly discovered controllers or attacks. Existing stronger memberships remain visible; our evidence-IP count stays 22.

## Remaining questions and coverage

All **25 private Censys leads remain admission-unresolved**. Five also occur in a Shodan-derived public feed, but collector provenance/redistribution support and an incident/sample bridge are insufficient. Those imports remain private; absence from other searches does not mean a host is benign.

All **35 canonical relationship questions remain separate**, with prior review dates retained in the [carry-forward CSV](remaining-unverified.csv). New targeted routes did not resolve the AhnLab component mappings, Microsoft address conflict, deleted/recreated repository question, JPCERT time/framework mappings or two certificate siblings. Prior original-source reviews are retained rather than represented as freshly repeated. The ARTEX forensic repository and existing payload crosshash metadata were already covered and are not counted as new discoveries.

Exact sample searches, public metadata and retained archive-directory comparisons found no new accessible requested campaign bytes. Authentication/verification restrictions and failed certificate downloads were not bypassed. Coverage is bounded to the recorded sources, queries and artifact windows; there is no all-internet completeness claim. No candidate DNS/HTTP/TLS request, scan, sample submission, artifact execution, Censys call or paid-provider call occurred. The daily schedule remains paused.

The [live map](https://ella-bakshi.github.io/ai-attacker-threat-research/) retains the existing interface, footer and India-view geometry. Scores are ordinal evidence strength, not maliciousness probabilities. The mixed research inventory is not an automatic block list.

[Full JSON](records.json) · [CSV](records.csv) · [Summary](summary.json) · [Historical context](campaign-context.csv) · [Deployment leads](deployment-leads.csv) · [Software references](software-fingerprints.csv) · [Shared/generic context](shared-services-and-generic-markers.csv) · [Incident artifacts](report-artifact-observables.csv) · [Own host summary](artifact-derived-observables.csv)
