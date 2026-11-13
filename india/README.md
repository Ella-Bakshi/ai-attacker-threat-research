# India targeting evidence

**The scope is infrastructure used against Indian targets, wherever that infrastructure is hosted.** See [C2 infrastructure targeting India](C2-INFRASTRUCTURE.md) for 18 source-reported C2 records, with delivery and configuration resources separated. Campaign-level targeting evidence is accepted; a named Indian victim is not required for each endpoint. The framework-specific gap below does not mean there is no publicly documented C2 targeting India.

As of 2026-11-10, **0 exact public ARTEX/CyberStrikeAI indicators were verified as specific to the Indian campaign in this collection**. CERT-In confirms CRAFTY FALCON targeting of India's BFSI sector and names the frameworks, but restricts the detailed IOC/fingerprint/rule set. [Evidence assessment](evidence-assessment.md).

- [Targeting-supported IOC CSV](targeting-supported-iocs.csv): intentionally header-only; no hidden values guessed.
- [Campaign-scope observables](campaign-scope-observables.csv): nine values from Zscaler's multi-country operation, whose operator prompts included India. These are targeting-intent/context associations, not per-IOC proof of Indian compromise.
- [Eight behavioral hunt hypotheses](behavioral-hunts.csv): grounded in the public advisory; not static IOCs or validated production rules.
- [Source-scoped campaign facts](campaign_context.json) and [rejected attributions](rejected_india_attributions.json).

An IP's hosting country, an India-based publisher, a shared tool or mention in an Indian advisory is insufficient to label an IOC India-specific. Korea/FortiGate indicators and the locally analyzed sample have not been attributed to CRAFTY FALCON. Additional AI-assisted India campaigns are now documented separately in the [India campaign supplement](additional-ai-campaigns/README.md), with their own source lists and static-analysis provenance. They are not attributed to these frameworks.
