# AI Attacker Threat Research — 15 November 2026 PEAK review

This supplement adds **13 evidence records and four new exact hash values**, with **zero new IP addresses and zero newly verified malicious-campaign IOCs**. Seven records add independent evidence to existing observables; two add external-provider corroboration. A new record, a new value and a new malicious IOC are different counts.

| Evidence origin | Records | New values | What changed |
|---|---:|---:|---|
| Our offline Windows artifact analysis | 10 | 3 | Three locally computed sample hashes; seven corroborations of existing static configuration or artifact observations |
| External ARTEX sample metadata | 3 | 1 | One new SHA3-384 value; MD5/SHA1 corroborations for the same known file |

[Canonical JSON](records.json) · [CSV](indicators.csv) · [Our Windows analysis](../../../research/analyst-derived/2026-11-15-cyberstrikeai-windows/cyberstrikeai-peak-review.md). The canonical index now contains 12,299 records; the master contains 15,944 distinct type/value entries. The selected IP overview remains 6,320 addresses.

## Hypotheses, tests and results

Using the [PEAK documentation structure](https://dispatch.thorcollective.com/p/the-peak-threat-hunting-template), this review made the required proof, competing explanations and negative controls explicit before accepting findings. Aggregation continued alongside the artifact work.

**CyberStrikeAI:** could a public Windows sample with conflicting provider labels establish a more specific lineage and configured endpoint? We acquired one exact archive member, verified its identity and inspected it offline. Generated Go metadata, application function names and selective native request arguments were compared with the [official beacon template at the recorded base commit](https://github.com/AIPentest/CyberStrikeAI/blob/d2084a948195d60fe7d66f8a8f1f5d901bb5dd3f/internal/c2/payload_templates/beacon.go.tmpl). Four local reference artifacts tested the proposed identifying conjunction. Single generic headers and Go/HTTP markers were insufficient.

The resulting file identity and static configuration are independently derived. The [provider entry](https://bazaar.abuse.ch/sample/1b95c2783b667ad5ffbd5b66afc367a92c314f507ba43789ec0bcda5a623a877/) also carries an AdaptixC2 classification, which remains documented. `vcs.modified=true` prevents an exact generating-revision claim. The recovered configuration does not establish a successful connection, malicious operation, named campaign or current endpoint ownership. This was selective native inspection, not complete decompilation of every function.

**ARTEX:** could the exact reported trojanized container or executable yield additional configuration? The [BadByte report, published 4 November and updated 5 November](https://badbyte.io/artex-backdoor-docker-image/), identifies removed images and a binary-only modification. Supported public acquisition routes did not yield the executable. We verified an existing source-pinned dependency reference, but acquired no ARTEX malware bytes and completed no new native decompilation. The publisher reports no added callback endpoint; that claim could not be independently tested.

The [exact YARAify file entry](https://yaraify.abuse.ch/sample/d5070f52262effe216b840711343bff8f2787f39208d887d8dfd9c673f8d1573/), reviewed on 15 November, supplies the three ARTEX hash mappings. Its 14 November sample-index/static-scan timestamps are not attack dates. These are externally reported identities for one file, not our byte extraction or three separate samples.

## Reliability changes

The review baseline contained 12,286 canonical records. All received structural checks; this does **not** mean every underlying source was freshly verified. All 7,274 Censys/Shodan records matched retained historical responses at their available scope; one remains host-only with its service port unconfirmed. Retained-response agreement does not authenticate acquisition independently or establish current operation.

A separate review covered all 442 baseline incident/source records across 30 primary URLs: 418 exact values matched fresh source content, four followed explicit publisher brace/port-list expansions, and 20 retained fresh-access gaps. All 27 original ARTEX/CyberStrikeAI main values were found and their reported roles reviewed.

The resulting corrections distinguish 13 campaign-context network records at score55 from explicit historical C2 at score70; qualify four source hash algorithms, including moving three unresolved values out of the main IOC category; preserve the unresolved `178.15.54.129`/`178.16.54.129` source discrepancy; and fill missing country-relevance metadata in 214 older records without adding targeting claims. See [indicator reliability and appropriate use](../../../docs/indicator-reliability.md).

No samples were executed, candidate services contacted, new scans submitted or paid-provider calls made. Native artifacts, raw captures and internal review ledgers remain outside the public dataset. Existing historical observations remain historical; this review grants no blanket approval to block the complete catalog.
