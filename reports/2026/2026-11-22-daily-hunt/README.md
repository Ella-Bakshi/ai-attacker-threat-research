# 22 November 2026 global source and public artifact hunt

This review adds **30 source records**, covering **29 new type/value pairs**. The map gains **11** historical source-reported IPs. None is an independently derived malicious IOC. [Catalog rows](records.csv) · [Full records and source locators](records.json) · [Counts](summary.json)

| Evidence class | Records | Basis |
| --- | ---: | --- |
| Source-reported incident indicators | 17 | First-party telemetry and published artifacts, including new historical backfill and separate source roles. |
| Supporting artifacts | 5 | Three reported ARTEX working-directory basenames and two file hashes for contextual hunting. |
| Independently derived software fingerprints | 8 | SHA-256 calculated from exact public artifact bytes. These identify software evidence only. |

## Source-reported findings

- **SILENT CLAIMANT.** Eight individual addresses with dated scanning or SMTP relay roles. Exaforce suspects ARTEX-like automation. The report does not establish the exact framework or a C2 service for those addresses. The network prefix and the address associated only with a domain of unknown purpose were excluded. [Exaforce original investigation](https://www.exaforce.com/blogs/silent-claimant-artex-aws-data-exfiltration)
- **African stock exchange intrusion.** One exact observed DNS callback token from the toolkit. The session took place on 20 September 2026 from 08:44 to 08:47 UTC at the published minute precision. The public testing service parent is shared. Collector-side receipt and toolkit attribution of co-resident implants remain unresolved. [Symantec original investigation](https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack)
- **JADEPUFFER and ENCFORGE.** Two July reports add three individual addresses, one exact configured beacon URL, one historical C2 endpoint, and two SHA-256s of the packed and unpacked ransomware. One address appears twice because the reports document different roles. Success of the first campaign's claimed staged exfiltration is unverified. No link to ARTEX or CyberStrikeAI is established. [Initial Sysdig report](https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion) · [Follow-up Sysdig report](https://www.sysdig.com/blog/jadepuffer-evolves-the-agentic-threat-actor-deploys-ransomware-built-to-destroy-ai-models)
- **ARTEX supporting artefacts.** Three basenames were added from AhnLab's original report on exposed working directories. Case associations and exact hash bindings remain unresolved. [AhnLab source](https://asec.ahnlab.com/ko/95844/)
- **ARTEX workbench recovery.** Odin reported two playbook SHA-256s from an exposed ARTEX workbench. Those records preserve the publisher’s Hunt disposition and unknown execution outcome. [Odin original investigation](https://brandefense.io/odin-research/reports/stolen-cloud-keys-backdoored-wordpress/)

## Our independently verified artifact observations

We computed the SHA-256 of the 18,968-byte Core Metadata text sidecar for each of the five Strix Agent 1.7.0 platform wheels and obtained the same result as PyPI's listed Core Metadata digest. It identifies the sidecar bytes. [Strix Agent release](https://pypi.org/project/strix-agent/1.7.0/#files) · [PyPI package index](https://pypi.org/simple/strix-agent/)

We computed SHA-256 and Git blob identity for the 30,280-byte CyberStrikeAI v1.8.1 schema asset. The v1.8.0 file has the same bytes. The pinned v1.8.1 source declares that it embeds this asset. [Upstream release](https://github.com/AIPentest/CyberStrikeAI/releases/tag/v1.8.1) · [Pinned asset](https://raw.githubusercontent.com/AIPentest/CyberStrikeAI/af6cf7500c8eff357cc6c3f50e7c7b150fcfa836/internal/database/schemas/application.sql) · [Exact v1.8.0 match](https://raw.githubusercontent.com/AIPentest/CyberStrikeAI/02ec1afcb9725f4fe44240f0918c59aefa18a7e7/internal/database/schemas/application.sql) · [Embedding declaration](https://github.com/AIPentest/CyberStrikeAI/blob/af6cf7500c8eff357cc6c3f50e7c7b150fcfa836/internal/database/schema_reconcile.go#L12-L13)

The v0.7.0 ARTEX source also embeds a distinct 96,010-byte schema asset. We recomputed its SHA-256 and Git blob identity. [ARTEX release](https://github.com/BaaRai/ARTEX/releases/tag/v0.7.0) · [Pinned asset](https://raw.githubusercontent.com/BaaRai/ARTEX/22ae88afabf66e47e73644a0528d8b427c4c80b8/db/schema.sql)

**Five vendor block entries match public release files.** We independently reproduced five SHA-256 matches in Odin Monograph 04. The files are two CyberStrikeAI release-source scripts and three ARTEX archive files. Three ARTEX files also match the v0.3.26 archive, and the CyberStrikeAI upgrade script also matches v1.8.1. Use these digests for identifying software and corroborating telemetry. [Odin report](https://brandefense.io/odin-research/reports/autonomous-ai-offense-and-llm-gateway-attacks/) · [CyberStrikeAI v1.7.24 source](https://github.com/AIPentest/CyberStrikeAI/tree/4ca8b7d33663cd4ba8213f4afa8194ae1928ef16) · [ARTEX v0.3.18 archive source](https://github.com/RuoJi6/ARTEX/tree/648bafb5938395b22c9d4573d48bfaac44c6449a)

## Unresolved and contextual evidence

The 35 existing canonical relationship questions and 25 private provider leads retain their previous status. Original JPCERT/CC and AhnLab lists verify exact values but leave the individual roles open. Microsoft's prose and IOC table continue to differ from one query literal. The EU Commission did not name ARTEX in its briefing, and ScanMalware did not release individual IPs in its aggregate telemetry. [JPCERT/CC alert](https://www.jpcert.or.jp/at/2026/at260030.html) · [Microsoft original](https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-sector/) · [European Commission briefing](https://audiovisual.ec.europa.eu/en/media/video/I-298222) · [ScanMalware report](https://scanmalware.com/blog/ai-hacking-agents-using-our-data)

The run used original public publications, exact package metadata and pinned non-executable assets. We accessed no reported network observable. Use source roles and observation dates to guide correlation before enforcement.
