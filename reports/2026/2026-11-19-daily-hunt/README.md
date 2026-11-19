# 19 November 2026: public labels, new reporting and exact artifacts

This pass adds **228 evidence memberships**, comprising **212 new distinct type/value pairs** and **16 corroborating memberships**. There are **13 own analysis memberships** and **215 externally sourced memberships**. The catalog becomes **13,058 canonical records** and **16,560 distinct master values**. These are mixed evidence classes, not counts of malicious systems.

## Censys labels and public evidence

Censys's ARTEX console fingerprint and threat-label query were already documented in its original **5 and 12 November** reporting. Their review on 19 November does not establish a new launch date. The [query guide](../../../docs/censys-threat-labels-and-queries.md) preserves the published syntax and qualifications: software matches can include authorized installations and copied/rebranded assets; a provider threat label is not proof of a malicious operator.

Four public-source memberships comprise a historical host corroboration, two published query references and one nonindicative DNS-context domain independently transcribed from a publisher figure. The figure is provider evidence, **not our first-party measurement**; its displayed reputation score is not inherited by our confidence rubric. Live Censys account results were not collected in this pass. Public documentation and publisher artifacts support these records; no commercial listing or account export is republished.

## New primary reporting

[Darktrace's 18 November investigation](https://www.darktrace.com/fr/blog/agentic-attacks-in-the-wild-inside-three-artex-investigations) adds historical role/date evidence. Existing `nginxmysql[.]com` and `45[.]153[.]126[.]223` are **BLOODALCHEMY C2**, not ARTEX controllers. New `213[.]111[.]150[.]145:8099` delivered wisp-agent on 5 November. New `43[.]98[.]196[.]73` was an Azure intrusion source on 20 October; that case had **no observed C2**. The new primary C2 observation raises the existing IP’s historical-role score from 55 to 70 and supplies an October 23–November 2 observation window; current operation remains unverified. Another existing address gains connection-attempt evidence. Five shared paste/file/tunnel services remain nonindicative at score 0; two appendix filename references have score ceiling 20 and no invented case mapping.

[huntback's 17 November report](https://huntback.io/blog/inside-cyberstrikeai-221-tool-executions-disabled-approval-gate) identifies `38[.]76[.]169[.]207` and TCP 8010 as a workspace file server. Its operator identity, testing authorization and victim compromise are unknown. Database/log hashes identify evidence artifacts, **not malware**, and the recorded session date is not used as a service sighting. These exposure/artifact references have score ceiling 20.

[ReversingLabs' 18 November notebook](https://www.reversinglabs.com/blog/threat-researchers-notebook-detection-strategies-for-artex-and-related-forks) supplies **184 ARTEX-family operator-binary SHA256s and nine favicon SHA256s**, kept as software fingerprints at 20. They are not 193 malicious-file findings or individual campaign attributions. The linked 3,096-host CSV returned HTTP 403; **zero attachment rows were acquired or imported**. See [source scope](source-review.md), [source identities](primary-source-context.json) and [GTIG context](gtig-context.md).

## Our exact-artifact work and source correction

The [separate analyst supplement](../../../research/analyst-derived/2026-11-19-exact-support-and-software-reference/README.md) records acquisition and bounded native/static work on **three exact public files**: a campaign supporting loader, its legitimate GameHook component, and a newly sourced ARTEX-family AArch64 controller reference. Locally recomputed digests and **30 selected native functions** support narrow identities and host markers; this is not complete whole-program decompilation. The ARTEX-family controller reference is dual-use software, with no malicious-operator assertion. There is no new independently verified malicious C2 IP, generated CyberStrikeAI campaign beacon or trojanized ARTEX campaign binary acquired in this pass. Raw binaries, executable material and decompiler projects remain private.

The current [FBI original PDF](https://www.ic3.gov/CSA/2026/261113.pdf) retains its printed **13 November** date but has **17 November revision metadata**. Its revised summary says **attempted sign-ins to more than 2,250 tenants**, replacing its earlier statement that access had been enabled. A source-citation number also changed. Neither change resolves the existing address discrepancy; the [scientific comparison](fbi-source-revision-review.json) preserves both file identities and date meanings.

## Remaining uncertainty and map

**All 35 unresolved relationships remain separate.** The [current-ID selection](remaining-unverified.csv) is carried forward with prior review times. This pass performed targeted checks of new sources, changed publisher material and new artifact routes; it does **not** claim that all 35 original sources were freshly re-reviewed.

After refresh, the selected inventory is **6,496 IPs**, adding exactly the three role-qualified addresses above; the **22 IPs with our analysis evidence remain unchanged**. New hashes, file markers and a nonindicative domain do not become resolved IPs. Scores 0/20/55/70 express scoped evidence strength, not probabilities of maliciousness or present-day operation. The existing interface, author credit, font and India-view geometry are preserved. The [map](https://ella-bakshi.github.io/ai-attacker-threat-research/) is a research inventory, not an automatic block list.

[Canonical records](records.json) · [CSV](records.csv) · [Software references](software-fingerprints.csv) · [Historical incident evidence](sourced-iocs.csv) · [Unresolved selection](remaining-unverified.csv)
