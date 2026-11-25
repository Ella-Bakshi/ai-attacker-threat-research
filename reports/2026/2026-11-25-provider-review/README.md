# 25 November 2026 provider review

This release adds **5,070 passive deployment evidence records** for **5,067 distinct endpoints**. **3,168 endpoints** are new to the master index. The selected map gains **2,695 unique IPs**. No new incident-confirmed C2 relationship was verified. [Records](records.json) · [CSV](records.csv) · [Counts](summary.json)

## Offensive Agency

**5,066** observations come from the public Offensive Agency host snapshot acquired on **25 November 2026 at 17:29 UTC**. This projection covers registered tool identities with a publisher-confirmed classification and one explicitly associated port. The provider's host first and last dates are retained separately from the port observation. Shared front ends, uncertain classifications and ambiguous associations were held for review.

Attribution **offensive.agency, data by ONYPHE**, licensed under CC BY 4.0. We selected and normalized source observations, added evidence scopes and enriched the IP map with its separate open metadata. [Provider methodology and license](https://offensive.agency/about) · [Public source](https://offensive.agency/api/hosts.json) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

| Tool | Source observations |
| --- | ---: |
| ARTEX | 3,206 |
| CyberStrikeAI | 968 |
| PentAGI | 522 |
| AutoCVE | 248 |
| Cairn | 40 |
| RedAmon | 36 |
| Strix | 21 |
| CyberStrike | 11 |
| Xalgorix | 5 |
| AIDA | 5 |
| BugTraceAI | 3 |
| Decepticon | 1 |

## Pasted-row cross-checks

Four pasted CyberStrikeAI endpoints had public historical scans that identify the console using its title and favicon. These four observations are cited to their scan records. Three also meet the Offensive Agency admission criteria. The fourth has an explicit port in the ScanMalware evidence. The existing two public RST Cloud records already preserve the related Cairn evidence. Pasted rows without independent public support remain private. [ScanMalware console hunt](https://scanmalware.com/hunts/337) · [RST Cloud analysis](https://www.rstcloud.com/hunting-ai-harnesses-cairn-artex-pentagi/)

The score of 20 represents passive deployment evidence. Each source supports its own date and role. The publisher's software match establishes no particular attack, operator or victim.
