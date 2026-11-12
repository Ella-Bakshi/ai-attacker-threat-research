# Collecting our own indicators

Reviewed 12 November 2026. An original finding needs its own evidence chain. A larger enriched IP list is not evidence of more malicious infrastructure.

| Work performed | Provenance | Supported claim |
|---|---|---|
| Read a publisher's IOC table | External report, analyst curation | The publisher reports the stated role/date |
| Extract configuration from exact sample bytes | External acquisition, our independent derivation | This sample configures or implements the stated observable |
| Parse an existing sandbox capture | Provider telemetry, our independent analysis | The recorded flow or attempt occurred within that task's limits |
| Capture an interaction on our owned sensor | First-party collection | That event reached our sensor at that time |
| Hash an official tool's logo or code | Our reference fingerprint | Software/byte identity, with malicious use unestablished |
| Join ASN, GeoIP, certificates or passive DNS | Enrichment or relationship hypothesis | Metadata or a relationship requiring further evidence |

## Current priority

Use newly acquired, source-backed samples or recorded artifacts. Retain acquisition URL/time, whole-file SHA256, exact byte/code/event locator, extraction/decoding procedure, role, confidence scope, and whether the value is new or corroborating. Exclude documentation, defaults, library traffic and unrelated embedded URLs before admitting a configured endpoint. Never replace a historical activity time with today's acquisition or enrichment time.

Our existing CyberStrikeAI-lineage ELF has already yielded its configured endpoints and main application analysis. Rehashing it does not create a new IOC. New work should target additional source-backed artifacts or a genuinely unresolved question. [CAPE](https://github.com/kevoreilly/CAPEv2#config-extraction) documents configuration extraction; its dynamic execution features are outside the present offline workflow. [MalwareBazaar](https://bazaar.abuse.ch/api/) documents authentication and public batch acquisition routes.

## First-party collection design

A future explicitly owned, isolated sensor can retain inbound session events, attempted payload URLs and passively received artifacts. [Cowrie](https://docs.cowrie.org/en/stable/OUTPUT.html) provides structured SSH/Telnet events; [OpenCanary](https://github.com/thinkst/opencanary) supports internal deception. Neither has been deployed for this project. No first-party attack telemetry is claimed.

Keep the sensor separate from production, disable proxy backends, restrict egress, retain UTC/session linkage privately, and remove credentials/personal data before publication. An inbound scanner IP is not automatically a payload server or C2. Attack speed, a user-agent string or a honeypot hit alone cannot establish AI-tool use. Artifact/configuration or incident evidence must supply that relationship.

The daily hunt continues full primary-source aggregation alongside an additional independent-artifact lane. An unavailable sample does not block source review or publication of verified sourced indicators. Source-reported indicators, our derivations, reference fingerprints and deployment leads remain separate. Unsuccessful acquisition and negative analysis are valid outcomes; no record is promoted merely to meet a quota. [ThreatFox](https://threatfox.abuse.ch/faq) describes indicator vetting and historical freshness limits.
