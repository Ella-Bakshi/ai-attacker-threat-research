# Reading Censys AI-framework labels

Censys publicly documented ARTEX/ScopeWeaver detection by 5 November 2026. Its 12 November article gives a seven-family roster query. These sources establish published detection support; they do not establish when a particular account received a feature or a new label was launched.

```text
host.services.threats.name: {"ARTEX", "ScopeWeaver", "CyberStrikeAI", "PentAGI", "HexStrike AI", "RedAmon", "Cairn"}
or web.threats.name: {"ARTEX", "ScopeWeaver", "CyberStrikeAI", "PentAGI", "HexStrike AI", "RedAmon", "Cairn"}
```

Source: [Censys, 12 November](https://censys.com/blog/artex-and-ai-attack-tools-why-threat-intelligence-must-originate-from-first-party-data). This query has not been executed locally. It searches provider labels, including potentially authorized deployments. No current count, actor attribution or maliciousness follows from the query itself.

The [5 November ARC article](https://censys.com/blog/artex-agentic-asbestos) also publishes a console query combining a title pattern with Next.js assets:

```text
(web.endpoints.http.html_title=~"^ARTEX[ :—]" and web.endpoints.http.body: "_next/static" ) or (host.services.endpoints.http.html_title =~ "^ARTEX[ :—]" and host.services.endpoints.http.body: "_next/static")
```

That is a software reference, not a locally benchmarked production detector. A title or generic Next.js asset alone is weak evidence; preserve service, port and endpoint context.

| Provider field | Meaning and limit |
|---|---|
| `host.services.threats` / `web.threats` | Service/endpoint detections. Inspect `name`, `id`, `type`, `source` and `confidence`. Do not transfer one service's role to every service on the IP. |
| `*.threats.evidence.data_path` / `found_value` | Where the match occurred and the matched value. Account access may be required. Preserve an exact evidence locator privately within the licensed interface. |
| `threats.confidence` | Reliability of the provider's identification; it is not our maliciousness assessment. |
| `host.reputation` | A separate model assessment using multiple host signals. Its category and risk score do not map to our ordinal evidence rubric. |

The [threat-data documentation](https://docs.censys.com/docs/platform-threat-hunting-threat-hunting-dataset) distinguishes security tools from C2 and other threat types. Inspect the actual returned type; a framework name alone does not establish it. Actor metadata describes groups previously associated with tooling, not proof of an actor on the individual host.

Threat history can remain visible after recent scans stop matching. Retain scan/detection times separately from article publication, lookup time and victim activity. Co-location, certificates and historical DNS associations require their own relationship evidence.

The [reputation documentation](https://docs.censys.com/docs/platform-reputation-scores) describes a 0–100 query/UI scale and floating-point raw values. The 12 November agent-file example uses `host.reputation.score > 0.5`. Treat this as a scale/version ambiguity and confirm semantics before reusing it; it is not our score threshold and was not executed here.

Use existing indexed observations. No live discovery/rescan, candidate connection or sample submission is needed for this workflow. Private account results remain private; a narrowly documented public article or artifact may support its own separately cited record. No account export was used for the linked public-figure finding.
