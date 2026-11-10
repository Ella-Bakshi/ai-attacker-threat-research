# India targeting: ARTEX and CyberStrikeAI

Research date: 10 November 2026. **No public exact network/hash IOC was verified for the ARTEX/CyberStrikeAI-linked CRAFTY FALCON campaign in this framework-specific pass.** This is a deliberate empty confirmed list, not a claim that attacks lack indicators.

CERT-In/CSIRT-Fin's [CIAD-2026-0058](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES02&VLCODE=CIAD-2026-0058), published 4 November 2026, describes CRAFTY FALCON attacks against financial-sector entities and names ARTEX, CyberStrikeAI, PentAGI and Cairn. It updates [CIAD-2026-0046](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES02&VLCODE=CIAD-2026-0046), published 9 October 2026. The public advisory says the complete IOCs, fingerprints and detection rules were distributed through restricted channels. Those values were not guessed or replaced with unrelated campaigns.

The India connection is victim/target context, not where a server is hosted. [Reuters' original report, syndicated by MarketScreener](https://www.marketscreener.com/news/india-flags-chinese-linked-ai-tools-in-hacking-campaign-against-financial-firms-ce785fdcda81f42d), explicitly describes Indian lenders/fintech/crypto victims, but notes CERT-In did not connect particular named institutions' incidents to CRAFTY FALCON. Tool origin does not identify operator nationality or state sponsorship.

`behavioral-hunts.csv` provides eight analyst-authored hunt hypotheses grounded in the public advisory, with data requirements and false-positive context. They are **behavioral guidance**, not static IOCs, validated rules, or framework-exclusive detections. Thresholds and windows require local tuning.

## Rejected India attributions

The [Threadlinqs compilation](https://intel.threadlinqs.com/threat/TL-2026-5362) advertises eight IOC values, of which two are publicly visible: 38.244.50.120 and xcai.pro. These are the already-published Korea ARTEX host and shared LLM reseller from CrowdStrike. The compilation itself says CERT-In published no actor-specific network IOCs. The other six values require account/credit access; no access control was bypassed. Its sample payment rule uses additional numerical/window assumptions not published by CERT-In; they were not adopted as official parameters.

iZOOlogic's [India NBFC payment-fraud analysis](https://izoologic.com/threat-advisory/ai-assisted-payment-api-fraud-campaign-against-indian-nbfcs/) explicitly says no IOCs were published for the Indian intrusions. Its related Korea/FortiGate values are pivots, not evidence of Indian campaign involvement. Ordinary HTTP retrieval returned 403; public web-tool text was reviewed separately, and the challenge-page digest is not passed off as article evidence.

The separate BadByte trojanized ARTEX-image report was not linked to CRAFTY FALCON by a primary source found here. Victim organisations, reporting contacts, legitimate banking APIs and Indian-hosted software sightings were not turned into malicious IOCs. Detailed country-target evidence from global campaigns requires a per-record link before it can carry an India-specific label.

## Files and scope

- `targeting-supported-iocs.csv`: explicit empty confirmed set.
- `campaign_context.json`: source-scoped campaign/geography/timeline evidence.
- `behavioral-hunts.csv` / `.json`: eight analyst hunt cards.
- `rejected_india_attributions.json`: disputed or unsupported geographic relationships.
- `sources.json`: capture URLs, retrieval dates and hashes. HTML/text captures are intermediates; do not publish them as source article bodies.

The bounded search included CERT-In, Indian vendors (Seqrite/QuickHeal, CloudSEK, Cyble, K7), Zscaler and iZOOlogic, plus original incident reporting and public compilations. No other primary ARTEX/CyberStrikeAI India-specific exact IOC set was found. Separate APT36/Gopher Strike/Sheet Attack campaigns are outside this framework-specific assessment and are now covered in the [India campaign supplement](additional-ai-campaigns/README.md) and [dedicated C2 infrastructure view](C2-INFRASTRUCTURE.md). Their campaign-level India targeting evidence does not depend on hosting country or a named victim per endpoint. No Censys queries, direct deployment requests, authentication attempts or sample execution occurred.
