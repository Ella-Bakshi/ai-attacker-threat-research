# CyberStrikeAI: public provider artifacts, 15 November 2026

This pass resolved one previously untyped file indicator using explicit independent provider metadata. It also identified two new file-identity values and independently selected four standalone static URL literals from public provider JSON. No malware bytes were acquired, no native operands were examined, and no new malicious C2 IP was established.

## Identity result

The [OTX analysis for 09e1da2afa1216ecc55648ec8e122d2a](https://otx.alienvault.com/api/v1/indicators/file/09e1da2afa1216ecc55648ec8e122d2a/analysis) explicitly labels MD5, SHA1 and SHA256 for one 6111380-byte ELF. The [SHA1 lookup](https://otx.alienvault.com/api/v1/indicators/file/520c64c1016199f0239882791e4b344a9b2437d7/analysis) returned an identical response. This bridges the file to the exact Linux-beacon literal in [Securelist's report](https://securelist.com/tr/cyberstrikeai-attacks/121715/). It establishes provider-supported cryptographic identity; we did not recalculate the malware digest locally.

Two identity additions are external provider aggregation: SHA1 `520c64c1016199f0239882791e4b344a9b2437d7` and SHA256 `5d1b591dde5009258da930fa362509f752557e3f215759d53e7d18052b0ef844`.

## Our public-artifact selections

Our work independently selected four complete, standalone URL strings from the public JSON arrays for the two exactly identified publisher-linked Linux samples. These are literal-only observations, with ordinal score 20 and no automatic blocking recommendation. Their historical role/lineage interpretation has Medium confidence. Static strings can be unused; request construction and successful exchange are not established.

| Sample SHA256 prefix | Standalone URL literal | Original JSON locator |
|---|---|---|
| `1c6498f0` | `https://media[.]fastcdn[.]bar:2083/assets/js/app.min.js` | `/analysis/plugins/strings/results/7232` |
| `1c6498f0` | `https://media[.]fastcdn[.]bar:2083/assets/js/main.min.js` | `/analysis/plugins/strings/results/7249` |
| `5d1b591d` | `http://104[.]234[.]26[.]163:8443/result` | `/analysis/plugins/strings/results/6695` |
| `5d1b591d` | `http://104[.]234[.]26[.]163:8443/check_in` | `/analysis/plugins/strings/results/6786` |

[Compact source evidence](provider-identity-evidence.json) retains exact response identities, retrieval UTC, sample bridges and JSON locators. It excludes raw provider bodies, API tokens, sample binaries and raw request captures. [Own observations](observations.json) carry individual sources, confidence scope and limitations.

## PEAK review

**Hypothesis:** independent provider analyses can resolve missing digest identities and expose exact additional sample strings without contacting infrastructure.

**Proof:** actual analysis identity fields, equivalent MD5/SHA1 lookups, exact publisher hash membership and standalone static-string array entries. Two hashes and four URLs were absent from 12,637 canonical records and 16,176 master values.

**Competing explanations and controls:** top-level provider query typing can be inferred from the supplied digest length. A nonindicative 32-hex control also received MD5 typing without a base record. Therefore empty analysis/community pulse typing did not resolve the other three 32-hex indicators or the LAMEHUG 64-hex indicator. Generic Go/library strings and concatenated metaextract URL fragments were excluded. Exact sample identity supports the narrow source relationship; it does not prove that a URL was used as a callback.

**Result:** one source-scope resolution, six remaining uncertain records, two provider file identities and four own public-JSON selections. Zero new first-party observations, acquired malware samples, native configuration findings or proven new malicious C2s.

## Coverage limits

The two CT sibling domains remain relationship leads. Exact-domain URLscan searches returned no public results within the displayed 30-day window; certificate issuance and empty search results do not establish deployment or absence. Four additional daily archive directory windows were fully examined; two failed the bounded parser, and exact sample bytes were not found. Prior retained directories were compared only against the newly bridged identities. Current liveness, victims, operators and exact generating revisions remain unknown. No sample execution, domain resolution, candidate contact, scan, paid query or sample submission occurred.
