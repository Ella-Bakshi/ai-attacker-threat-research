# Historical CyberStrikeAI-template-lineage payloads — 15 November 2026

Two exact historical Linux payloads from the [URLhaus 3944164 delivery table](https://urlhaus.abuse.ch/url/3944164/) were independently acquired from a public archive and examined offline. Both contain native HTTP POST arguments targeting **23.254.195.48:18443**, a different port from the8099 delivery service and the previously examined8443 configuration.

| Artifact SHA256 | Size | Native evidence |
|---|---:|---|
| `7832997e951cdd9c169d25e72141e24d63f342b19f6ad2e1523f5f21a486c9c7` |6,115,512 bytes| Check-in 35-byte URL at offset 3,475,602; result 33-byte URL at3,471,158 |
| `f825c06b278627ab9753ccdeffd510a32f6bc706845931906597d1f8d978913d` |6,168,868 bytes| Check-in 35-byte URL at offset 3,502,635; result 33-byte URL at3,498,191 |

Acquisition verified full SHA256, ZIP CRC32 and size for each exact member. Native operands, lengths, POST methods and resolved calls to `net/http.NewRequestWithContext` corroborate the intended URLs. Forty-two of 43 base function names match the [pinned official beacon template](https://github.com/AIPentest/CyberStrikeAI/blob/b43bdb991c3bee4f433cd1a0a370a90c4e24241e/internal/c2/payload_templates/beacon.go.tmpl), alongside specific protocol/function markers. Both artifacts use generic `beacon(devel)` module metadata and lack an official revision. The conclusion is **CyberStrikeAI beacon-template code lineage**, with exact generating revision, modifications, operator and campaign unknown. Recovered function names/boundaries and selective native checks do not mean every function was decompiled.

URLhaus directly lists both 7 October payloads and the independently examined 6 November `cbf1045...` payload at the same delivery URL. URL addition 2026-10-07T07:15:25Z, payload observations, local acquisition and intended controller configuration have different meanings. No present liveness, successful registration, shared operator or victim attribution follows from this relationship. The provider's displayed online status was not independently adopted.

A five-marker conjunction was present in these two artifacts and absent as a conjunction in four finite local controls: ARTEX, a local official-source CyberStrikeAI controller, a third-party egress component and the benign Go compiler. This is not a measured production false-positive rate. The existing generated-path ELF signature misses both variants because they lack that path; broad beacon coverage must not be claimed.

The JSON evidence keeps source seeds, acquisition identity, native locators, code-lineage inference and negative controls separate. The supplemental own observations contain four newly computed crosshashes and three newly extracted endpoint/URL values, with score 60 for exact static evidence. Scores are ordinal evidence strength, not probabilities of maliciousness. No new IP address, globally first discovery or named malicious-campaign IOC is claimed. No sample execution, controller/DNS/TLS probe, scanning, submission, paid service or private provider export was used. Keys, raw requests, binaries and decompiler projects are excluded.
