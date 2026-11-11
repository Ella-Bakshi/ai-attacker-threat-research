# Global AI tooling and campaign research — 11 November 2026

This supplement adds **44 exact type/value records new to this repository**. It preserves source-reported campaign evidence separately from our software analysis. No global first-discovery claim is made.

| Evidence class | Records | Export |
|---|---:|---|
| Reported campaign observables | 27 | [Sourced IOCs](sourced-iocs.csv) |
| Software fingerprints and host patterns | 14 | [Fingerprints](software-fingerprints.csv) |
| Historical PentAGI service identification | 1 | [Deployment lead](deployment-leads.csv) |
| Nonindicative supporting context | 2 | [Context](supporting-context.csv) |

[All records CSV](indicators.csv) · [Full records JSON](records.json) · [Sources](sources.json) · [Tool registry](tools.json). The nine independently derived records are also available in [our source-fingerprint export](our-source-fingerprints.csv).

## Reported campaign evidence

The [SOCRadar CyberXero investigation, 6 October](https://socradar.io/blog/cyberxero-ai-iab-ukraine-critical-infrastructure/), and [10 November profile](https://socradar.io/blog/dark-web-profile-cyberxero/) provide operator, staging, Cobalt Strike and file observables. [Hunt's PaperCut investigation, 15 October](https://hunt.io/blog/papercut-attacker-ai-toolkit-exploit-code-second-rce), provides orchestration, file-staging, reverse-tunnel and collection-tool observables.

Ten distinct IPs enter the overview. Their original roles and unknown activity times remain explicit. Campaign artifacts use `OtherAIThreatResearch`; co-location with PentAGI does not establish that PentAGI implements a Cobalt Strike listener. The specifically reported PentAGI certificate/service at port 33333 remains a software/service identification. Generic PentAGI certificate or TLS-stack matches are excluded as campaign pivots. No current operation or India association is inferred.

## Our additional tool fingerprints

| Project | Pinned revision | Our records | Identification scope |
|---|---|---:|---|
| [Strix](https://github.com/usestrix/strix) | `685bbc8138d35fc9fe378ac37ec0d9198b9c46a3` | 5 | Viewer header/cookie patterns, HTML asset conjunction, PNG identity and local output path |
| [PentestGPT](https://github.com/GreyDGL/PentestGPT) | `e8b1bb77d1ac00329675cec3b060aba971ec1ac8` | 2 | Separate legacy and agent-subproject package/CLI identities |
| [CAI](https://github.com/aliasrobotics/cai) | `6dc79257777f5f1c9500b4d2319935d34a47412e` | 2 | Archived API/application and package identities |

Strix and PentestGPT are open-source security tools. CAI's archived revision has mixed licensing and is described here as **source-available**, not wholly OSI-open-source. These are reference/source fingerprints, not malware hashes or observed hostile installations. Confidence covers pinned source or byte identity; broad negative-control specificity and runtime efficacy have not been measured. The pre-existing hostname `strix.loupes.com.cn` is not attributed to Strix by its name.

## Aaj Tak article and circular evidence

[Aaj Tak's 11 November article](https://www.aajtak.in/crime/cyber-crime/story/ai-agents-cyber-attack-banks-fintech-i4c-cert-in-advisory-pvzs-rpti-2693594-2026-11-11) names this project and repeats its 5,884-IP/60-country baseline. This downstream mention provides no independent telemetry. It cautions against equating IPs with active agents. No exact network/file IOC was found in the reviewed article body, so no IOC is admitted from it.

[CERT-In CIAD-2026-0058, 4 November](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES02&VLCODE=CIAD-2026-0058), independently supports the BFSI campaign/tool context. Detailed infrastructure fingerprints and detection rules remain in restricted advisories. The media article does not connect this inventory's individual addresses to that campaign.

## Collection limits

Only public reporting and pinned official source bytes were reviewed. No candidate host requests, DNS resolutions, sample execution, paid-provider queries or Censys MCP calls were made. Existing sources were checked for overlap; the retained backlog includes SecFlow campaign reporting. This is a bounded research delta, not an exhaustive internet census. Hashes identify the stated artifacts; source publication, source revision and enrichment times are distinct from attack activity.
