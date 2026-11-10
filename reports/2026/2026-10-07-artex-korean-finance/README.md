# Artex Korean Finance

Report date: 2026-10-07. Collection reviewed: 2026-11-10. Source: [crowdstrike](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/). This folder contains 12 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `101[.]53[.]80[.]20` | ipv4 | Proxies (CrowdStrike); Proxy IP address | Medium | campaign-context |
| `103[.]248[.]148[.]84` | ipv4 | Proxies (CrowdStrike); Proxy IP address | Medium | campaign-context |
| `124[.]155[.]252[.]63` | ipv4 | Proxies (CrowdStrike); Proxy IP address | Medium | campaign-context |
| `154[.]201[.]79[.]246` | ipv4 | Proxies (CrowdStrike); Proxy IP address | Medium | campaign-context |
| `203[.]160[.]133[.]172` | ipv4 | Proxies (CrowdStrike); Proxy IP address | Medium | campaign-context |
| `205[.]214[.]59[.]31` | ipv4 | Proxies (CrowdStrike); Proxy IP address | Medium | campaign-context |
| `209[.]209[.]85[.]38` | ipv4 | Proxies (CrowdStrike); Proxy IP address | Medium | campaign-context |
| `23[.]158[.]220[.]98` | ipv4 | Proxies (CrowdStrike); Proxy IP address | Medium | campaign-context |
| `23[.]248[.]249[.]90` | ipv4 | Proxies (CrowdStrike); Proxy IP address | Medium | campaign-context |
| `38[.]244[.]50[.]120` | ipv4 | Reported attacker-controlled ARTEX host and open directory | Medium | main-iocs |
| `38[.]244[.]50[.]120:18899` | network_endpoint | Attacker open-directory service | Medium | main-iocs |
| `hxxp://38[.]244[.]50[.]120:18899/.claude/CLAUDE.md` | url | Published attacker-side open-directory artifact URL | Medium | main-iocs |

[Evidence methodology](../../../docs/methodology.md).
