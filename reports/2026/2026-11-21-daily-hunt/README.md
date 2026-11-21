# Extended global hunt and exact ARTEX backdoor evidence

**21 November 2026**. This pass adds **559 reviewed source memberships**: **82 our artifact derivations** and **477 externally sourced memberships**. Exact deduplication adds **500 type/value pairs** to the master; **59 memberships** supply evidence for values already present or added by another source in this run. These totals include contextual artifacts and software references, not just malicious infrastructure.

## Our reproducible findings

- [Exact trojanized ARTEX binary](../../../research/analyst-derived/2026-11-21-artex-trojanized-artifact/README.md): hash-verified 51,210,988-byte ELF; 13 selected functions reconstructed. Native code confirms the public login-to-shell branch before credential validation, with a configured database handle required. No console was contacted. Eight memberships corroborate seven existing values and add one UI asset identity; the shared favicon remains a software reference.
- [Nine LeadStack npm archives](../../../research/analyst-derived/2026-11-21-leadstack-exact-artifacts/README.md): SHA256, registry SHA1 and npm SHA512 integrity verified, with TAR/member and byte locators. Thirty-eight memberships include 28 values also reported in the separate external packet and ten additional values. Legitimate Hermes Agent is distinct from its unauthorized installation.
- [Ten PHP2Shell campaign scripts](../../../research/analyst-derived/2026-11-21-socradar-exact-artifacts/README.md): 36 memberships from exact source-backed artifacts, including a newly cataloged configured endpoint on port 42283. The SSH remote-forward listener on 43402 is not an outbound SSH destination port. This separate campaign has no established ARTEX/CyberStrikeAI association.

Our derivations contribute **32 values beyond both the prior master and this run's external rows**. Other own memberships corroborate previously known or concurrently reported values. Independent analysis of public artifacts is distinct from first-party collection: **no owned attack sensor is deployed**. No new independently verified malicious C2 IP or current live C2 was established.

## Aggregation and evidence classes

| Publication class | Added memberships |
|---|---:|
| sourced-iocs | 50 |
| software-fingerprints | 17 |
| shared-services-and-generic-markers | 11 |
| report-artifact-observables | 118 |
| deployment-leads | 38 |
| campaign-context | 248 |
| sample-derived-observables | 77 |

The [primary-source context](primary-source-context.json) details the reporting packets. Additional originals include [Bitrise](https://bitrise.io/artex-incident-report), [Chainstack](https://chainstack.com/security-incident-nov-2026/), [Dragos](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens) and [DIVD](https://www.divd.nl/hacked/). Roles and dates remain per-record in [JSON](records.json) and [CSV](records.csv). Original source publication, observed activity, archive acquisition and local review timestamps are not interchangeable.

Bitrise's three well-supported incident sources are separated from weak hosting/name-only candidates, which remain private. Chainstack's five IPs retain source, relay, beacon and delivery roles by endpoint; its eight hashes identify modified application/test files, not the unacquired second stage. Dragos's ARTEX client strings date key-use observations, not the original provider compromises. WorkOS's follow-up describes an unintended researcher benchmark escape; it does not establish a malicious operator or exonerate an unrelated incident sharing an address.

The broader reporting covers BabidiGhost, ArgonHunt, BOSSAI, KeyHunter, XaocMail, n0n, INC/Gentlemen workbench, LeadStack, Agent Framework and historical AI-analysis evasion. Each keeps its own AI-involvement scope. A source's operator claims, staged packages, planned withdrawals and ransom demands do not establish successful compromise, execution or payment. Two checksum-invalid original address/endpoint strings and a malformed 63-character hash were withheld without repair.

## Map, tools and remaining gaps

The selected overview adds **62 IPs**, projecting **6,687 unique IPs** across evidence classes. A new address can be a software deployment lead, reported incident source or historical campaign host. Our independently parsed LeadStack IP also appears in the external packet and is counted once. Source roles and score ceilings are preserved; enrichment never raises a score. See the [main CSV](../../../data/ip-overview.csv) and [interactive map](https://ella-bakshi.github.io/ai-attacker-threat-research/).

The [tool index](../../../tools/README.md) now contains **57 identities**, with 14 newly indexed in this pass and scoped CyberStrikeAI release metadata. A meaningful ARTEX derivative remains a fork resource, not another counted identity. The [source and methods directory](../../../docs/research-source-directory.md) adds national advisories, independent creators, public collections, canary studies and newer research methods, with licensing and validation limits.

All **35 prior unresolved relationships** remain in a [separate carry-forward view](remaining-unverified.csv); canonical historical review dates are retained. All **25 private Censys leads** still lack a sufficient independent public admission bridge. Newly accepted literal IPs have no exact overlap with those leads. A later software sighting, copied list or shared hosting relationship does not resolve an earlier campaign attribution.

The exact encrypted BLOODALCHEMY payload remains missing; the human-verified YARAify result reports that hash absent from its corpus. Exact requested CyberStrikeAI campaign samples remain acquisition gaps; Triage download access was blocked and deferred. Eight newly reported wheel/webshell seeds and seven DXSCAN seeds had no match in 89 retained inventory files containing 54,506 listed entries. This is a finite corpus comparison, not a statement that samples do not exist elsewhere. Missing source windows and unpublished artifacts remain in the private backlog.

The reporting lane alone processed 51 search query strings and 31 scripted source-URL attempts, alongside the other source, repository and artifact lanes. Discovery indexes and translations were followed to underlying reports; they were not counted as independent corroboration. Coverage emphasizes 13–21 November with linked historical backfill. No all-internet or publisher-wide completeness is claimed, and the global cutoff has not been advanced past unfinished windows.

**Zero Censys or paid-provider calls, candidate probes, DNS lookups, sample submissions or malware execution.** Local licensed IPtoASN/DB-IP Lite enrichment supplies approximate hosting metadata with snapshot provenance. Public tests, repository checksum manifests, raw articles/binaries and internal review receipts were not added. The existing interface, geography, attribution and separated build/commit/Pages workflow are retained. The scheduled hunt remains paused; this was a manual run.
