# Artex Exposed Secrets

Report date: 2026-11-05. Collection reviewed: 2026-11-10. Source: [microsoft_secrets](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/). This folder contains 4 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `157[.]22[.]126[.]128` | ipv4 | Reconnaissance against victim Azure AI workloads | Medium | campaign-context |
| `199[.]19[.]77[.]18` | ipv4 | Sign-ins using leaked/stolen application credentials; Tor exit node | Medium | campaign-context |
| `199[.]19[.]77[.]84` | ipv4 | Successful service-principal sign-ins and follow-on cloud operations | Medium | campaign-context |
| `65[.]87[.]223[.]26` | ipv4 | Malicious requests, embedded shell commands in UA, attempts to obtain App Service tokens | Medium | campaign-context |

[Evidence methodology](../../../docs/methodology.md).
