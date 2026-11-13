# Global source review — 13 November 2026

This supplement adds **86 source records covering 81 values new to the master**; five existing values gain source evidence. They are historical observations and context, not 86 newly active threats. Our independent-artifact lane produced **zero new malicious IOCs** today.

| Evidence class | Records | Export |
|---|---:|---|
| Reported incident/campaign observables | 40 | [Sourced IOCs](sourced-iocs.csv) |
| OSINT deployment leads | 6 | [Deployment leads](deployment-leads.csv) |
| Software/certificate/key references | 13 | [Software fingerprints](software-fingerprints.csv) |
| Supporting image references | 2 | [Supporting tools](supporting-tools.csv) |
| Shared services and generic markers | 25 | [Shared context](shared-context.csv) |

[Full JSON](records.json) · [All-record CSV](indicators.csv) · [Sources](sources.json). Seven literal IPs are newly added to the overview; domain-only records were not resolved. No new India targeting or current liveness is asserted.

## Source roles and dates

[Eye Security, 12 November](https://labs.eye.security/how-we-defended-against-an-ai-driven-attack/) reports an incident, webshell/probe artifacts and an exact callback hostname. Its separate OSINT infrastructure list is retained as deployment leads. The reported webshell credential is omitted. Shared callback providers, library UAs, short prefixes and synthetic identities are context. Two published Git-author identities required decoding publisher email obfuscation; their encoded locators and method are preserved.

[Gambit's original report](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company) supplies historical C2, staging, exfiltration and skimmer infrastructure. Roles remain distinct, including nine scheme-less skimmer host/path values; no scheme was invented. The visible page says **22 September 2026 / Eyal Sela**, while JSON-LD says **8 October / Curtis Simpson**. Records retain this disagreement and use the visible editorial date with an explicit basis. Named Hermes/Strix/Cairn use is campaign-level context; exact upstream/deployed-revision links remain unproven.

[Arctic Wolf's pinned 10 November alert](https://github.com/rtkwlf/wolf-tools/blob/c18da9b1ad3186f9255c45e6c0b3560e897ac1df/pack_alerts/202611-antifox-alibaba-hosted-platforms-facilitate-web-cloud-intrusions/README.md) links AntiFox-hosting source infrastructure to IIS/AWS intrusions. Its two IPs are not relabeled C2. The opaque banner hash has no stated algorithm/input, so is not called a malware SHA1. SDK UAs remain generic. The alert links the AntiFox repository; current source identity does not establish the campaign-generating revision.

[SOCRadar's 12 November report](https://socradar.io/blog/artex-ai-pentest-consoles-us/) provides three X.509 leaf fingerprints and four SSH host-key fingerprints from its 11 November snapshot. Shared images/keys can explain clustering; common operator or malicious use is not established. Its public 1,295-IP candidate file does not identify the 916 confirmed subset. The 89 candidates absent from our prior map were excluded from admission; no prefixes were expanded. Existing favicon references were corroborated without new discovery claims.

## Independent work and tooling

The newly available 11 November public sample-archive directory contained 676 entries. Sixteen selected source-backed seeds and an offline comparison with 81 baseline SHA256 values produced no match. The 12 November archive returned 404; two new exact public recorded-analysis searches returned no report. No sample body was acquired, authenticated 403 request retried, or sample executed.

The [tool index](../../../tools/README.md) adds ten verified identities, reaching **33**, and records AI-Infra-Guard v4.6.10. CyberStrike is distinct from CyberStrikeAI. AntiFox and ScopeWeaver have source-backed ARTEX lineage; Cybermes acknowledges NousResearch Hermes, which does not prove that identity was used in Gambit's campaign. Runtime fingerprints and maliciousness remain separate from documentation identities.

All new records are externally sourced. Raw publisher captures and review receipts remain private. No paid-provider/Censys calls, candidate probing, DNS resolution, controller access, execution or sensor deployment occurred. The public inventory remains a mixed evidence catalog, not an automatic block list.
