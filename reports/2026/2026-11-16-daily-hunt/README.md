# AI Attacker Threat Research — 16 November 2026

This manual run adds **50 reviewed memberships: 40 new type/value pairs and 10 corroborating memberships**. Totals are **12,811 canonical records**, **16,336 master values** and **6,490 selected IPs**. There are no new IP values. These are research totals across evidence classes, not counts of malicious systems.

[JSON](records.json) · [CSV](records.csv) · [Delta](summary.json) · [Remaining uncertainty](remaining-unverified.csv).

## Our exact-artifact findings

[Independent analysis](../../../research/analyst-derived/2026-11-16-exact-public-artifacts/README.md) acquired two exact public artifacts: a Talos-listed NIK C2 implant and Cursor's identified modified extension.js. Recalculated identities and static analysis add **19 own memberships: 13 new values and six corroborations**. Ten identity/configuration observations use score 60; nine host, software or fragment fingerprints use 20. Scores express evidence strength, not maliciousness probabilities.

Sixteen selected NIK functions were reconstructed from 261 recovered application functions and a 6,571-function Go/runtime inventory. Original-byte checks support its decoded primary URL, POST heartbeat construction and conditional fallback. The fallback is not initially needed with the valid primary configuration. JavaScript analysis covers the 7,386-byte injected prologue, public SSH fingerprints, conditional filenames/LaunchAgent label and existing external POST destination. Neither whole program was exhaustively analyzed or executed.

No new exact ARTEX/CyberStrikeAI campaign sample, observed persistence/traffic, or new independently verified malicious C2 IP was obtained. Expanded families retain their own identities.

## Aggregation and software references

[Seventeen sourced campaign artifacts](sourced-iocs.csv) come from GreyNoise's original PaperCut investigation; its two IPs were already cataloged. Five algorithm-uncertain hash literals and an ambiguous filename were withheld. [Four Cloudflare Worker naming patterns](campaign-context.csv) remain broad campaign context, without specific malicious-domain or blocking claims.

[Software references](software-fingerprints.csv) include source-attributed ARTEX/SDK user-agent corroborations and four strings independently inspected in pinned CyberStrikeAI/HexStrike source. Runtime reachability and specificity remain qualified. The legitimate PentAGI reporting service stays [supporting context](supporting-tools.csv), score 0.

The [Global Edition source review](../../../research/software-fingerprints/2026-11-16-artex-global-source/README.md) adds three independently checked, maintainer-listed references: updater User-Agent, conditional guard framing and a seven-table schema conjunction. They establish no hostile installation or universal ARTEX behavior. The [CTI Academy review](cti-academy-review.md) distinguishes 3 November publication from 16 November modification and lab findings from incident evidence.

The [registry](../../../tools/README.md) adds LuaN1aoAgent, reaching **43 identities**, with pinned ownership, license and qualified release history. Inclusion does not establish malicious use. Global Edition is a separately qualified ARTEX fork resource.

## Coverage and limitations

[GTIG's new report](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold) adds contemporary context without an exact network/file IOC table admitted here. [Elastic](https://www.elastic.co/security-labs/threat-command/agentic-offensive-frameworks-detection-artex), [Cloudflare](https://blog.cloudflare.com/adapting-to-ai-penetration-testing-orchestrators/) and [Qualys](https://blog.qualys.com/misc/2026/11/15/artex-moves-at-machine-speed-what-risk-owners-need-to-change) were read as underlying sources. Tool names, speed and generic probe strings do not establish AI authorship or operator identity.

Original-source and visual review of a ColCERT advisory rejected an incorrect search-snippet octet and a separate internally inconsistent proxy address. Neither questionable address was added. **35 existing source/relationship questions remain separate**; no resolving evidence was established this pass.

The source lane processed 43 public-web query executions and nine exact source windows, alongside Google discovery. Five Censys actions and five Shodan title searches provided private index context only. Account-only observations were not republished as a public feed. No new scans, target connections, DNS queries or sample submissions occurred. A new archive window returned 404; successful coverage was not claimed. This is finite research, not all-internet completeness.

The original 9,053-record core, 342-record derived collection and dated uncertainty snapshots remain unchanged. Current summary metadata now agrees with 13 YARA declarations in nine files, nine main CyberStrikeAI records and zero unresolved original hash algorithms. Physical report-folder counts are labeled separately from historical cohorts; these metadata corrections change no indicator identity.
