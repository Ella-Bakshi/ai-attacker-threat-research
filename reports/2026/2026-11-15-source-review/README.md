# AI Attacker Threat Research — original-source review, 15 November 2026

**Historical review snapshot.** This report and its 73-row unresolved CSV preserve the state at completion of this pass. See the [later evidence-resolution report](../2026-11-15-evidence-resolution/README.md) and [current unresolved export](../../../research/unverified-findings/source-review-unresolved.csv) for subsequent dispositions. The linked canonical index and master continue to evolve.

This completed review covered all **12,299 canonical records** and the **3,740 additional scalar values** found only in the master at that time. Every record received a scoped source-review disposition. It added no new indicator values or IPs. **73 unresolved or qualified findings were separated**, including 64 already classified as unresolved and 9 newly separated in this pass. [Historical unverified CSV](unverified-findings.csv) · [Full record index](../../../data/index.json) · [Master](../../../data/ALL-FOUND-master.csv).

| Canonical review state | Records | Meaning |
|---|---:|---|
| Original source support | 3,559 | Publisher/pinned-source value and stated role, with date meanings reviewed |
| Exact artifact support | 327 | Exact artifact identity and bounded byte/native/event derivation |
| Retained historical provider observation | 8,340 | Response/feed/table membership, without authenticated-acquisition or maliciousness claims |
| Unverified | 73 | A remaining algorithm, attribution, address, relationship or detection-pattern qualification |

The additional 3,740 master-only rows are retained provider observations. These record counts are not malicious-system counts, and the master deduplicates exact type/value pairs across source memberships.

## What was checked

The earlier incident review covered 442 records. The 20 original-source access gaps have now closed: ordinary public SentinelOne and Splunk reports support their literal values and stated roles. Another 574 report-backed records were checked against original content or explicit publisher-linked artifacts. Case/defanging, enumerated alternatives, endpoint components, layout whitespace and publisher-linked IOC files are documented normalizations, not invented values.

All 2,546 addresses in the [pinned Talos list](https://github.com/Cisco-Talos/IOCs/blob/23e72502a454456d17a85f147d0e837edfea9489/2026/11/artex-and-beyond.txt) match. The 689 retained [ThreatBook feed](https://threatbook.io/hubfs/Feeds/ARTEX.txt) endpoints and 377 retained [ARTEX](https://scanmalware.com/hunts/328)/[CyberStrikeAI](https://scanmalware.com/hunts/337) hunt-table records also match their historical evidence. A value absent from a later rolling feed is not silently deleted or relabeled as disproven.

The 7,274 canonical Censys/Shodan records match actual endpoint/certificate fields, all 14,200 listed source memberships and every supplied scan date. Six records have unknown dates; they remain unknown. The earlier host-only uncertainty for 39.107.106.59:8080 is resolved by an explicit retained host/port/title response. The 3,740 master-only values likewise match all 6,701 source memberships and supplied dates; 544 domains are actual web-property hostnames, not reverse-DNS names promoted into software observations. These checks establish retained-response consistency, not independent authentication of acquisition, software specificity, current service or malicious use.

All 397 analyst-origin records were reviewed: 326 exact-artifact observations, 61 pinned-source observations and 10 qualified patterns. After correcting the UUID claim to its verified base/prefix, that narrow fact is retained as artifact-supported; the other nine qualified hypotheses/relationships remain separated. All 195 ARTEX native route registrations received fresh literal/length/registration checks. Existing unchanged Windows, VoidLink and India peer-reviewed subsets were reused explicitly; complete fresh decompilation of every function is not claimed.

## Corrections and unresolved findings

- One additional LAMEHUG-associated64-hex hash has no verified algorithm label. Its value, publisher role and dates are preserved as an algorithm-unverified lead. The earlier four algorithm-unverified source hashes remain qualified; the supporting-script entry is now in the unresolved export.
- RogueWinRM and Mimikatz supporting-file MD5 identities have independent exact-byte bridges. They remain supporting tools; file identity does not prove deployment of this copy in a reported campaign.
- Seven generic browser-check primary URLs were replaced with exact sample/archive evidence. The previous URLs remain correction context, not evidence sources.
- The CyberStrikeAI UUID formula describes a base/prefix. HTTP code appends a hyphen and 16 runtime token characters at native call 0x656f2f; the base must not be used as an exact complete-field match.
- A legitimate ConnectWise remediation application ID received a narrower role description. One filename's prose layout was corrected.
- Fifteen source-file hash differences reproduce exactly as Windows CRLF versus Git LF bytes. Representation is recorded; these are not content mismatches or new malicious hashes.

The Microsoft178.15/178.16 address discrepancy, shared-apex leads, sample/campaign ambiguities and unvalidated detection hypotheses remain unresolved. Source-literal support does not resolve those separate questions.

## Using the data and map

The map's **Source review** filter separates original source/artifact support, retained historical observations and unresolved memberships. One IP can have different records in several states; source details retain unresolved record IDs. Unresolved records cannot independently earn a C2 flag or a score above10; shared nonindicative context stays0. Other supported records retain their own scoped roles and scores. The selected overview remains 6,320 IPs. Fourteen addresses have at least one unresolved membership; eleven have only unresolved memberships. Mixed memberships are visible in the source details.

No candidate services were contacted, DNS lookups or scans performed, samples executed/submitted, paid-provider calls made or commercial Hunt export used. Raw source copies, artifacts and internal review ledgers remain private. This source review does not approve the complete catalog or map as an automatic block list. [Reliability and appropriate use](../../../docs/indicator-reliability.md).

Later review: [deeper source and public-artifact hunt](../2026-11-15-deeper-hunt/README.md) revisits the remaining40 and resolves one digest identity. Its current list has 39 unresolved findings; this folder's dated decision/snapshot exports retain their earlier state.

Later [exact-artifact and identity review](../2026-11-15-exact-artifact-review/README.md) supports four additional file identities. The current unresolved list has 35 records; this folder’s dated snapshots retain their earlier state.
