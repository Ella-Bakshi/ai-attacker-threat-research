# Artex Multi Country Workspaces

Report date: 2026-10-21. Collection reviewed: 2026-11-10. Source: [zscaler_global_ai_campaign](https://www.zscaler.com/es/blogs/security-research/inside-global-ai-assisted-hacking-campaign). This folder contains 9 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `161[.]8[.]161[.]140` | ipv4 | Upstream SOCKS proxy host | Medium | campaign-context |
| `154[.]201[.]79[.]246:443` | network_endpoint | Proxy pool API | Medium | campaign-context |
| `161[.]8[.]161[.]140:11005` | network_endpoint | Upstream SOCKS proxy | Medium | campaign-context |
| `205[.]214[.]59[.]31:443` | network_endpoint | Upstream SOCKS proxy | Medium | campaign-context |
| `23[.]248[.]226[.]250` | ipv4 | Work server | Medium | main-iocs |
| `23[.]248[.]226[.]251` | ipv4 | Work server | Medium | main-iocs |
| `23[.]248[.]226[.]252` | ipv4 | Work server | Medium | main-iocs |
| `23[.]248[.]226[.]253` | ipv4 | Work server | Medium | main-iocs |
| `23[.]248[.]226[.]254` | ipv4 | Work server | Medium | main-iocs |

[Evidence methodology](../../../docs/methodology.md).
