# Unit42 Artex Derived Activity

Report date: 2026-10-30. Collection reviewed: 2026-11-10. Source: [deep_unit42](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/5ed83ef5ab608b87fac4f95c4c1d50798c6e78e9/2026-10-30-activity-using-ARTEX-agentic-AI.txt). This folder contains 12 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

The publisher recommends monitoring/correlation, not automatic blocking. Attribution is ARTEX or a derived framework, without confirmed actor ownership.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `103[.]100[.]158[.]103` | ipv4 | Monitor-only scanning/OAuth source correlated by UAs/client IDs | Medium | campaign-context |
| `152[.]233[.]51[.]12` | ipv4 | Monitor-only source of probing and unauthenticated API writes | Medium | campaign-context |
| `173[.]254[.]220[.]78` | ipv4 | Reconnaissance source with a co-located Sub2API gateway | Medium | campaign-context |
| `31[.]40[.]205[.]155` | ipv4 | ARTEX-realm server and primary source of reported self-registration/API activity | Medium | main-iocs |
| `nonexistent-i3185` | canary_string | Vendor-observed ARTEX-associated software/canary marker | Low | software-fingerprints |
| `zz-no-such-key-1a2b3c.html` | canary_string | Vendor-observed ARTEX-associated software/canary marker | Low | software-fingerprints |
| `zz_no_such_user_9f3a` | canary_string | Vendor-observed ARTEX-associated software/canary marker | Low | software-fingerprints |
| `zzq.nonexistent9x7` | canary_string | Vendor-observed ARTEX-associated software/canary marker | Low | software-fingerprints |
| `zzzrandom12345` | canary_string | Vendor-observed ARTEX-associated software/canary marker | Low | software-fingerprints |
| `WWW-Authenticate: Basic realm="ARTEX"` | http_auth_realm | Vendor-observed ARTEX-associated software/canary marker | Low | software-fingerprints |
| `Mozilla/5.0 (Windows NT 10.0; Win64; x64) recon-audit` | user_agent | Vendor-observed ARTEX-associated software/canary marker | Low | software-fingerprints |
| `Mozilla/5.0 (security-testing; authorized)` | user_agent | Vendor-observed ARTEX-associated software/canary marker | Low | software-fingerprints |

[Evidence methodology](../../../docs/methodology.md).
