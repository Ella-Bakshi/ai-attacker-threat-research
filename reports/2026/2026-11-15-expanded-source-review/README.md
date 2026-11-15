# AI Attacker Threat Research — expanded source review, 15 November 2026

This global public-source expansion adds **331 externally sourced records** across distinct evidence classes. It includes historical backfill as well as recent reporting. The separately published [artifact-resolution supplement](../2026-11-15-evidence-resolution/README.md) adds seven independently derived values.

[All records CSV](records.csv) · [JSON](records.json) · [Deployment leads](deployment-leads.csv) · [Shared context](shared-context.csv) · [Prototype identities](prototype-context.csv)

| Source and evidence class | Records | Interpretation |
|---|---:|---|
| Cisco Talos — UAT-10147 campaign-associated indicators | 31 | 17 URLs, two IPs and 12 explicitly typed SHA-256 hashes; historical source-reported roles |
| Houdin — CyberStrikeAI deployment leads | 292 | Historical public IP/port software-fingerprint leads; hostile use unestablished |
| Houdin — shared-CDN context | 1 | A shared Cloudflare address without hostname/SNI cannot identify a dedicated installation |
| ESET — PromptLock research identities | 7 | Explicit SHA-1 identities with a publisher-assessed proof-of-concept qualification |

## Campaign reporting

[Cisco Talos's 20 August report](https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations/) documents UAT-10147's AI-assisted operations. The linked [pinned TXT list](https://github.com/Cisco-Talos/IOCs/blob/cdcef7d26efd578e5fe83cdd99141ad0dc73ad92/2026/08/UAT-10147%20integrates%20agentic%20AI.txt) and [STIX data](https://github.com/Cisco-Talos/IOCs/blob/cdcef7d26efd578e5fe83cdd99141ad0dc73ad92/2026/08/UAT-10147%20integrates%20agentic%20AI.json) agree on all admitted values; STIX explicitly labels the types and hash algorithms. Individual component roles remain unspecified where the source does not map them. The report distinguishes observed PentestGPT activity from DeepAudit presence and assessed intent. It does not establish that every listed file was AI-generated, or connect this campaign to ARTEX/CyberStrikeAI.

These 31 values are new to this repository's master, including two new literal IPs. No domain was resolved to manufacture a historical malicious-IP relationship. Unknown activity dates remain blank; source publication and STIX metadata are separate clocks.

[All 31 campaign-associated observables](talos-campaign-observables.csv) retain their category columns. Separate views contain [17 source-reported URLs](sourced-iocs.csv), [two campaign-context IPs](campaign-context.csv) and [12 report-associated file identities](report-artifact-observables.csv). Component identity or a publisher list membership alone does not establish that every supporting file is malicious or AI-generated.

## Historical software sightings

[Houdin's 29 September report](https://houdin.io/blog/mapping-200-undetected-chinese-ai-attack-platforms) discloses 280 host rows with a 24 September census cutoff. The public rows expand to **293 distinct literal IP/port pairs**, although the narrative says 295 indexed records. Only the disclosed pairs are retained; two missing records are not inferred. There are 187 new endpoint type/value pairs, 106 existing endpoint memberships and **156 IPs new to the selected inventory**.

The source's title/certificate signals are host-aggregate metadata, not independently verified matches at every listed port. Exact service observation times are unknown. Certificate issuance is not an installation or attack timestamp. Ten certificate-only leads have a written evidence ceiling of 10; other ordinary leads use 20. Shared-CDN context stays 0. A separate stronger source membership can retain its own score. These are ordinal evidence labels, not probabilities of maliciousness.

The source expressly offers its factual table as copyable CSV. This publication attributes the factual subset and adds our evidence qualifications; no separate open-data license is claimed, and no article, screenshot or commercial export is reproduced. The other-family ThreatFox/reputation annotations are excluded from our roles. A label on another service or the same IP is not proof of a malicious CyberStrikeAI operator.

## Research prototypes and methodology

[ESET's original PromptLock report](https://www.welivesecurity.com/en/ransomware/first-known-ai-powered-ransomware-uncovered-eset-research/) was published on 26 August 2025. Its 3 September update says an academic prototype closely resembles the samples, supporting a proof-of-concept interpretation. ESET had not observed actual attacks. The seven explicit SHA-1 identities are supporting research context; neither exact academic generating source nor active campaign attribution is claimed. [AI-related malware research index](../../../research/ai-related-malware/README.md).

[Harness's API-traffic study](https://www.harness.io/blog/an-artex-threat-hunt-across-customer-api-traffic) contributes methodology, with no new admitted incident endpoints: its actual source addresses are withheld. The study's search inputs are not evidence that those addresses appeared in the described incidents. [How this informs our independent collection](../../../docs/original-ioc-collection.md#lessons-from-the-expanded-public-source-review).

Search engines, primary publisher pages, linked IOC repositories and upstream project sources were used together. Duplicated summaries and snippets were not treated as corroboration. Some sources and provider pages remained unavailable; further exact-artifact and algorithm questions stay in the private backlog. This is a bounded research pass, with no all-internet completeness claim. No candidate infrastructure was contacted, paid service called or private Hunt export used.
