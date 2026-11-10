# C2 infrastructure targeting India

**Targeting India means the campaign targets Indian entities. Infrastructure can be hosted anywhere, including an abused SaaS tenant or resource.** No hosting-country filter is applied. A primary report's campaign-level victimology is sufficient for this scoped association; identifying a named Indian victim for every endpoint is not required.

This view contains **17 source-reported C2 indicator records** from APT36 vibeware, Gopher Strike and Sheet Attack. They were already present in the research dataset; this update clarifies their roles and adds no newly discovered endpoint. These separate campaigns have no established ARTEX/CyberStrikeAI/CRAFTY FALCON link. The restricted CERT-In framework-linked set remains a separate evidence gap.

- [C2 infrastructure CSV](c2-infrastructure-targeting-india.csv) · [Full provenance JSON](c2-infrastructure-targeting-india.json)
- [Initial-access and payload-delivery infrastructure CSV](delivery-infrastructure-targeting-india.csv) · [JSON](delivery-infrastructure-targeting-india.json): 22 records
- [Backup C2-configuration resources CSV](c2-configuration-resources-targeting-india.csv) · [JSON](c2-configuration-resources-targeting-india.json): two records, kept separate from tasking endpoints
- [Role counts and inclusion policy](network-role-summary.json) · [Complete India campaign supplement](additional-ai-campaigns/README.md)

Counts refer to values/records, not distinct servers. A domain and its URL can describe the same infrastructure; delivery and C2 roles can overlap. SaaS indicators apply to the reported tenant or resource, not the provider's entire domain or address space. Network confidence is medium for historical source-reported association, with current reachability, ownership and individual victim compromise unverified. Three URL-prefix records omit authentication-like query values; they are not exact complete request URLs.

| Campaign | Indicator (defanged) | Reported role | Source date | Confidence | Source |
|---|---|---|---|---|---|
| APT36-vibeware | 23[.]152[.]0[.]81 | Havoc C2, also used as CobaltStrike and Mythic C2 | 2026-03-05 | Medium | [Primary source](https://github.com/bitdefender/malware-ioc/blob/5a4f9b09091d530ab99dabad044bd542c2bd5e12/2026_03_05-apt36-iocs.csv) |
| APT36-vibeware | 45[.]56[.]162[.]170:8000 | C2 used to download malicious files, also used as CobaltStrike C2; port 8000 is the reported download endpoint, not a verified Beacon listener | 2026-03-05 | Medium | [Primary source](https://github.com/bitdefender/malware-ioc/blob/5a4f9b09091d530ab99dabad044bd542c2bd5e12/2026_03_05-apt36-iocs.csv) |
| APT36-vibeware | slackin[.]online | NimShellcodeLoader Cobalt Strike C2 using Azure Front Door | 2026-03-05 | Medium | [Primary source](https://www.bitdefender.com/en-us/blog/businessinsights/apt36-nightmare-vibeware) |
| Gopher Strike | govt-filesharing[.]site | C2 domain | 2026-01-26 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-gogitter-gitshellpad-and-goshell) |
| Gopher Strike | ingov[.]myartsonline[.]com | C2 domain | 2026-01-26 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-gogitter-gitshellpad-and-goshell) |
| Gopher Strike | listsoft-update[.]site | C2 domain | 2026-01-26 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-gogitter-gitshellpad-and-goshell) |
| Gopher Strike | workspace1[.]myartsonline[.]com | C2 domain | 2026-01-26 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-gogitter-gitshellpad-and-goshell) |
| Gopher Strike | https://adobe-acrobat[.]in/ninevmc987[.]php?file=bncoeeav34564cvv94adfavc3354334dfsf | C2 URL | 2026-01-26 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-gogitter-gitshellpad-and-goshell) |
| Gopher Strike | http://ingov[.]myartsonline[.]com/hpc5985[.]php | C2 URL | 2026-01-26 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-gogitter-gitshellpad-and-goshell) |
| Gopher Strike | http://workspace1[.]myartsonline[.]com/hpc5985[.]php | C2 URL | 2026-01-26 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-gogitter-gitshellpad-and-goshell) |
| Gopher Strike | https://govt-filesharing[.]site/hpc5985[.]php | C2 URL | 2026-01-26 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-gogitter-gitshellpad-and-goshell) |
| Sheet Attack | gov-service-in-default-rtdb[.]firebaseio[.]com | FIREPOWER C2 domain | 2026-01-27 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-sheetcreep-firepower-and) |
| Sheet Attack | govs-services-in-default-rtdb[.]firebaseio[.]com | FIREPOWER C2 domain | 2026-01-27 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-sheetcreep-firepower-and) |
| Sheet Attack | webdevurl-cc389-default-rtdb[.]firebaseio[.]com | FIREPOWER C2 domain | 2026-01-27 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-sheetcreep-firepower-and) |
| Sheet Attack | https://docs[.]google[.]com/spreadsheets/d/1cB8jzFpQcixridoEz_eDvLnjCTx79gKFQSoFiuOErdM/edit | C2 URL | 2026-01-27 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-sheetcreep-firepower-and) |
| Sheet Attack | https://docs[.]google[.]com/spreadsheets/d/1cdSJvZ7tx6CPBuEa66uTVWmSD4zABnZOLjM87pRXkTE/edit | C2 URL | 2026-01-27 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-sheetcreep-firepower-and) |
| Sheet Attack | https://docs[.]google[.]com/spreadsheets/d/1wgx4gj3-YGGAwmtr1DRu4n1QkznK2pYoKO6C4GTmquY/edit | C2 URL | 2026-01-27 | Medium | [Primary source](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-sheetcreep-firepower-and) |
