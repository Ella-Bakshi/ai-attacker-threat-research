# Vapor Panda Artex

Report date: 2026-10-29. Collection reviewed: 2026-11-10. Source: [crowdstrike_vapor_panda](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/). This folder contains 11 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `nginxmysql[.]com` | domain | BLOODALCHEMY C2 domain | Medium | campaign-context |
| `sqlserver-sqlite[.]com` | domain | BLOODALCHEMY C2 domain | Medium | campaign-context |
| `www[.]ddduuuppp[.]com` | domain | BLOODALCHEMY C2 domain | Medium | campaign-context |
| `192[.]121[.]47[.]20` | ipv4 | IP address of www[.]ddduuuppp[.]com | Medium | campaign-context |
| `45[.]153[.]126[.]223` | ipv4 | IP address of nginxmysql[.]com | Medium | campaign-context |
| `89[.]46[.]234[.]50` | ipv4 | IP address of sqlserver-sqlite[.]com | Medium | campaign-context |
| `C:\ProgramData\artx5v\` | path | Campaign-specific ARTEX artifact directory | Low | software-fingerprints |
| `D:\ProjectX\Merman_New\` | path | Internal BLOODALCHEMY project path reported in implant | Low | supporting-tools |
| `364251838edfcf5ef1107fa692da3c5bd9a540482449f645992830134bf807ab` | sha256 | BLOODALCHEMY payload file (graphics-hook_config.bin) | High | supporting-tools |
| `3fb5a9fb3e2cb1d6208966bd4e55d10282d19c7250d827efa560463d60a12ee4` | sha256 | BLOODALCHEMY loader DLL (graphics-hook-filter64.dll) | High | supporting-tools |
| `49fe70419fd19b81ca8d730a6ef7c1ec71b681d60b390761070d42686c7d2068` | sha256 | GameHook binary renamed svchost.exe | High | supporting-tools |

[Evidence methodology](../../../docs/methodology.md).
