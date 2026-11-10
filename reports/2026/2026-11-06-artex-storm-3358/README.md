# Artex Storm 3358

Report date: 2026-11-06. Collection reviewed: 2026-11-10. Source: [microsoft_storm3358](https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-sector/). This folder contains 7 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `199[.]19[.]95[.]66` | ipv4 | WISP C2 node | Medium | campaign-context |
| `199[.]19[.]95[.]67` | ipv4 | WISP C2 node | Medium | campaign-context |
| `199[.]19[.]95[.]68` | ipv4 | WISP C2 node | Medium | campaign-context |
| `85[.]11[.]167[.]52` | ipv4 | C2 server | Medium | campaign-context |
| `31[.]77[.]229[.]35` | ipv4 | ARTEX server | Medium | main-iocs |
| `85[.]11[.]168[.]45` | ipv4 | ARTEX server | Medium | main-iocs |
| `91[.]92[.]240[.]238` | ipv4 | ARTEX server | Medium | main-iocs |

[Evidence methodology](../../../docs/methodology.md).
