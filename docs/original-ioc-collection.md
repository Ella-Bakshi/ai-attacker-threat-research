# Collecting our own indicators

Reviewed 15 November 2026. An original finding needs its own evidence chain. A larger enriched IP list is not evidence of more malicious infrastructure.

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

The [15 November Windows artifact review](../research/analyst-derived/2026-11-15-cyberstrikeai-windows/cyberstrikeai-peak-review.md) demonstrates this workflow on another sample: three locally computed hash identities and native request arguments corroborate seven existing observables. The evidence establishes static configuration and code lineage; it adds no verified malicious-campaign IOC or first-party attack telemetry.

The [historical Linux payload supplement](../research/analyst-derived/2026-11-15-historical-cyberstrikeai/historical-payload-analysis.md) adds four computed crosshashes and three native configuration values from two additional exact artifacts. These are independent derivations from public material, with no first-party sensor telemetry or named campaign attribution.

## First-party collection design

A future explicitly owned, isolated sensor can retain inbound session events, attempted payload URLs and passively received artifacts. [Cowrie](https://docs.cowrie.org/en/stable/OUTPUT.html) provides structured SSH/Telnet events; [OpenCanary](https://github.com/thinkst/opencanary) supports internal deception. Neither has been deployed for this project. No first-party attack telemetry is claimed.

Keep the sensor separate from production, disable proxy backends, restrict egress, retain UTC/session linkage privately, and remove credentials/personal data before publication. An inbound scanner IP is not automatically a payload server or C2. Attack speed, a user-agent string or a honeypot hit alone cannot establish AI-tool use. Artifact/configuration or incident evidence must supply that relationship.

The daily hunt continues full primary-source aggregation alongside an additional independent-artifact lane. An unavailable sample does not block source review or publication of verified sourced indicators. Source-reported indicators, our derivations, reference fingerprints and deployment leads remain separate. Unsuccessful acquisition and negative analysis are valid outcomes; no record is promoted merely to meet a quota. [ThreatFox](https://threatfox.abuse.ch/faq) describes indicator vetting and historical freshness limits.

## Structured hunt review

The [PEAK documentation approach](https://dispatch.thorcollective.com/p/the-peak-threat-hunting-template) and [agentic hunting discussion](https://dispatch.thorcollective.com/p/the-agentic-threat-hunter) inform our private hunt ledger. Each question records its hypothesis, evidence window, source/artifact scope, competing explanations, negative controls, disposition and next step. Parallel source and artifact work converges in a separate evidence review before admission. These are methodology references, not IOC sources or claims that an owned sensor exists. Unresolved results remain private; a corroboration does not become a new unique value.

## Lessons from the expanded public-source review

[Harness's 13 November API-traffic study](https://www.harness.io/blog/an-artex-threat-hunt-across-customer-api-traffic) separates sender-supplied tool names from verified software identity and request outcomes. Its examples withhold source addresses, so its search inputs cannot resolve our disputed-address records. For future authorized telemetry, correlate an endpoint, identity, response and session before assigning an incident role. Common clients, high volume and a shared IP are insufficient alone.

[Houdin's historical CyberStrikeAI census](https://houdin.io/blog/mapping-200-undetected-chinese-ai-attack-platforms) illustrates complementary certificate and page-content evidence. These remain software sightings. Its other-C2 feed annotations are separate services/claims, and a certificate's issue date does not date an installation or attack. Our current collection uses existing public evidence without repeating the publisher's active scans.

[Splunk's PEAK deliverables guidance](https://www.splunk.com/en_us/blog/security/key-threat-hunting-deliverables-with-peak.html) treats evidence gaps, revised detections and future hunt questions as useful results alongside incidents. We preserve negative results and concrete next steps. A finite signature match can verify a reference-byte observation while production detection efficacy remains experimental.

For additional samples, the decision sequence is: verify the source-to-artifact hash bridge; inspect exact bytes offline; prove that a URL is a configured request argument; compare specific code lineage with finite controls; review independently; deduplicate against every indexed record and the master. Report new values, corroborations, corrections and unresolved relationships separately. Aggregation continues in parallel and keeps its external origin.
