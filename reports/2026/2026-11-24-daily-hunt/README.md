# 24 November 2026 public-source and artifact hunt

The review adds **16 evidence records**, representing **15 new distinct values** and **3 new selected map IPs**. Three findings come from independently hashed exact upstream assets. All address additions come from original publisher reporting. [Full records and source locators](records.json) · [CSV](records.csv) · [Counts](summary.json)

## Source-reported evidence

- Wiz identified three historical ARTEX operator hosts. Two are new map addresses. The third gains an incident role alongside its previous passive evidence. The publisher's late-October to November 1 date range is preserved separately from any exact event timestamp. The report establishes no C2 or India targeting role for these entries. [Wiz original table](https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks#iocs) · [Pinned companion CSV](https://github.com/wiz-sec-public/wiz-research-iocs/blob/4d39ec3255e90b1a68f0b6346f73e47fd81d0436/reports/agentic_attacks_in_the_wild_iocs.csv)
- In a separate intrusion, Wiz attributed the command layer to CyberStrikeAI and reported three exact Kubernetes, IAM and runner names. The report also identifies a separate ARTEX checkout. Per-marker observation dates remain unknown. [Wiz case report](https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks)
- Bitrise reported an exact agent client name in its own event records at 17:44:07 UTC on November 13. The client-name interpretation is scoped to that incident. [Bitrise incident report](https://bitrise.io/artex-incident-report)
- CloudSEK documented an adjacent espionage case with Hermes in the exposed operator workspace. The records preserve a historical C2 and staging IP, one infrastructure domain, and four published malware hashes. The Strix name in this case identifies the customized Hermes deployment. The case has no established ARTEX or CyberStrikeAI link. [CloudSEK original investigation](https://www.cloudsek.com/blog/off-the-rails-inside-an-exposed-silent-lynx-server)

## Our independently verified software observations

We computed SHA-256 from the bytes of the ARTEX v0.7.0 CycloneDX SBOM and the release's published checksum text. We also matched the exact CyberStrikeAI browser extension metadata across v1.8.0 and v1.8.1. These observations verify software identity. The review yielded zero independently derived malicious indicators. [ARTEX release](https://github.com/BaaRai/ARTEX/releases/tag/v0.7.0) · [CyberStrikeAI release](https://github.com/AIPentest/CyberStrikeAI/releases/tag/v1.8.1)

## Corroboration, coverage and holds

- The Hendry Adrian article summarizes ReversingLabs' already reviewed research. Spectrum's original census has existing dated records, with exposed software observed separately from incident evidence. AhnLab's Copy Cat article is already represented in the catalog. Starlog helps check source architecture and lineage. [ReversingLabs original](https://www.reversinglabs.com/blog/threat-researchers-notebook-detection-strategies-for-artex-and-related-forks) · [Spectrum](https://www.spectrum.security/blog/offensive-ai-tools-in-the-wild) · [AhnLab Copy Cat](https://asec.ahnlab.com/en/95875/) · [Starlog](https://starlog.is/articles/cybersecurity/how-artex-works)
- The European Commission's November 23 briefing confirms the EU Academy leak in its AI-assisted campaign. The briefing does not identify an exact framework or IOC. ScanMalware's lookup study provides aggregate telemetry only. [Commission briefing](https://audiovisual.ec.europa.eu/de/media/video/I-298395) · [ScanMalware](https://scanmalware.com/blog/ai-hacking-agents-using-our-data)
- Arkose's ARTEX testing adds controlled-lab context. ThreatFox tags and Offensive Agency deployment sightings are provider evidence. A label, shared host, or console match does not establish an operator or incident. [Arkose Labs](https://www.arkoselabs.com/blog/the-latest-in-agent-traffic-artex-pen-testing-tool) · [Offensive Agency methodology](https://offensive.agency/about)

No new provider export entered the project. The 35 unresolved canonical relationships and 25 private leads keep their existing dispositions. Use the exact original source roles and dates to guide correlation.
