# Global aggregation and independent collection — 12 November 2026

The aggregation lane continues alongside development of independent collection. This supplement adds **47 exact values new to this repository** from historical primary reporting; it does not assert 47 newly active threats.

| Evidence class | Records | Export |
|---|---:|---|
| Source-reported campaign observables | 44 | [Sourced IOCs](sourced-iocs.csv) |
| Generic host paths requiring correlation | 2 | [Host artifacts](host-artifacts.csv) |
| Operator-support domain context | 1 | [Supporting context](supporting-context.csv) |

[All records CSV](indicators.csv) · [Full records JSON](records.json) · [Sources](sources.json). The additions include **12 literal IPs** and **25 payload SHA256 identities**. Those hashes were transcribed from sources; their sample bytes were not acquired in this run. One hash has two published filename aliases; the uncertain `c22.exe` mapping stays Medium confidence.

## Historical campaign evidence

[Hunt's SecFlow investigation, 3 September](https://hunt.io/blog/chinese-operator-secflow-claude-qwen-deepseek-asia), supplies orchestration, payload, redirector, proxy and host-artifact evidence. SecFlow is the AI orchestrator; SecBox and GLUTTON have separate malware/tool roles. No ARTEX or CyberStrikeAI lineage is inferred. Publisher capture dates are retained as acquisition context, with unknown first/last malicious activity left blank. The support-domain wildcard is not expanded into a block list.

[NorForge's Cairn investigation, 19 October](https://norforge.com/blog/inside_cairn), supplies two fully disclosed AIA0002 staging IPs. They are not labeled controller panels or C2. Redacted panel addresses remain excluded. [Cairn identity](cairn-identity.json) pins the official `oritera/Cairn` README; it is distinct from CAI and similarly named products. No campaign-generating revision was established.

[Unit 42's newer ecosystem review](https://unit42.paloaltonetworks.com/artex-and-ai-powered-red-teaming-tools/) was published at **2026-11-11 23:00:53 UTC**, falling on 12 November in India. It contributes context and discovery leads, not an exact malicious network/file IOC set in this supplement. Cadence patterns, example domains and placeholder input values are not standalone malicious indicators.

## Developing our own collection

[Our collection design](../../../docs/original-ioc-collection.md) distinguishes external reporting, independent artifact derivation, first-party telemetry, reference fingerprints and enrichment. No owned sensor is deployed and no new first-party attack telemetry is claimed.

The independent lane checked exact source-backed sample hashes against retained archive indexes and two fresh public daily directories, and checked four public recorded-analysis searches. A documented authenticated exact-hash metadata request returned HTTP 403; its cause was not established and no alternate credential or access route was attempted. It acquired no matching new sample or task. Consequently **zero new independently derived malicious IOCs** were admitted today. Existing CyberStrikeAI native configuration remains valid prior analysis, not a new discovery.

A bounded exact-member acquisition helper and an offline owned-sensor observation adapter were developed privately. They do not execute samples, start sensors, contact candidate infrastructure or automatically publish observations. The adapter must be distinguished from an operating sensor. The aggregation lane was not blocked by these acquisition gaps.

## Tool index and our source hypotheses

The separate [tool index](../../../tools/README.md) now contains 23 verified identities, including 15 newly indexed candidates. Two independently derived source identification hypotheses for Cairn and Shannon remain outside the admitted IOC catalog: their source presence is verified, while runtime specificity and malicious use are unestablished. They add no map locations.

## Additional recent-source review

[Strand Intelligence](https://www.strandintelligence.com/blog/anatomy-of-artex-infrastructure-indicators-and-implications) corroborates the existing ARTEX favicon identity and authentication realm; lab/example infrastructure was excluded. [Sophos](https://www.sophos.com/en-us/blog/artex-attackers-apply-agentic-ai) provides vendor detection identifiers and behavioral guidance, not an additional malicious network/file IOC set. Its rendered article was reviewed; direct raw capture timed out. Neither review increased the admitted count.

## Review limits

Exact source literals, hashes, normalization, aliases, role boundaries and corpus overlap were checked independently. No target probing, candidate DNS resolution, sample execution, Censys MCP call or paid-provider use occurred. Historical infrastructure can be reassigned. Reconstructing private/redacted infrastructure or treating enrichment as proof of compromise remains outside the admission standard.
