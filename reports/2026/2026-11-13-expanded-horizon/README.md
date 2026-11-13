# AI Attacker Threat Research — 13 November 2026 expanded review

Reviewed additions: **145 source/analysis records**, **143 new master type/value entries** and **2 corroborations**. The latter include independently derived facts where noted. These totals span evidence classes, not malicious servers.

| Evidence class | Records |
|---|---:|
| report-artifact-observables | 40 |
| shared-services-and-generic-markers | 6 |
| sourced-iocs | 53 |
| software-fingerprints | 16 |
| supporting-context | 7 |
| report-host-network-artifacts | 15 |
| deployment-leads | 2 |
| artifact-derived-observables | 4 |
| sample-derived-observables | 2 |

[All records (CSV)](indicators.csv) · [Full provenance (JSON)](records.json). Category CSVs use the evidence-class filenames above.

This review adds historical primary-source backfill and separates framework abuse, AI-related malware, software identification and infrastructure leads. Retrieval on 13 November does not make the underlying incidents new. Source publication dates and per-indicator observations remain separate; missing observation dates stay blank.

ThreatDown's [CARBONATO investigation](https://www.threatdown.com/blog/carbonato/) supplies campaign infrastructure and contextual host artifacts. It describes an unchanged Nous Research Hermes installation receiving a malicious persona. The legitimate agent package is not a malicious-file indicator. Withheld registry addresses were not inferred, and common service filenames require correlation.

[Hunt's Thailand Ministry of Finance investigation](https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent) distinguishes staging, Hades C2, an SSH client and a certificate-only lead. Its VShell samples were staged; use against the ministry was unproven. One purported SHA256 has only 63 hexadecimal characters and was excluded without repair. Certificate hashes remain separate from malware hashes.

[Unit42's BUGSTER report](https://unit42.paloaltonetworks.com/ai-assisted-cybercrime-analysis/) explicitly links the actor's server to Hermes and a C2 listener, while reporting criminal activity primarily against India. This establishes campaign-level India context, not indicator-specific proof of traffic to an Indian victim. The separately listed commercial proxy remains supporting infrastructure. [Earlier Unit42 reporting](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/) directly links the NousResearch upstream; this supports project-level reported abuse without identifying a campaign build revision or resolving Gambit's separate identity gap.

The separate malware index retains LAMEHUG/PROMPTSTEAL runtime-model use, PromptSpy's research qualification, VoidLink development evidence, likely AI assistance in FunkSec, and delivery/branding distinctions for other sample groups. ESET's associated hash lists represent artifacts across several algorithms, not an inflated sample count. Shared model-provider domains, credentials, victim details and ambiguous research-group hashes are excluded.

These are reviewed external findings. Independent static analysis, where admitted, is labeled separately and proves byte/configuration content rather than observed first-party network activity. No sensor collection, target probing, current liveness validation or comprehensive internet coverage is claimed. Supporting artifacts and deployment leads must not be merged into an automatic block list.

ThreatDown displays 22 September 2026 while its publication metadata says 23 September; both are retained. Unit42 describes seven FunkSec variants but lists eight FunkSec hash rows; exact rows are retained without inventing a reconciliation.

[Our bounded VoidLink native analysis](../../../research/analyst-derived/2026-11-13-voidlink/README.md) records a sample default distinct from the published infrastructure port. No current connection or victim telemetry is claimed.

| Observable (defanged) | Class | Role | Source date | Confidence | Source |
|---|---|---|---|---|---|
| 54[.]67[.]2[.]84 | report-artifact-observables | Hardcoded VNC C&C configuration in analyzed PromptSpy; no field infection proven | 2026-02-19 | High | [Source](https://www.welivesecurity.com/en/eset-research/promptspy-ushers-in-era-android-threats-using-genai/) |
| m-mgarg[.]com | report-artifact-observables | Publisher-reported phishing/brand-impersonation website associated with analyzed distribution chain | 2026-02-19 | High | [Source](https://www.welivesecurity.com/en/eset-research/promptspy-ushers-in-era-android-threats-using-genai/) |
| mgardownload[.]com | report-artifact-observables | Publisher-reported PromptSpy dropper distribution website according to VirusTotal | 2026-02-19 | High | [Source](https://www.welivesecurity.com/en/eset-research/promptspy-ushers-in-era-android-threats-using-genai/) |
| 52[.]222[.]205[.]45 | shared-services-and-generic-markers | Historical hosting IP listed alongside phishing website; ownership/exclusive malicious use unproven | 2026-02-19 | Low | [Source](https://www.welivesecurity.com/en/eset-research/promptspy-ushers-in-era-android-threats-using-genai/) |
| 104[.]21[.]91[.]170 | shared-services-and-generic-markers | Historical Cloudflare hosting IP listed alongside distribution website; shared edge not malicious wholesale | 2026-02-19 | Low | [Source](https://www.welivesecurity.com/en/eset-research/promptspy-ushers-in-era-android-threats-using-genai/) |
| stayathomeclasses[.]com | sourced-iocs | Analyzed LAMEHUG HTTP(S) exfiltration endpoint host; described as compromised hosting by other reporting | 2025-09-25 | High | [Source](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html) |
| stayathomeclasses[.]com/slpw/up[.]php | sourced-iocs | LAMEHUG exfiltration endpoint as scheme-less publisher text | 2025-09-25 | High | [Source](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html) |
| 144[.]126[.]202[.]227 | sourced-iocs | LAMEHUG/PROMPTSTEAL hardcoded SSH exfiltration destination | Unknown | High | [Source](https://www.sentinelone.com/labs/prompts-as-code-embedded-keys-the-hunt-for-llm-enabled-malware/) |
| 8[.]149[.]128[.]10 | report-artifact-observables | Publisher-reported historical C2 server | 2026-01-16 | High | [Source](https://www.sysdig.com/blog/voidlink-threat-analysis-sysdig-discovers-c2-compiled-kernel-rootkits) |
| 8[.]149[.]128[.]10:8080 | report-artifact-observables | Publisher-reported historical C2 endpoint | 2026-01-16 | High | [Source](https://www.sysdig.com/blog/voidlink-threat-analysis-sysdig-discovers-c2-compiled-kernel-rootkits) |
| 45[.]79[.]183[.]61 | sourced-iocs | C2 hub | 2026-09-22 | High | [Source](https://www.threatdown.com/blog/carbonato/) |
| 91[.]99[.]195[.]164 | sourced-iocs | Historical fsociety-era C2 | 2026-09-22 | High | [Source](https://www.threatdown.com/blog/carbonato/) |
| 213[.]136[.]79[.]115 | sourced-iocs | Beacon / reverse-shell endpoint; reported ports 8080 and 4444 | 2026-09-22 | High | [Source](https://www.threatdown.com/blog/carbonato/) |
| 213[.]136[.]83[.]197 | sourced-iocs | Operator LLM gateway; source reported live Sep 3, 2026 | 2026-09-22 | High | [Source](https://www.threatdown.com/blog/carbonato/) |
| 190[.]211[.]124[.]187 | sourced-iocs | Reverse-tunnel sink | 2026-09-22 | High | [Source](https://www.threatdown.com/blog/carbonato/) |
| carbonato-proxy-drab[.]vercel[.]app | sourced-iocs | Campaign LLM proxy, source reported suspended | 2026-09-22 | High | [Source](https://www.threatdown.com/blog/carbonato/) |
| carbonato-proxy-zeta[.]vercel[.]app | sourced-iocs | Campaign LLM proxy, source reported suspended | 2026-09-22 | High | [Source](https://www.threatdown.com/blog/carbonato/) |
| carbonato-proxy-zeta-2[.]vercel[.]app | sourced-iocs | Campaign LLM proxy, source reported suspended | 2026-09-22 | High | [Source](https://www.threatdown.com/blog/carbonato/) |
| 162[.]243[.]3[.]92 | sourced-iocs | Actor server hosting Hermes, C2 listener, Cursor IDE proxy and supporting services | 2026-10-21T14:00:24Z | High | [Source](https://unit42.paloaltonetworks.com/ai-assisted-cybercrime-analysis/) |
| 104[.]238[.]38[.]202 | supporting-context | Commercial proxy server used by actor | 2026-10-21T14:00:24Z | Medium | [Source](https://unit42.paloaltonetworks.com/ai-assisted-cybercrime-analysis/) |
| 43[.]246[.]208[.]207 | sourced-iocs | Staging/open directories; Hades Windows hardcoded C2 on 443; VShell payload hosting on 21083 | 2026-07-23 | High | [Source](https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent) |
| 103[.]97[.]0[.]57 | supporting-context | SSH CLIENT address in recovered Hermes configuration, not C2 | 2026-07-23 | Medium | [Source](https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent) |
| 118[.]107[.]222[.]232 | deployment-leads | Certificate-related host only; exact malicious service or operational role unproven | 2026-07-23 | Low | [Source](https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent) |
| 202[.]181[.]27[.]115 | sourced-iocs | Hades Linux hardcoded C2 on 12443, plus certificate overlap | 2026-07-23 | High | [Source](https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent) |
| redhatupdating432[.]dnsrd[.]com | deployment-leads | Historical domain on staging IP, predating observed operation | 2026-07-23 | Low | [Source](https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent) |
| code[.]newcli[.]com | supporting-context | Third-party AI proxy used for limited Claude connectivity tests and configured Codex access | 2026-07-30T10:00:52Z | Low | [Source](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/) |
| 8[.]149[.]128[.]10 | sample-derived-observables | Compiled default C2 host in exact VoidLink implant 4c4201 | 2026-01-13 | High | [Source](https://research.checkpoint.com/2026/voidlink-the-cloud-native-malware-framework/) |
| 8[.]149[.]128[.]10:443 | sample-derived-observables | Compiled default C2 host/port pair in exact VoidLink implant 4c4201 | 2026-01-13 | High | [Source](https://research.checkpoint.com/2026/voidlink-the-cloud-native-malware-framework/) |
