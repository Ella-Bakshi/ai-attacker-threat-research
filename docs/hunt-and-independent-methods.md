# Hunt.io methods, supported exports, and an independent research workflow

Official documentation checked on 2026-11-10 UTC (2026-11-11 in India). This note describes public methods and documented interfaces. No account data, proprietary detection rules, private portal APIs or attacker servers were accessed by this research subtask.

## What Hunt collects and how it builds context

Hunt's own collection is active internet measurement, not solely passive threat-feed aggregation. Its current Platform Stats documentation describes open-port discovery, protocol detection on unknown ports, complete HTTP HTML grabs, parsed TLS certificates, SSH public keys and JARM fingerprints. Host histories and pivots join those observations. Reading the resulting index is passive from our research client's perspective, while Hunt's underlying probes are active. [Platform Stats](https://hunt.io/support/platform-stats), [older methodology announcement](https://hunt.io/blog/hunt-platform-statistics).

Hunt describes its C2 feed as a combination of internet scans for protocols and artifacts, repeated attention to historically risky infrastructure, validation and a research team maintaining signatures. These are vendor descriptions, not a published detector specification or independent performance measurement. The feed also includes offensive frameworks and reconnaissance tools; a framework match does not alone prove a malicious operator or Indian target. The current C2 interface exposes family, IP, hostnames, port, country and first/last observations. [C2 feed methodology](https://hunt.io/blog/introducing-C2-feed), [current C2 interface](https://hunt.io/support/c2-infrastructure).

The platform separates several kinds of evidence:

| View | What it contributes | Interpretation |
|---|---|---|
| C2 Infrastructure | Provider-classified service/framework observations and dates | Software/service identification; keep Hunt's classification separate from independently established campaign use. |
| AttackCapture | Captured open-directory files, tags, summaries and searchable source/configuration content | Can provide stronger artifact/context evidence; inspect the actual file and its capture time. |
| IOC Hunter | Source articles and extracted indicator relationships | Follow the primary publisher to verify role, date, attribution and targeting. |
| Signals | Sensor-observed scanning/probing/attack behavior | Behavior context; sensor activity alone does not identify victims or prove a successful intrusion. |
| Search/host history | Certificates, keys, domains, services and chronology | Pivots are hypotheses until supported by specific shared evidence. |

Sources: [AttackCapture](https://hunt.io/support/attackcapture), [IOC Hunter](https://hunt.io/support/ioc-hunter), [Signals](https://hunt.io/support/signals), [Search](https://hunt.io/support/search).

AttackCapture's public guide documents Listing, Attack Reports, Code Search, Explore and Exploit Capture. Reports can be searched for victims/targets, and code search returns matched lines with host/time context. That makes these better routes for investigating India targeting than a host-country filter. Summaries and automatic tags require review against the underlying artifact. The Signals guide itself marks parts of its query syntax "to verify"; do not treat those unfinished examples as guaranteed current syntax.

## Fingerprints and their limits

Useful general techniques include matching exact certificate hashes, certificate fields, SSH host keys, HTTP headers/content hashes, software markers, favicons and TLS configuration fingerprints. They provide different kinds of evidence. A copied certificate is not proof of common ownership; default SSH keys and common TLS stacks can produce broad matches. HTTP/TLS evidence must be tied to the same service, port, hostname/SNI and observation time.

JARM is an open, active technique: it sends ten different TLS ClientHello probes and hashes selected server responses. Its algorithm ignores X.509 certificate data, so a matching certificate and matching JARM are distinct observations. The original implementation is public; there is no need to extract Hunt's private implementation. [Salesforce JARM](https://github.com/salesforce/jarm), [Hunt's public explanation](https://hunt.io/glossary/jarm-fingerprinting).

Hunt's own CameraSwarm investigation demonstrates why matches need context: even a rare JARM match was rejected after the other host's domains, history and captured file references indicated an unrelated system. Its analysis also distinguishes copied certificate bytes from a matching TLS stack. Do not publish unrelated neighboring IPs, an entire ASN or every shared fingerprint match as an IOC. [CameraSwarm analysis](https://hunt.io/blog/operation-cameraswarm-dahua-cameras-compromised).

## Supported private collection and export

Use the account's supported controls and entitlements. Capture the chosen framework filters, time window, sort, counts and export time before downloading; preserve the raw export locally with SHA256. A row count is not a unique-IP or confirmed-malicious-host count. Deduplicate separately by IP, service endpoint, hostname and evidence record.

HuntSQL's current public guide says `ip.current` is one row per IP combining HTTP, TLS, SSH, JARM, JA4, favicon, protocol and scan metadata. The Schema panel lists field types, examples and supported operators; **Download schema** and **Samples** are the documented way to build a valid query. Export from Results. Do not guess a family field or reuse old table names without checking aliases. [HuntSQL guide](https://hunt.io/support/huntsql).

The public API documentation links its own OpenAPI reference at [a.hunt.io/openapi.json](https://a.hunt.io/openapi.json). It documents these interfaces; they were not inferred from private portal traffic:

| Purpose | Documented endpoint | Notes |
|---|---|---|
| Inspect visible tables | `POST /sql/list-tables` | Account-visible tables and discovery metadata. |
| Inspect a table | `POST /sql/schema` | Optional body `schema: "ip.current"`; aliases resolve to the canonical table. |
| Query | `POST /sql` | Requires `sql`; supports page/count/export/histogram/download-request modes. |
| Download query results | `POST /sql/download` | Requires `query`; optional `file_type` is JSON, NDJSON or CSV, plus a documented time-window parameter. |
| C2 feed | `GET /feeds/c2` | Gzip NDJSON with service fields; optional exact-domain exclusion controls. |

Authentication uses a licensed API key, and access/quota is account dependent. The API guide exposes usage, rate and burst limits; no universal trial quota or export cap is established here. An accepted request time-window maximum is not a guarantee of that much retained historical data. Keep keys in a local environment/secret store and out of logs, screenshots, exports and GitHub. [API reference](https://a.hunt.io/), [API keys and usage](https://hunt.io/support/api).

Current Feeds documentation says the C2 feed is generated when downloaded; IOC Hunter covers seven days and refreshes every thirty minutes, while phishing covers thirty days and refreshes hourly. The older C2-launch article described a seven-day window, so record the actual request/export scope instead of assuming that historical wording describes every current feed. [Feeds](https://hunt.io/support/feeds).

Saved SQL, actor and AttackCapture monitors can rerun at a chosen interval. Check account usage before choosing a polling interval, preserve last-success checkpoints and avoid re-downloading unchanged windows. Handle rate limits and entitlement errors normally; do not bypass limits. [Alerts](https://hunt.io/support/alerts).

## Private data and public publication

Hunt's current terms restrict ordinary use to internal security purposes, reserve rights to its service/data, prohibit scraping and proprietary reverse engineering, and permit API access only within a separate licensed scope. They prohibit disclosure or redistribution of Hunt data, including derived products, unless another applicable agreement expressly allows it. A supported export button permits downloading within the service; it does not establish public redistribution rights. Keep portal exports and provider-derived records private here. Do not add provider-export rows, an enriched substitute, screenshots exposing account data, or complete copied API documentation to the public repository. [Terms, sections 1 and 3](https://hunt.io/terms-of-service).

The public research corpus should retain independently acquired primary-report facts, original artifact analysis and explicitly licensed data. Keep a separate private provider-evidence store. Merely replacing a provider column with ASN/geolocation does not change the origin of its observations. If a public primary report independently documents an existing value, cite that report and its limited role instead of laundering an entire commercial export into a public feed.

## Independent collection architecture

The following is an analyst-designed workflow using general public methods, not Hunt's proprietary rules:

1. **Build reproducible local fingerprints.** Pin the official ARTEX/CyberStrikeAI source commit and a local test build. In an isolated lab, capture the default HTTP routes, content, favicon bytes, titles, version markers and TLS behavior. Record the exact hashing/encoding procedure. Use ordinary Next.js/Go pages, copied default assets and legitimate framework installations as negative controls.
2. **Keep discovery passive by default.** Search already-indexed public/authorized sources using our own documented fingerprints. Store the provider, query, service, observation time and retrieval time. Any future active measurements need a separate explicit scope; this workflow does not launch internet scans or contact actor infrastructure.
3. **Verify application identity and service scope.** Require specific evidence beyond a generic title/icon. Compare cached route/body markers and exact asset hashes, keeping certificate/JARM observations tied to the matched port/SNI. Classify a good software match as a deployment lead; it can still be a legitimate security installation.
4. **Analyze acquired artifacts offline.** For authorized sample bytes, save acquisition provenance and cryptographic hashes, then extract configured endpoints, protocol structure, paths and other observables without executing the sample. Distinguish configured C2 from observed traffic. Keep binaries and secret-bearing captures outside the public repository.
5. **Establish campaign and India relevance.** Accept explicit primary campaign victimology naming India, or a target list/prompt with documented campaign context. Connect infrastructure through an exact configured endpoint, malicious-artifact hash or source-reported operational host. A generic actor's wider victimology, hosting country, ASN or co-located framework alone is insufficient. Campaign target intent is enough for a scoped record; successful compromise is a separate claim.
6. **Enrich without changing the verdict.** Add independently licensed ASN/approximate geolocation data and its dataset release/hash. Do not infer an actor's nationality, a victim country or maliciousness from hosting location. Keep software confidence, historical role confidence and campaign/targeting confidence separate.
7. **Publish reviewable evidence classes.** Maintain source-reported incident IOCs, sample-derived configuration, deployment leads, software fingerprints, supporting infrastructure and unresolved findings in separate exports. Every record needs source/capture locator, date basis, analyst contribution, confidence scope and limitations. Preserve duplicates' source memberships while deduplicating type/value totals.
8. **Run offline quality gates.** Check exact source literals, same-service joins, first/last timestamp meanings, source versus enrichment dates, category counts, credential absence and license provenance. Keep disproven pivots in a rejection log. New detections should be promoted only when new supporting evidence resolves the specific uncertainty.

For the present India hunt, the Zscaler operation establishes India among operator target prompts, while its published network roles remain work server, jump server and proxy. That is useful attack-infrastructure context, but does not by itself identify a beacon listener. The public primary-source findings and the private Hunt enrichment therefore remain separate.
