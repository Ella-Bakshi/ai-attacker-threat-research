# Aws Fortigate Campaign Context

Report date: 2026-02-20. Collection reviewed: 2026-11-10. Source: [aws_fortigate](https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/). This folder contains 2 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `185[.]196[.]11[.]225` | ipv4 | Threat operations infrastructure in AWS FortiGate campaign | Medium | campaign-context |
| `212[.]11[.]64[.]250` | ipv4 | Scanning/exploitation infrastructure in AWS FortiGate campaign; separate CyberStrikeAI banner observation by Team Cymru | Medium | campaign-context |

[Evidence methodology](../../../docs/methodology.md).
