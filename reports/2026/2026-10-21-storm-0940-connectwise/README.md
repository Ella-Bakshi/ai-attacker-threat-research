# Storm 0940 Connectwise

Report date: 2026-10-21. Collection reviewed: 2026-11-10. Source: [microsoft_storm0940](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/). This folder contains 6 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `144[.]172[.]64[.]128` | ipv4 | Storm-0940 infrastructure (Microsoft); Storm-0940 service-principal sign-ins and Graph API activity; Incident-associated source / Storm-0940 overlap | Medium | campaign-context |
| `144[.]172[.]64[.]60` | ipv4 | Storm-0940 infrastructure (Microsoft); Storm-0940 service-principal sign-ins and Graph API activity; Incident-associated source / Storm-0940 overlap | Medium | campaign-context |
| `144[.]172[.]64[.]99` | ipv4 | Storm-0940 infrastructure (Microsoft); Storm-0940 service-principal sign-ins and Graph API activity; Incident-associated source / Storm-0940 overlap | Medium | campaign-context |
| `187[.]15[.]88[.]186` | ipv4 | Transient VPN source in compromised-app activity | Medium | campaign-context |
| `187[.]15[.]89[.]186` | ipv4 | Transient VPN source in compromised-app activity | Medium | campaign-context |
| `187[.]15[.]90[.]217` | ipv4 | Transient VPN source in compromised-app activity | Medium | campaign-context |

[Evidence methodology](../../../docs/methodology.md).
