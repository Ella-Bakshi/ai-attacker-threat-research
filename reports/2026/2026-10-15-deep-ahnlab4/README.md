# Deep Ahnlab4

Report date: 2026-10-15. Collection reviewed: 2026-11-10. Source: [deep_ahnlab4](https://asec.ahnlab.com/en/95875/). This folder contains 9 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `bob-research-skills-en.Zip` | filename | Repackaged REAPER skill archive | Low | software-fingerprints |
| `skills-translated-en.Zip` | filename | Repackaged skill collection archive | Low | software-fingerprints |
| `artex-ko` | path | Localization directory marker | Low | software-fingerprints |
| `reaper-full` | path | Rebranded ARTEX project directory/name | Low | software-fingerprints |
| `cache.Php` | filename | REAPER follow-on PHP payload name | Low | supporting-tools |
| `irc.Php` | filename | REAPER persistence/IRC control implant name | Low | supporting-tools |
| `#mg_master` | irc_channel | Reported channel used by REAPER follow-on IRC implant | Low | supporting-tools |
| `!Cmd@` | protocol_command | Reported IRC implant command marker | Low | supporting-tools |
| `!Cmd@all` | protocol_command | Reported IRC implant broadcast command marker | Low | supporting-tools |

[Evidence methodology](../../../docs/methodology.md).
