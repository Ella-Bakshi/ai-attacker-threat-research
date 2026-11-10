# Datadog

Report date: 2026-11-09. Collection reviewed: 2026-11-10. Source: [datadog](https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/). This folder contains 20 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `102[.]216[.]154[.]102` | ipv4 | Incident-associated traffic source | Medium | campaign-context |
| `103[.]54[.]154[.]32` | ipv4 | Incident-associated traffic source | Medium | campaign-context |
| `103[.]54[.]154[.]40` | ipv4 | Incident-associated traffic source | Medium | campaign-context |
| `154[.]36[.]136[.]197` | ipv4 | Incident-associated traffic source | Medium | campaign-context |
| `154[.]36[.]136[.]23` | ipv4 | Incident-associated traffic source | Medium | campaign-context |
| `154[.]64[.]252[.]77` | ipv4 | Incident-associated traffic source | Medium | campaign-context |
| `169[.]128[.]55[.]214` | ipv4 | Incident-associated traffic source | Medium | campaign-context |
| `45[.]145[.]228[.]25` | ipv4 | Incident-associated traffic source | Medium | campaign-context |
| `82[.]158[.]88[.]233` | ipv4 | Incident-associated traffic source | Medium | campaign-context |
| `88[.]229[.]22[.]232` | ipv4 | Incident-associated traffic source | Medium | campaign-context |
| `ARTEX-worker/1.0` | user_agent | Observed ARTEX-related UA | Low | software-fingerprints |
| `Mozilla/5.0 (Windows NT 10.0; Win64; x64) ARTeX-authorized-pentest` | user_agent | Observed ARTEX-related UA | Low | software-fingerprints |
| `Mozilla/5.0 (X11; Linux x86_64) artex-verify/1.0` | user_agent | Observed ARTEX-related UA | Low | software-fingerprints |
| `Mozilla/5.0 ARTeX` | user_agent | Observed ARTEX-related UA | Low | software-fingerprints |
| `artex-audit/1.0` | user_agent | Observed ARTEX-related UA | Low | software-fingerprints |
| `artex-i21861-canary` | user_agent | Observed ARTEX-related UA | Low | software-fingerprints |
| `artex-pentest/1.0` | user_agent | Observed ARTEX-related UA | Low | software-fingerprints |
| `artex-readonly/1.0` | user_agent | Observed ARTEX-related UA | Low | software-fingerprints |
| `artex-spawn/1` | user_agent | Observed ARTEX-related UA | Low | software-fingerprints |
| `artex-verify/1.0` | user_agent | Observed ARTEX-related UA | Low | software-fingerprints |

[Evidence methodology](../../../docs/methodology.md).
