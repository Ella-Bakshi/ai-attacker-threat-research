# Deep Srm

Report date: 2026-11-04. Collection reviewed: 2026-11-10. Source: [deep_srm](https://www.s-rminform.com/latest-thinking/artex-in-the-wild-lessons-from-responding-to-agentic-ai-attacks). This folder contains 3 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `ARTEX – Autonomous pentest console` | html_title | Reported incident-source Next.js console title | Low | software-fingerprints |
| `tasks/<taskID>/i<intentID>/` | path_pattern | Agent working-folder template correlated by S-RM | Low | software-fingerprints |
| `ARTEX' UNION SELECT 1—` | sql_probe_string | SQL probe marker in incident response cases | Low | software-fingerprints |

[Evidence methodology](../../../docs/methodology.md).
