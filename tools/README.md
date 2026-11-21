# AI security tooling index

Updated **21 November 2026**. This registry covers **57 project identities**, including fourteen added on 21 November, one on 16 November, nine on 15 November and ten on 13 November. Earlier pinned source revisions remain historical inspected references. It includes dedicated security agents, AI-assisted auditing, conventional reconnaissance and adjacent general agents. A project's presence here does not establish maliciousness or a hostile deployment. Capabilities are upstream descriptions, not executed or independently benchmarked results.

[Full JSON](tool-registry.json) · [Importable CSV](tool-registry.csv) · [Our source identification hypotheses](source-identification-hypotheses.json)

Each entry records its owner, aliases, pinned revision, documentation/resources, latest visible release, activity date and meaning, license qualifications, AI-feature assessment, lifecycle evidence and narrowly scoped abuse reporting. Documentation byte hashes identify the inspected source; they are not malware hashes or runtime deployment detectors. This registry is separate from IOC totals and does not add map locations.

## Established projects

| Project and source | What it does, according to its maintainer | Latest visible release |
|---|---|---|
| [ARTEX](https://github.com/BaaRai/ARTEX) | Go/Next.js multi-agent penetration-testing platform with planning, tool execution and optional offensive workflows. | [v0.7.0](https://github.com/BaaRai/ARTEX/releases/tag/v0.7.0) (2026-11-21) |
| [CyberStrikeAI](https://github.com/AIPentest/CyberStrikeAI) | Security automation workspace combining agent planning, MCP tools, human oversight, evidence, workflows and optional C2 capabilities. | v1.8.1 (2026-11-19) |
| [PentAGI](https://github.com/vxcontrol/pentagi) | Self-hosted multi-agent penetration-testing system using LLMs and conventional security tools. | v2.2.0 (2026-10-05) |
| [AutoCVE](https://github.com/larlarua/AutoCVE) | Multi-agent source auditing and vulnerability verification/reporting platform with sandboxed tool workflows. | v1.0.5 (2026-07-12) |
| [HexStrike AI](https://github.com/0x4m4/hexstrike-ai) | MCP-oriented security automation framework exposing conventional assessment tools to AI clients. | No GitHub release found |
| [Strix](https://github.com/usestrix/strix) | Autonomous application-testing agents described as combining runtime assessment and vulnerability verification. | v1.7.1 (2026-11-10) |
| [PentestGPT](https://github.com/GreyDGL/PentestGPT) | LLM-driven penetration-testing research/tooling with separate legacy and autonomous agent interfaces. | v1.0.0 (2025-12-24) |
| [CAI](https://github.com/aliasrobotics/cai) | Archived framework for building specialized AI security-testing agents. | No GitHub release found |

## Indexed on 12 November 2026

| Project and source | What it does, according to its maintainer | Latest visible release |
|---|---|---|
| [ARL community backup](https://github.com/Aabyss-Team/ARL) | Asset enumeration, service identification and exposure inventory in a community copy of the original ARL project. | 2.6.3 (2025-03-04) |
| [ARL-Next](https://github.com/owl234/ARL-Next) | ARL-derived platform with asynchronous scan orchestration, asset investigation and an MCP interface for AI clients. | [v1.5.1](https://github.com/owl234/ARL-Next/releases/tag/v1.5.1) (2026-11-21) |
| [Scope Sentry](https://github.com/Autumn-27/ScopeSentry) | Distributed asset mapping, subdomain, leakage, vulnerability and directory scanning with page monitoring. | v1.9.4 (2026-08-23) |
| [Nemo](https://github.com/hanc00l/nemo_go) | Distributed reconnaissance platform covering domains, IPs, services and website assets. | v3.2.1 (2026-02-09) |
| [XingRin](https://github.com/yyhuni/xingrin) | Self-hosted distributed asset discovery, scanning, search and result-management platform. | v1.5.8 (2026-01-11) |
| [LunaFox](https://github.com/yyhuni/lunafox) | Next-generation self-hosted ASM platform with runtime/engine components and distributed workers, linked as XingRin successor. | v0.0.1-alpha.240 (2026-11-01) |
| [OpenEASD](https://github.com/cybersecify/OpenEASD) | External-surface discovery and scan orchestration with findings, monitoring and prioritization. | v3.0.1 (2026-10-14) |
| [DeepAudit](https://github.com/lintsinghua/DeepAudit) | Multi-agent source-code security analysis with sandbox verification and reporting, as described by its maintainers. | v3.0.4 (2026-01-24) |
| [AIxVuln](https://github.com/m4xxxxx/AIxVuln) | LLM-directed vulnerability discovery and verification with function calling and Docker sandboxes. | v1.3 (2026-03-14) |
| [AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) | Security assessment of AI infrastructure, agents, MCP tools, skills and model interfaces. | [v4.6.11](https://github.com/Tencent/AI-Infra-Guard/releases/tag/v4.6.11) (2026-11-19) |
| [AutoHunter (Chris-biu)](https://github.com/Chris-biu/AutoHunter) | AI-orchestrated vulnerability-testing platform integrating conventional assessment tools and scope controls. | No GitHub release found |
| [Cairn](https://github.com/oritera/Cairn) | General state-space search harness demonstrated by maintainers for autonomous penetration testing. | v0.2.1 (2026-05-10) |
| [Shannon](https://github.com/KeygraphHQ/shannon) | Source-informed web/API assessment that uses browser and command-line actions to validate findings, per upstream documentation. | [v3.6.1](https://github.com/KeygraphHQ/shannon/releases/tag/v3.6.1) (2026-11-20) |
| [Agent Zero](https://github.com/agent0ai/agent-zero) | General agent with a Linux workspace, terminal, browser and desktop capabilities. | [v2.16](https://github.com/agent0ai/agent-zero/releases/tag/v2.16) (2026-11-17) |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Persistent general agent with tool use and extensible skills, relevant as an orchestration substrate to monitor. | [v0.23.3](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.3) (2026-11-20) |

[ARTEX source/fork review](artex-source-review.md): three historical-record annotations, four meaningful fork resources and three source-verified fork UAs; no malicious IOC count change.

## Added on 13 November 2026

| Project and source | Maintainer-described purpose | Latest visible release |
|---|---|---|
| [RedAmon](https://github.com/samugit83/redamon) | Self-hosted assessment agents organize findings in a graph and propose remediations, with documented approval gates. | [v7.9.0](https://github.com/samugit83/redamon/releases/tag/v7.9.0) (2026-11-19) |
| [Decepticon](https://github.com/BitterSecurity/Decepticon) | Agent framework for orchestrating red-team assessment workflows and security-tool interactions. | v2.2.2 (2026-10-28) |
| [PentestAgent](https://github.com/GH05TCREW/pentestagent) | Agent-based black-box security testing with workflows for authorized assessments and bug-bounty research. | No GitHub release found |
| [Cybermes](https://github.com/Zyrexnn/Cybermes) | Security-focused harness combining a Hermes engine, specialized skills and model/tool orchestration. | v3.5.1 (2026-11-13) |
| [Xalgorix](https://github.com/xalgorix/xalgorix) | Agent-driven assessment orchestration with reconnaissance, finding review and a web interface. | [v4.6.200](https://github.com/xalgorix/xalgorix/releases/tag/v4.6.200) (2026-11-21) |
| [AIRecon](https://github.com/pikpikcu/airecon) | Local-model reconnaissance/assessment assistant paired with a Kali-based container environment and terminal interface. | 0.1.7-beta (2026-04-03) |
| [RAPTOR](https://github.com/gadievron/raptor) | Claude Code configuration and security workflows for analysis, research and assessment of authorized artifacts. | v3.1.0 (2026-09-07) |
| [CyberStrike](https://github.com/CyberStrikeus/CyberStrike) | Agent-oriented security-testing harness with specialized workflows and integrations. | v2.0.1-beta.3 (2026-11-10) |
| [ScopeWeaver](https://github.com/cskwork/scopeweaver) | ARTEX-derived platform with English/Korean interface and message localization, retaining upstream provenance. | v0.9.1 (2026-11-04) |
| [AntiFox](https://github.com/AntiFox-AI/antifox) | ARTEX-derived multi-agent assessment platform focused by its maintainers on reproducible evidence and report delivery. | v2.0.3 (2026-10-30) |

AntiFox and ScopeWeaver have pinned ARTEX lineage. CyberStrike is a separate project from CyberStrikeAI. Cybermes acknowledges NousResearch Hermes as its core; this is a software relationship, not a campaign attribution bridge. RAPTOR has MIT text despite GitHub NOASSERTION metadata. The AI-Infra-Guard source fingerprints refer to their inspected source revision.

## Emerging projects and identity cautions

- **XingRin → LunaFox:** an upstream-linked successor, with a dated alpha prerelease. LunaFox's public GPL projection excludes a closed Agent; it is not a wholly open-source product. A release is not a maturity or runtime-quality assessment.
- **ARL, Scope Sentry and XingRin:** conventional reconnaissance in the inspected sources. ARL-Next documents AI/MCP integration, Nemo LLM reports/MCP, and OpenEASD optional AI analysis disabled by default. These different capabilities are not interchangeable.
- **ARTEX:** BaaRai is the designated English fork, with Autumn-27 lineage stated in its README; GitHub's `fork` flag alone misses that relationship.
- **ThreatBook enterprise editions:** ThreatBook lists ARTEX Pro Enterprise and CyberStrikeAI Enterprise as commercial RedAgents offerings. In response to the FBI FLASH, ThreatBook CEO Feng Xue says the ARTEX Pro mentioned in the advisory differs from the company’s cloud-only enterprise edition. Campaign attribution follows the framework identified in each incident report. [RedAgents product listings](https://redagents.ai/) · [ThreatBook CEO statement](https://www.linkedin.com/posts/secway_threatbooks-statement-on-the-fbi-flash-activity-7528623058979405824-HRPp)
- **CAI and Cairn are separate projects.** CAI is archived and has mixed licensing. No exact campaign-generating revision is established by an upstream identity review.
- **Hermes:** Separate [CARBONATO](https://www.threatdown.com/blog/carbonato/) and [Hunt Thailand](https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent) reporting establishes abuse of the NousResearch project. Exact campaign revisions remain unknown; this does not resolve Gambit's separate identity gap or classify legitimate installations as malicious.
- **Licenses:** Scope Sentry remains unresolved; AI-Infra-Guard has additional README attribution instructions alongside Apache-2.0 metadata. AutoHunter and Agent Zero contain MIT texts despite GitHub's NOASSERTION metadata. DeepAudit's closed-version claimed findings must not be assigned to the public release.
- **SecFlow:** the actor orchestration framework's exact public source remains unresolved. The unrelated defensive `aradhyacp/SecFlow` is not substituted based on its name.

## Independently derived source hypotheses

[Two JSON hypotheses](source-identification-hypotheses.json) · [CSV](source-identification-hypotheses.csv)

Cairn's hypothesis combines its root HTML title, Alpine initialization, named function, local-storage key and icon path at a pinned revision. Shannon's combines its exact package/CLI identity with the npx-mode state paths; it is a local software pattern, not an HTTP detector. Source bytes and cited line locators were independently checked.

Both remain **untested runtime hypotheses**, separate from the admitted IOC catalog and its counts. High confidence refers to source presence only. No live deployment, malicious use, campaign-generating revision or empirical false-positive rate was established. Five incomplete/default synthetic controls were rejected; these are not benign deployment measurements or broad negative-control validation. Generic titles, framework routes and directory names alone are insufficient. No target requests, DNS resolution, installation or source execution occurred.

Primary ecosystem context: [Unit 42](https://unit42.paloaltonetworks.com/artex-and-ai-powered-red-teaming-tools/), [GTIG](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks), [NorForge](https://norforge.com/blog/inside_cairn). Exact tool-specific sources and confidence limits remain in each registry entry.

## 15 November additions and releases

Four projects are new to this index; their release dates are historical. No malicious IOC or runtime-fingerprint claim follows from inclusion.

| Project | Maintainer-described scope | License | Release reference |
|---|---|---|---|
| [Fennec](https://github.com/Fennec-AI/Fennec) | Multi-agent web/API security assessment with a dashboard and local execution runner. | Apache-2.0 | [v0.2.0](https://github.com/Fennec-AI/Fennec/releases/tag/v0.2.0) (2026-06-30) |
| [PenPard](https://github.com/penpard/penpard) | LLM-driven web/mobile assessment assistant integrating Burp Suite and mobile analysis tools. | PolyForm-Noncommercial-1.0.0 | [1.0.1](https://github.com/penpard/penpard/releases/tag/1.0.1) (2026-02-12) |
| [AIDA](https://github.com/Vasco0x4/AIDA) | Security assessment agent with an MCP service, scoped projects and a web dashboard. | AGPL-3.0 | [v1.1.0](https://github.com/Vasco0x4/AIDA/releases/tag/v1.1.0) (2026-04-15) |
| [Pentest Swarm AI](https://github.com/Armur-Ai/Pentest-Swarm-AI) | Agent orchestration for API/web assessment, recon, classification, validation and reporting. | AGPL-3.0-only | [v0.3.7](https://github.com/Armur-Ai/Pentest-Swarm-AI/releases/tag/v0.3.7) (2026-10-30) |

PenPard is source-available with noncommercial terms, not OSI open source. AIDA and Pentest Swarm AI are indexed at their owning upstreams; discovered forks are retained as relationship evidence rather than extra tools. Maintainer claims have not been executed or benchmarked. Pinned documentation hashes identify the reviewed text, not a deployment.

Release metadata updates: [AIPentest/CyberStrikeAI](https://github.com/AIPentest/CyberStrikeAI/releases/tag/v1.8.0) v1.7.24 → v1.8.0, [owl234/ARL-Next](https://github.com/owl234/ARL-Next/releases/tag/v1.4.6) v1.4.5 → v1.4.6, [samugit83/redamon](https://github.com/samugit83/redamon/releases/tag/v7.8.0) v7.5.1 → v7.8.0, [Zyrexnn/Cybermes](https://github.com/Zyrexnn/Cybermes/releases/tag/v3.5.1) v3.5.0 → v3.5.1, [xalgorix/xalgorix](https://github.com/xalgorix/xalgorix/releases/tag/v4.6.193) v4.6.187 → v4.6.193. Historical source pins remain unchanged.

## Additional source-review identities

These entries verify software identity. Reported abuse, where available, has its own source and scope. Exact campaign revisions and deployed bytes remain unknown. Earlier pins and release-review history are preserved.

| Project and source | Source/identity qualification | Latest visible release |
|---|---|---|
| [sapper-v2](https://github.com/N1nEmAn/sapper-v2) | Competition-oriented multi-agent assessment orchestrator; benchmark/championship claims remain maintainer assertions. | v18-champion (2026-11-01) |
| [HalberdStrike](https://github.com/kuaiyelink/HalberdStrike) | LLM assessment harness; PenTestGPT-inspired design is a maintainer claim, not independently verified code lineage. | No GitHub release found |
| [Bulwark](https://github.com/bulwark-sec/bulwark) | Pinned LICENSE/top badges say AGPL-3.0; README footer claims Apache-2.0. Conflict unresolved. | v5.26.0 (2026-06-10) |
| [0security](https://github.com/0sec-labs/0security) | Canonical repository now `0sec-labs/0security`; the old `0` alias verified. Both license files checked; disclosure totals unverified. | [v0.41.0](https://github.com/0sec-labs/0security/releases/tag/v0.41.0) (2026-11-20) |
| [DarkMoon](https://github.com/ASCIT31/Dark-Moon) | Upstream-described autonomous local-LLM assessment framework and privacy gateway; source/runtime/benchmark claims remain distinct. No malicious use established. | [v1.6.0](https://github.com/ASCIT31/Dark-Moon/releases/tag/v1.6.0) (2026-10-25) |

Acronis [reports HalberdStrike use in BOSSAI operations](https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/). The reported owner/name match the indexed upstream; the exact deployed revision, modifications and bytes remain unknown. The report describes operator-mediated transfers of reconnaissance reports, not direct autonomous communication between those agents.

DarkMoon is new to this registry on 15 November; its public release date is historical. Its [pinned README](https://github.com/ASCIT31/Dark-Moon/blob/edfe9cb12a263036a0c3dc1af604713e8197cce9/README.md), owning-repository metadata, full GPLv3 source-edition [license](https://github.com/ASCIT31/Dark-Moon/blob/edfe9cb12a263036a0c3dc1af604713e8197cce9/LICENSE) and release metadata were inspected. Capabilities and privacy-gateway behavior were not executed, independently benchmarked or security validated; the separately marketed Pro edition was not assessed. Inclusion adds no malicious IOC, deployment location or validated runtime fingerprint.

## Added on 16 November 2026

| Project and source | Maintainer-described purpose | Latest visible release |
|---|---|---|
| [LuaN1aoAgent](https://github.com/SanMuzZzZz/LuaN1aoAgent) | TypeScript/Pi-SDK assessment agents with separate planning, execution and observation roles and durable evidence graphs. | v2.0.0 (2026-07-20) |

The inspected v2 is a rewrite of the historical Python v1. Capabilities and scope controls are static documentation claims; neither runtime enforcement nor v1 benchmark transfer was validated. Cloudflare names the project in its AI-orchestrator survey without linking a particular source revision to a malicious deployment. This registry entry adds no malicious IOC or map location.

ARTEX resource review on 16 November: [Global Edition tagged source](https://github.com/jiwoochris/artex-global/tree/d6964594a0221cd921b85056d604bce9d8ce54df), version `v0.3.15-global.1`, is a separately qualified AGPL-3.0 fork. [Static evidence](../research/software-fingerprints/2026-11-16-artex-global-source/README.md) adds software references; it establishes no malicious deployment or equivalence to every ARTEX fork.

## Added on 21 November 2026

Six identities extend the research index. They are historical research/maintainer projects newly indexed here, with no malicious IOC, hostile deployment or performance claim.

| Project | Scope and qualification | Root license | Latest repository release metadata |
|---|---|---|---|
| [Antares](https://github.com/enowdev/antares) | Maintainer-described Go agent workspace with specialist security roles, browser and shell tools, evidence/reporting, memory/RAG and scoped assessment workflows. | Apache-2.0 | [v0.8.0](https://github.com/enowdev/antares/releases/tag/v0.8.0) (2026-11-14) |
| [PentestAgent (research implementation)](https://github.com/nbshenxm/pentest-agent) | Research implementation separating reconnaissance, planning and execution agents for intelligence gathering, vulnerability analysis and exploitation. | MIT | No GitHub releases present in reviewed collection |
| [VulnBot](https://github.com/KHenryAegis/VulnBot) | Research framework using LLM-coordinated reconnaissance, scanning and exploitation phases, task planning and optional retrieval augmentation. | MIT | No GitHub releases present in reviewed collection |
| [AutoPentester](https://github.com/YasodGinige/AutoPentester) | LLM agent research framework for iterative pentesting with configurable model providers, retrieval augmentation and repeated-result handling. | MIT | No GitHub releases present in reviewed collection |
| [MAPTA](https://github.com/arthurgervais/mapta) | Author-described multi-agent web application assessment with tool-grounded sandbox execution and a separate validation agent. | MIT | No GitHub releases present in reviewed collection |
| [BugTraceAI](https://github.com/BugTraceAI/BugTraceAI) | Maintainer-documented suite linking autonomous web/API assessment engines, an analyst dashboard, REST/MCP integrations and model resources. | Apache-2.0 | [demo-report](https://github.com/BugTraceAI/BugTraceAI/releases/tag/demo-report) (2026-02-18) — demonstration report, not software |

The research implementation **nbshenxm/pentest-agent** is distinct from the already indexed **GH05TCREW/PentestAgent**. AutoPentester retains a `pentestgpt` package and Grey_D MIT license notice; this package heritage is recorded without inventing an exact generating revision. MAPTA's inspected tree has no README; its author-owned description, pinned agent source and complete MIT license were reviewed. Antares explicitly describes an early release. BugTraceAI is one umbrella identity: independently deployable components and models may have their own versions and terms. Its parent repository's `demo-report` release must not be presented as the scanner's software version.

CyberStrikeAI release metadata is updated to **v1.8.1**, published **19 November 2026 at 08:47:08 UTC**, with its earlier review retained. The pinned source comparison remains historical; release publication does not identify a campaign's deployed version. No project, controller, installer, setup hook, benchmark or payload was executed, and no network IOC or map address follows from this registry update.

## Extended source review on 21 November 2026

Eight independently named source projects add creator and architecture coverage. These are source/documentation identities; no malicious IOC, target address, deployed version, safety guarantee or benchmark result is established by their inclusion. Older release dates below are historical backfill, not new November launches.

| Project | Maintainer-described role | Reviewed root license | Latest stable GitHub release metadata |
|---|---|---|---|
| [Pentest Anything](https://github.com/SammyYohan/Pentest-Anything) | Maintainer-described MCP server and CLI orchestrating Semgrep, Trivy, SQLMap and Nuclei, with local authorization scope, evidence and result handling. | [MIT](https://github.com/SammyYohan/Pentest-Anything/blob/6dc78fa718619f299fcb72413266fff2f4811941/LICENSE) | [v2.6.0](https://github.com/SammyYohan/Pentest-Anything/releases/tag/v2.6.0) (2026-11-17) |
| [Spider](https://github.com/xdisform/Spider) | Maintainer-described Claude Code prompt/skill harness coordinating reconnaissance, assessment, verification and reporting agents with shared engagement memory. | [MIT](https://github.com/xdisform/Spider/blob/db1a743c8d66fdefa751f5953f3f774531e90f8f/LICENSE) | No releases in reviewed GitHub collection |
| [Zazy Pentest Plugin for Claude](https://github.com/AnandJogawade/Zazy-Pentest-Plugin-for-Claude) | Maintainer-described Claude Code plugin for scoped security assessment, with prompt/skill libraries, a verification agent and recon-to-report commands. | [MIT](https://github.com/AnandJogawade/Zazy-Pentest-Plugin-for-Claude/blob/bbed10a77f6e973ac3670dfbefc9630afcc9b19f/LICENSE) | [v1.1.0](https://github.com/AnandJogawade/Zazy-Pentest-Plugin-for-Claude/releases/tag/v1.1.0) (2026-11-16) |
| [AutoPentest (wooluo)](https://github.com/wooluo/AutoPentest) | Maintainer-described FastAPI/Vue platform coordinating recon, asset mapping, scanning, AI validation and reports with optional Kali SSH execution and DNSLog verification nodes. | [MIT](https://github.com/wooluo/AutoPentest/blob/54262e8a5645cc85cc84e86e694f45bb5f542ce4/LICENSE) | No releases in reviewed GitHub collection |
| [ARES (Mafifrizi)](https://github.com/Mafifrizi/ARES) | Maintainer-described self-hosted engagement platform with module orchestration, attack-path graphs, scope controls, encrypted evidence storage, reporting and optional authorized LLM planning/MCP access. | [MIT](https://github.com/Mafifrizi/ARES/blob/369e7150b62352cdb809388ad32e9183775ae290/LICENSE) | [v6.0.0](https://github.com/Mafifrizi/ARES/releases/tag/v6.0.0) (2026-06-22) |
| [Ares (Dreadnode)](https://github.com/dreadnode/ares) | Maintainer-described Rust platform coordinating red-team worker agents and blue-team investigations against shared lab infrastructure, with trace/evidence collection and benchmark replay. | [MIT](https://github.com/dreadnode/ares/blob/786b2987bfeb08284b93802c3f533c54738e1e48/LICENSE) | [v0.3.0](https://github.com/dreadnode/ares/releases/tag/v0.3.0) (2026-05-18) |
| [PentestCode](https://github.com/s0ld13rr/pentestcode) | Maintainer-described terminal assessment agent with coordinated specialist agents, persistent engagement state, parsed tool outputs and configurable model providers. | [MIT](https://github.com/s0ld13rr/pentestcode/blob/b7db9ccbe83d62bd6ead8b57b6a1f5070e9a7fab/LICENSE) | [v0.2.7](https://github.com/s0ld13rr/pentestcode/releases/tag/v0.2.7) (2026-10-23) |
| [BreachWeave](https://github.com/m-sec-org/BreachWeave) | Maintainer-described Manager/Solver/Observer collaboration system with shared evidence and hypotheses; a separately pinned pentest branch adds project/asset planning, reports and activity replay. | [Apache-2.0](https://github.com/m-sec-org/BreachWeave/blob/bc2d9502a2625c5ef354adc30243bd091341cc51/LICENSE) | No releases in reviewed GitHub collection |

`Mafifrizi/ARES` and `dreadnode/ares` are distinct projects. `wooluo/AutoPentest` is distinct from `YasodGinige/AutoPentester`. PentestCode describes itself as an OpenCode hard fork; copied and similarly named repositories were not added as separate projects. BreachWeave's CTF `main` and enhanced `pentest` branches remain one identity, with separate documentation and license pins. Spider's complete root MIT text was checked despite GitHub's `NOASSERTION` metadata; provisioned tools keep their own licenses. Prompt/skill harnesses and scanner orchestration do not imply a separately validated model or autonomous runtime.

The existing ARTEX entry gains a qualified resource for [bcyw/ARTEX](https://github.com/bcyw/ARTEX), pinned at `47770f3c4038c9b794937ccc4b2d295b57de2f57`. Its README calls it a self-maintained derivative and reports substantive changes, including SQLite and removal of programmatic asset gates. This derivative is not counted as another registry identity. CyHawk's independent static-review post explicitly does not establish deployment or confirmed attacks, and the repository's versioning statements do not establish a published release: the reviewed GitHub release collection was empty.

All 49 earlier source pins and release-review history remain unchanged in this extension. Only ARTEX's `meaningful_fork_resources` list is appended; all its other fields remain intact. The previously reviewed CyberStrikeAI v1.8.1 release metadata and historical source pins are preserved. Deception labs, detection collections, commercial services and papers belong in the research source directory, with their own limitations and licenses.

## Stable release review on 21 November 2026

GitHub release records update nine entries: BaaRai ARTEX, Shannon, RedAmon, Xalgorix, Hermes Agent, Agent Zero, ARL-Next, AI-Infra-Guard and 0security. The registry records publication times in UTC, prior release metadata and the verified tag commits for BaaRai ARTEX and Shannon. The source pins identify the revisions inspected in earlier reviews. Campaign build and deployment status require their own evidence.
