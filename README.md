# AI Attacker Threat Research

Research into the abuse of AI offensive frameworks and AI-assisted malware development, with sources, dates, scoped confidence and reproducible static evidence. Snapshot: **24 November 2026**.

## IP overview and map

[**Live interactive map**](https://ella-bakshi.github.io/ai-attacker-threat-research/) · [**Main IP CSV**](data/ip-overview.csv) · [JSON](data/ip-overview.json) · [Enrichment and automatic updates](docs/enrichment-and-map.md)

The main CSV contains IP, source-observation timestamp, ASN, hosting/network organization, location and a documented confidence score. The map separates passive deployment leads, campaign infrastructure and our derivations. Hosting geography is separate from India targeting; scores express evidence strength, not a maliciousness probability. The [coverage snapshot](data/enrichment/summary.json) records matched and unmatched enrichment.

[![IP infrastructure map](maps/world.svg)](https://ella-bakshi.github.io/ai-attacker-threat-research/)

**This is a research inventory, not an automatic block list.** Review the [evidence classes and reliability limits](docs/indicator-reliability.md) before enforcement.

The inventory total counts unique IP addresses across evidence classes. It does not count active AI agents, successful attacks or systems targeting a particular country. The current catalog has **14,064 canonical source records**; the master has **17,470 distinct type/value pairs**, including **3,733 master-only historical values**. These counts include hashes, domains, paths, patterns and multiple source memberships for one IP. They differ from the map's selected unique-IP count.

## Tool index

[**57 verified project identities and resources**](tools/README.md), including fourteen added on 21 November, with earlier additions retained: capabilities, official sources/fork lineage, releases, license qualifications, AI features and scoped abuse evidence. Early releases and adjacent general agents remain labeled. [Our two source identification hypotheses](tools/source-identification-hypotheses.json) are runtime-untested software research, separate from admitted IOCs.

## Our findings

On 24 November, we independently verified three upstream software assets. The same review adds 13 source-reported observations and 3 selected map IPs. [24 November hunt](reports/2026/2026-11-24-daily-hunt/README.md).

On 22 November, we independently verified 8 software artifact fingerprints. The same review adds 22 source-reported memberships and 11 historical IPs to the inventory. The 35 unresolved relationships and 25 private leads retain their previous status. [22 November hunt](reports/2026/2026-11-22-daily-hunt/README.md).

Earlier on 21 November: [21 November extended global hunt and exact ARTEX backdoor evidence](reports/2026/2026-11-21-daily-hunt/README.md) adds 559 memberships: 82 own artifact derivations and 477 external memberships, representing 500 new type/value pairs. We acquired the exact trojanized ARTEX binary and independently verified its native backdoor path. Nine npm archives and ten campaign scripts yield separate own findings; the map adds 62 role-qualified addresses across evidence classes. All 25 private Censys leads and 35 unresolved relationships remain separate. [Expanded sources and collection methods](docs/research-source-directory.md).

Earlier on 19 November: [19 November exact public beacon recovery and source hunt](reports/2026/2026-11-19-payload-hunt/README.md) adds 125 memberships: 19 own derivations and 106 external memberships. Two acquired CyberStrikeAI-lineage ELF files yield native-backed configuration, including one new configured IP at score 60; campaign attribution and current operation remain unknown. The map adds five addresses across separate evidence classes. All 25 private Censys leads and 35 canonical relationship questions remain unresolved.

Earlier on 19 November: [19 November deeper native, public-artifact and original-source hunt](reports/2026/2026-11-19-deeper-hunt/README.md) adds 181 memberships: four own observations and 177 external memberships. The map adds 117 addresses across historical context, software leads and shared services. All 25 private Censys leads and 35 canonical relationship questions remain unresolved. No new exact requested campaign-malware bytes or independently verified malicious C2 IP was obtained.

Earlier on 19 November: [19 November Censys cross-check and artifact identities](reports/2026/2026-11-19-censys-crosscheck/README.md) adds 24 memberships: ten own software/source observations and 14 external memberships, including seven new map IPs. No new independently verified malicious C2 IP was found. Of 100 private ARTEX title leads, 75 already have public-list support and 25 stay private without an admissible public bridge. The 35 unresolved relationships remain separate.

Earlier on 19 November: [19 November source and exact-artifact review](reports/2026/2026-11-19-daily-hunt/README.md) adds 228 memberships and 212 distinct values across separate evidence classes. It includes three role-qualified historical/exposure IPs and exact supporting-component/controller-reference analysis. The 184 published operator hashes and nine favicon hashes remain software references. Censys's public labels were documented earlier in November; this pass adds published query references and historical evidence. All 35 unresolved relationships remain separate.

Earlier on 16 November: [an exact publisher-displayed CyberStrikeAI support-script representation](research/analyst-derived/2026-11-16-cyberstrikeai-publisher-script/README.md) corroborates four existing values after matching all three publisher hashes. The [focused deeper pass](reports/2026/2026-11-16-deeper-artifact-hunt/README.md) adds 12 values through 15 external memberships, including three historical web attack-source IPs without ARTEX/CyberStrikeAI attribution. All 35 unresolved relationships remain separate. No new beacon/controller binary or independently verified malicious C2 IP was acquired.

Earlier on 16 November: [two new exact public artifacts](research/analyst-derived/2026-11-16-exact-public-artifacts/README.md), a NIK C2 implant and modified extension.js, yield 19 independently derived memberships: 13 new values and six corroborations. [16 November review](reports/2026/2026-11-16-daily-hunt/README.md) adds 40 distinct values overall, with zero new IP values; 35 unresolved questions remain separate. [Global Edition source references](research/software-fingerprints/2026-11-16-artex-global-source/README.md) and four pinned CyberStrikeAI/HexStrike strings are qualified software research. No new exact ARTEX/CyberStrikeAI campaign sample or independently verified malicious C2 IP was obtained.

Earlier on 15 November: [native Linux routes](research/analyst-derived/2026-11-15-linux-native-routes/README.md) and [Windows persistence corroborations](research/analyst-derived/2026-11-15-cyberstrikeai-windows-native/README.md): two new static URL prefixes, two existing-value corroborations and one separate experimental lineage rule. [Exact-artifact and identity review](reports/2026/2026-11-15-exact-artifact-review/README.md) resolves four hash identities; 35 questions remain separate. No new sample bytes or malicious C2 IPs were obtained.

Earlier on 15 November: [four CyberStrikeAI public-analysis URL observations](research/analyst-derived/2026-11-15-cyberstrikeai-provider-artifacts/README.md), selected from exact provider JSON with score 20. These are separate from local sample-byte/native findings; two additional provider crosshashes remain externally sourced. [Deeper review](reports/2026/2026-11-15-deeper-hunt/README.md): one of 40 unresolved identities supported, 39 remain separate.

Earlier on 15 November: [two historical CyberStrikeAI-lineage Linux payloads](research/analyst-derived/2026-11-15-historical-cyberstrikeai/historical-payload-analysis.md) yield seven independently derived values: four crosshashes, one configured endpoint and two URL paths. Exact native evidence is separate from campaign attribution.

Also on 15 November: [Windows CyberStrikeAI-lineage artifact evidence](research/analyst-derived/2026-11-15-cyberstrikeai-windows/cyberstrikeai-peak-review.md): three locally computed hashes for one sample and seven existing configuration observables corroborated in native code. No new IP or verified malicious-campaign IOC.

Also on 15 November: [a second complete VoidLink variant](research/analyst-derived/2026-11-15-voidlink/README.md), with native default-port evidence and exact hash identities.

Earlier on 13 November: [VoidLink sample defaults and native evidence](research/analyst-derived/2026-11-13-voidlink/README.md), separately scoped from the historical 342-record collection.

The original collection contains **342 derived or verified records**, including byte/native-backed configuration from an acquired CyberStrikeAI-lineage beacon and ten additional conditional host/protocol patterns. Later artifact supplements are linked separately above. These records include software/reference fingerprints; they are not all confirmed malicious IOCs, and no global novelty is claimed.

- [Our derived observations](research/analyst-derived/all-derived-observables.csv)
- [Acquired beacon analysis and evidence](research/analyst-derived/2026-11-10-cyberstrikeai-elf/README.md)
- [Detection rules](detections/README.md): 13 YARA candidates and one explicitly experimental Sigma rule

The sample's exact operator, named campaign, India targeting and current live C2 remain unknown. Static capability does not prove execution on a victim.

Additional independently verified India-campaign observations are in [our separate static analysis](india/additional-ai-campaigns/2026-11-10-independent-static-analysis/README.md) and [own-observation CSV](india/additional-ai-campaigns/analyst-derived.csv): **5 records**, with vendor-reported campaign context and our byte/method evidence kept distinct.

The [independent enrichment supplement](independent-enrichment/README.md) adds **16 separately scoped records** from public sandbox, certificate and historical scan artifacts: six derived facts, two TLS fingerprints, two unverified sibling domains and six shared-CDN contexts. It corroborates 80 check-in attempts to an existing configured IP; it does not add a verified India-specific C2. [Own observations CSV](independent-enrichment/observations.csv).

We also performed [two first-party endpoint observations](research/first-party/README.md): one root GET per existing seed, with DNS/TLS/HTTP evidence. HTTP 521 and 404 are point-in-time responses, not functioning-C2 proof. These measurements remain separate from provider data and the incident lists. [How our collection works](docs/our-enrichment-workflow.md) · [Hunt's public methods and supported private exports](docs/hunt-and-independent-methods.md).

[ARTEX reachability and fork qualifications](tools/artex-source-review.md) refine our static enrichment markers and a historical authentication realm; source presence is separate from observed traffic.

## Sourced IOCs

On 21 November, the follow-up added 17 source records from the AWS Cairn investigation and two Symantec reports. The two AWS addresses have unspecified network roles. [Public-source follow-up](reports/2026/2026-11-21-followup/README.md).

The original main-record cohorts contain **18 ARTEX-associated** and **9 CyberStrikeAI-associated** records. Later case-qualified source additions are retained in the incident exports and dated reports. The CyberStrikeAI export also includes eight externally reported crosshash identities for four known samples. All three formerly algorithm-unverified CyberStrikeAI/script hashes now have explicit publisher digest bridges. The supporting PowerShell script and its crosshashes remain in supporting tools; the [current untyped-hash export](frameworks/CyberStrikeAI/unverified-file-hash-leads.csv) is empty; all nine historical source values remain in the dated source report and canonical catalog. The [15 November review](reports/2026/2026-11-15-peak-review/README.md) preserves the literal values and publisher roles while narrowing these classifications. Every record retains role, source, dates, confidence scope and verification status. Supporting tools, software fingerprints, passive sightings and unresolved claims remain separate.

- [ARTEX incident indicators](frameworks/ARTEX/README.md)
- [CyberStrikeAI incident indicators](frameworks/CyberStrikeAI/README.md)
- [Research appendices](research/README.md)
- [Compact research catalog](data/catalog.csv) and [master union](data/ALL-FOUND-master.csv): 17,470 distinct type/value records across evidence classes, not a count of malicious systems

## India-related evidence

“Targeting India” refers to the victims or campaign target selection, regardless of infrastructure hosting country. The [dedicated C2 infrastructure view](india/C2-INFRASTRUCTURE.md) contains **18 source-reported C2 records**, with [delivery infrastructure](india/delivery-infrastructure-targeting-india.csv) and [backup configuration resources](india/c2-configuration-resources-targeting-india.csv) kept separate. Campaign-level targeting evidence is sufficient for these scoped associations; a named individual victim is not required for each endpoint.

CERT-In confirms CRAFTY FALCON targeting Indian BFSI organizations and names ARTEX/CyberStrikeAI among the tools, but keeps the detailed IOC set restricted. **No publicly verified exact ARTEX/CyberStrikeAI IOC specific to the Indian campaign was established in this collection.** We do not substitute Korea/FortiGate addresses or generic software sightings for that set.

- [India assessment and primary sources](india/README.md)
- [Nine multi-country context observables](india/campaign-scope-observables.csv): the operator's target prompts included India; this does not prove an Indian compromise
- [Eight India-focused behavioral hunt hypotheses](india/behavioral-hunts.csv): guidance, not static IOCs or validated production rules

The separate [India AI campaign supplement](india/additional-ai-campaigns/README.md) adds **171 externally sourced IOC records** from APT36 vibeware, Sheet Attack and Gopher Strike, plus **5 independently verified/derived observations**. These campaigns have primary-source India targeting evidence and vendor-assessed AI involvement; no ARTEX/CyberStrikeAI link is established. [Sourced IOCs](india/additional-ai-campaigns/sourced-iocs.csv), [our observations](india/additional-ai-campaigns/analyst-derived.csv), [report artifacts](india/additional-ai-campaigns/report-artifacts.csv), and [supporting context](india/additional-ai-campaigns/supporting-context.csv) remain separate.

## Browse dated reports

### 2026-11-24

- [Public-source and artifact hunt](reports/2026/2026-11-24-daily-hunt/README.md) adds 16 records, with Wiz incident roles and three independent asset identities.

### 2026-11-22

- [Submitted evidence reconciliation](reports/2026/2026-11-22-grok-review/README.md) adds 35 records, independently verifies eight software fingerprints, and corrects one master attribution. The selected IP count is unchanged.
- [Global source and public artifact hunt](reports/2026/2026-11-22-daily-hunt/README.md) adds 30 records and 11 historical map addresses, with 8 independently verified software fingerprints.

### 2026-11-21

- [External review reconciliation](reports/2026/2026-11-21-peer-review/README.md) adds 19 source records, including three Sapper software identifiers, and dates two existing map entries.
- [Public-source follow-up](reports/2026/2026-11-21-followup/README.md) adds 17 source records and 6 IPs to the inventory.
- [Extended global hunt and exact ARTEX backdoor evidence](reports/2026/2026-11-21-daily-hunt/README.md): 559 memberships, 82 own derivations, 62 new map addresses and 14 newly indexed tools; unresolved findings remain separate.
- [Research sources and collection methods](docs/research-source-directory.md).

### 2026-11-19

- [Exact public beacon recovery and source hunt](reports/2026/2026-11-19-payload-hunt/README.md): two acquired CyberStrikeAI-lineage samples, 19 own derivations, 106 external memberships and five new map addresses; unresolved findings remain separate.
- [Deeper native and original-source hunt](reports/2026/2026-11-19-deeper-hunt/README.md): 181 memberships, four own observations and 117 new map addresses across separate evidence classes; unresolved findings remain separate.
- [Censys cross-check and software artifact identities](reports/2026/2026-11-19-censys-crosscheck/README.md): 24 memberships, 15 new values, seven new map IPs and ten own software/source observations; uncertain leads stay separate.
- [Public labels, new primary reporting and exact artifacts](reports/2026/2026-11-19-daily-hunt/README.md): 228 memberships, 212 new values and three role-qualified IPs; software fingerprints and 35 unresolved relationships remain separate.

### 2026-11-16

- [Deeper artifact and source review](reports/2026/2026-11-16-deeper-artifact-hunt/README.md): four own existing-value corroborations, 15 external memberships, 12 new values and three historical attack-source IPs; all 35 unresolved findings remain separate.
- [Source aggregation and new artifact analysis](reports/2026/2026-11-16-daily-hunt/README.md): 50 memberships, 40 new values, 10 corroborations and two newly acquired exact artifacts; no new IP value. Evidence classes and 35 unresolved questions remain separate.
- [ARTEX Global Edition source review](research/software-fingerprints/2026-11-16-artex-global-source/README.md) and [CTI Academy context](reports/2026/2026-11-16-daily-hunt/cti-academy-review.md).
- [Tool registry](tools/README.md): LuaN1aoAgent added, 43 identities total.

### 2026-11-15

- [Exact artifacts and publisher identities](reports/2026/2026-11-15-exact-artifact-review/README.md): four of 39 identities supported, 35 role/relationship questions remain separate; four own native observations and one detector hypothesis, eight external crosshashes, 32 aggregation memberships and one external ARTEX software fingerprint.

- [Deeper source and public-artifact hunt](reports/2026/2026-11-15-deeper-hunt/README.md): all 40 unresolved findings revisited; one digest identity resolved, 39 remain separate. Four own public-analysis static URL observations and 74 external source memberships, including historical NIK C2/VOLTA/UAT-10147 and JPCERT context.

- [Evidence resolution and new artifact findings](reports/2026/2026-11-15-evidence-resolution/README.md): all 73 findings revisited; 33 narrow evidence claims supported, 40 source/relationship questions unresolved as of that pass. That pass retained seven experimental operational detection hypotheses.
- [Expanded public-source review](reports/2026/2026-11-15-expanded-source-review/README.md): 31 Talos campaign-associated indicators, 293 historical software/context endpoints and seven prototype identities, with sources, dates and scoped confidence.
- [Original-source verification and unresolved findings](reports/2026/2026-11-15-source-review/README.md): historical snapshot covering 12,299 canonical records and 3,740 master-only values; its 73-row unresolved list is preserved as of that pass.
- [PEAK artifact hunt and reliability review](reports/2026/2026-11-15-peak-review/README.md): ten own static observations and three external provider identities, four new hash values, plus role/algorithm qualifications.
- [Daily source and independent artifact review](reports/2026/2026-11-15-daily-review/README.md): 2,681 evidence records, 591 new type/value entries; Talos deployment leads and FBI corroborations remain separate from campaign indicators.
- [New VoidLink variant evidence](research/analyst-derived/2026-11-15-voidlink/README.md): three hash identities for one artifact and known-IP/8080 corroboration.
- [Tool index](tools/README.md): nine additions across the day and five earlier release updates, 42 identities total.

### 2026-11-13

- [Expanded horizon: framework abuse and AI-related malware](reports/2026/2026-11-13-expanded-horizon/README.md): 145 reviewed records across distinct evidence classes; [eight-group malware index](research/ai-related-malware/README.md).

- [Global source review](reports/2026/2026-11-13-global-review/README.md): 86 source records, 81 values new to the master, seven new overview IPs; evidence classes remain separate.
- [Tool index](tools/README.md): ten new identities, 33 total, plus a qualified release update.

### 2026-11-12

- [Global aggregation and independent collection](reports/2026/2026-11-12-global-aggregation/README.md): 47 historical source additions, including 12 IPs; independent collection development runs alongside aggregation.
- [Tool index expansion](tools/README.md): 15 newly indexed candidates, 23 unified identities, and two independent source identification hypotheses.
- [How we collect our own indicators](docs/original-ioc-collection.md).

### 2026-11-11

- [Global AI tooling and campaign research](reports/2026/2026-11-11-global-ai-tooling/README.md): 44 additions, including nine own source fingerprints and ten new IPs; sourced IOCs, service leads and context remain separate.

- [Our analysis — public artifacts and certificate relationships](independent-enrichment/README.md).
- [Our measurements — bounded DNS, TLS and HTTP seed observations](research/first-party/README.md).
- [Fresh India-targeting source review](india/2026-11-11-source-review.md).

### 2026-11-10

- [Our analysis — India campaign sample identity and static behavior](india/additional-ai-campaigns/2026-11-10-independent-static-analysis/README.md).

### 2026-11-09

- [Datadog — ARTEX activity in AWS](reports/2026/2026-11-09-datadog/README.md) — 20 report-associated observables.

### 2026-11-06

- [Microsoft — Storm-3358](reports/2026/2026-11-06-artex-storm-3358/README.md) — 7 report-associated observables.

### 2026-11-05

- [Check Point — operator-side artifacts](reports/2026/2026-11-05-deep-checkpoint/README.md) — 3 report-associated observables.
- [Microsoft — exposed secrets](reports/2026/2026-11-05-artex-exposed-secrets/README.md) — 4 report-associated observables.

### 2026-11-04

- [BadByte — trojanized ARTEX distribution](reports/2026/2026-11-04-artex-trojanized-distribution/README.md) — 12 report-associated observables.
- [Hunt.io — ARTEX infrastructure](reports/2026/2026-11-04-deep-huntio/README.md) — 39 report-associated observables.
- [S-RM — incident-response cases](reports/2026/2026-11-04-deep-srm/README.md) — 3 report-associated observables.
- [Huntback — ARTEX fork research](reports/2026/2026-11-04-huntback/README.md) — 1 report-associated observable.

### 2026-11-02

- [Kaspersky — CyberStrikeAI beacons](reports/2026/2026-11-02-cyberstrikeai-beacon-campaign/README.md) — 24 report-associated observables.

### 2026-10-31

- [Google Threat Intelligence Group — agentic frameworks](reports/2026/2026-10-31-google/README.md) — 1 report-associated observable.

### 2026-10-30

- [Unit42 — ARTEX-derived activity](reports/2026/2026-10-30-unit42-artex-derived-activity/README.md) — 12 report-associated observables.

### 2026-10-29

- [CrowdStrike — VAPOR PANDA](reports/2026/2026-10-29-vapor-panda-artex/README.md) — 11 report-associated observables.

### 2026-10-22

- [Wiz — Storm-0940](reports/2026/2026-10-22-wiz/README.md) — 2 report-associated observables.

### 2026-10-21

- [Microsoft — Storm-0940 and ConnectWise](reports/2026/2026-10-21-storm-0940-connectwise/README.md) — 6 report-associated observables.
- [Zscaler — multi-country operator workspaces](reports/2026/2026-10-21-artex-multi-country-workspaces/README.md) — 9 report-associated observables.

### 2026-10-15

- [AhnLab — ARTEX infrastructure](reports/2026/2026-10-15-deep-ahnlab4/README.md) — 9 report-associated observables.

### 2026-10-07

- [CrowdStrike — Korean financial sector](reports/2026/2026-10-07-artex-korean-finance/README.md) — 12 report-associated observables.

### 2026-10-03

- [PLURA — ARTEX research](reports/2026/2026-10-03-deep-plura/README.md) — 5 report-associated observables.

### 2026-03-05

- [Bitdefender — APT36 vibeware targeting India](india/additional-ai-campaigns/2026-03-05-apt36-vibeware/README.md).

### 2026-03-02

- [Team Cymru — CyberStrikeAI infrastructure](reports/2026/2026-03-02-cyberstrikeai-fortigate-context/README.md) — 1 report-associated observable.

### 2026-02-20

- [AWS — FortiGate campaign context](reports/2026/2026-02-20-aws-fortigate-campaign-context/README.md) — 2 report-associated observables.


### 2026-01-27

- [Zscaler — Sheet Attack targeting Indian government](india/additional-ai-campaigns/2026-01-27-sheet-attack/README.md).

### 2026-01-26

- [Zscaler — Gopher Strike targeting Indian government](india/additional-ai-campaigns/2026-01-26-gopher-strike/README.md).
