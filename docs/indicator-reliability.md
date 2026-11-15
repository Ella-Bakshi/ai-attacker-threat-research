# Indicator reliability and appropriate use

An observable becomes useful evidence through its source, role, time and context. An exact file hash, an indexed console and an incident-reported C2 address answer different questions. This repository preserves those differences; the complete catalog and map are research inventories, not a single malicious-infrastructure block list.

## Select records by evidence class

| Class | Supported interpretation | Important limit |
|---|---|---|
| Source-reported incident/campaign IOC | A publisher associates the value with the stated historical role | Preserve the precise role, dates, source corrections and attribution limits |
| Our artifact extraction | We independently reproduced an identity or found configuration in exact artifact bytes | Configured intent does not prove execution, a successful connection, victims or current ownership |
| Software fingerprint or detection hypothesis | A pattern may identify software or a code lineage | Legitimate installations, common components and copied assets need controls |
| Passive deployment lead | A provider historically indexed a service or marker | Installation is not proof of hostile operation or present liveness |
| Supporting/shared service | The source describes supporting infrastructure or context | Shared hosting, API resellers and legitimate services are not dedicated C2 by association |
| Unverified/conflicting finding | A specific question remains unresolved | Keep it separate until the missing proof is obtained |

**Our finding** means a stated analyst derivation with an exact artifact/source locator. It does not imply first-party sensor collection or global first discovery. Provider metadata that we curate remains external evidence. Multiple hashes of one file are multiple identities, not multiple samples.

## Confidence has a scope

High confidence in an exact hash or software match does not establish maliciousness. The map uses ordinal evidence-strength labels, not probabilities: 0 for unreviewed/shared context; 10 for an unresolved historical lead; 20 for a passive deployment/fingerprint; 55 for reported campaign context; 60 for exact static configuration independently examined; and 70 for a primary-source-reported historical C2 role. Hosting enrichment never increases this score. The record's written basis and conflicting evidence take precedence over a label alone.

IP, service port, hostname/SNI, sample variant and observation time must remain connected to their own evidence. A certificate at another port, neighboring address, ASN or hosting country does not establish that relationship. Enrichment location describes hosting, not victim location or country targeting. Provider indexing, sample submission, certificate validity, acquisition and victim activity are separate clocks; unknown dates remain blank.

## Review scope as of 15 November 2026

The baseline review structurally checked all 12,286 canonical records. It matched 7,274 Censys/Shodan records to retained local response evidence, including one host-only match whose service port remains unconfirmed. These checks do not independently authenticate original provider acquisition or recheck every software-identification decision.

Of 442 baseline incident/source records, 418 exact values matched fresh primary content, four were supported by explicit enumerated expansions, and 20 could not be freshly reviewed because the underlying sources returned access errors. All 27 original ARTEX/CyberStrikeAI main values received a source-role review. **The full catalog has not received fresh underlying-source verification for every record.**

The review also corrected role-based scoring for 13 network records and missing country-relevance metadata in 214 older records. Four source hash literals remain algorithm-unverified: three reported beacon hashes are separated as unresolved findings, while one supporting-script hash retains its supporting role with an unverified algorithm type. Separately, one reported beacon MD5 relationship is supported by a fresh [public Triage identity bridge](https://tria.ge/261027-qmb8eaes6q). Matching a 32-character source literal alone does not independently verify MD5 over the artifact bytes.

The [6 November Microsoft report](https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-sector/) contains `178.15.54.129` in a query and `178.16.54.129` in its table. The [13 November FBI advisory](https://www.ic3.gov/CSA/2026/261113.pdf) repeats the table variant. That compilation supplies neither independent telemetry nor an explicit correction resolving the octet discrepancy. The conflict remains visible; repetition is not independent corroboration.

## Operational use

Use source-reported malicious indicators only with their historical role, freshness and local context. Review shared/reassigned IPs and mutable image tags before enforcement. File blocking requires the exact algorithm and artifact identity. Software fingerprints and passive leads support investigation and detection development; they require separate evidence before being treated as malicious infrastructure. Generic pattern matches have no implied production false-positive estimate.

Read the original source and limitations before taking action. A later review can corroborate, narrow or reject an earlier interpretation without changing the literal value. Dated reports preserve what was known at the time; counts and map refreshes do not establish that historical services remain active.
