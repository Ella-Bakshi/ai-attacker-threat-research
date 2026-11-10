# AI Attacker Threat Research

Research into the abuse of AI offensive frameworks, with sources, dates, scoped confidence and reproducible static evidence. Snapshot: **10 November 2026**.

## Our findings

We derived or verified **333 records**, including byte/native-backed configuration from an acquired CyberStrikeAI-lineage beacon and ten additional conditional host/protocol patterns. These records include software/reference fingerprints; they are not all confirmed malicious IOCs, and no global novelty is claimed.

- [Our derived observations](research/analyst-derived/all-derived-observables.csv)
- [Acquired beacon analysis and evidence](research/analyst-derived/2026-11-10-cyberstrikeai-elf/README.md)
- [Detection rules](detections/README.md): 12 compiled YARA rules and one explicitly experimental Sigma rule

The sample's exact operator, named campaign, India targeting and current live C2 remain unknown. Static capability does not prove execution on a victim.

## Sourced IOCs

The main incident lists contain **18 ARTEX-associated** and **9 CyberStrikeAI-associated** indicators reported by external sources. Every record retains role, source, dates, confidence scope and verification status. Supporting tools, software fingerprints, passive sightings and unresolved claims remain separate.

- [ARTEX incident indicators](frameworks/ARTEX/README.md)
- [CyberStrikeAI incident indicators](frameworks/CyberStrikeAI/README.md)
- [Research appendices](research/README.md)
- [Compact research catalog](data/catalog.csv) and [master union](data/ALL-FOUND-master.csv): 14,809 distinct type/value records across evidence classes, not a count of malicious systems

## India-related evidence

CERT-In confirms CRAFTY FALCON targeting Indian BFSI organizations and names ARTEX/CyberStrikeAI among the tools, but keeps the detailed IOC set restricted. **No publicly verified exact India-specific IOC was established in this collection.** We do not substitute Korea/FortiGate addresses or generic software sightings for that set.

- [India assessment and primary sources](india/README.md)
- [Nine multi-country context observables](india/campaign-scope-observables.csv): the operator's target prompts included India; this does not prove an Indian compromise
- [Eight India-focused behavioral hunt hypotheses](india/behavioral-hunts.csv): guidance, not static IOCs or validated production rules

## Browse dated reports

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

### 2026-03-02

- [Team Cymru — CyberStrikeAI infrastructure](reports/2026/2026-03-02-cyberstrikeai-fortigate-context/README.md) — 1 report-associated observable.

### 2026-02-20

- [AWS — FortiGate campaign context](reports/2026/2026-02-20-aws-fortigate-campaign-context/README.md) — 2 report-associated observables.

