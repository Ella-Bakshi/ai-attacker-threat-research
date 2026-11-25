# 25 November 2026 daily hunt

This review adds **30 evidence records**, covering **29 new distinct type/value pairs** and **5 newly selected historical IPs**. The repeated address retains two source memberships. [Records](records.json) · [CSV](records.csv) · [Counts](summary.json)

## Source-reported incident evidence

- JFrog reported an ARTEX-linked malicious-model campaign on Hugging Face on 24 November. Its source data gives 14 exact SHA-256s for malicious model files and probe components. One additional hash identifies a listed tokenizer configuration whose exact revision remains uncertain. One published path describes an operator self-test. JFrog observed no reportbacks from external victims before takedown. The review checked the publisher's literals and dates. [JFrog investigation](https://research.jfrog.com/post/the-agent-that-robbed-itself-an-ai-driven-hugging-face-malware-campaign-leaks-its-own-operator/) · [Source data](https://research.jfrog.com/hf-agent-self-exfil-iocs.csv)
- Unit 42's 24 November report lists four IPv4 observations and an operator-local path. It identified historical C2 and payload staging on one address that also hosted a CyberStrikeAI service. The July–September window describes the full set of cases. [Unit 42 original report](https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/)
- ReliaQuest's 7 October case study adds three address observations and a path on the affected host. It observed pre-incident traffic and staging on the shared address. CyberStrikeAI was present there, and its participation in that intrusion remains unestablished. The role and provenance of each observation remain separate. [ReliaQuest original report](https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/)

## Our static software fingerprints

We computed five new SHA-256 fingerprints from pinned public source assets. One ARTEX-family logo is byte-identical in three checked project trees. One is ScopeWeaver's source icon, and three are browser extension icons shared by CyberStrikeAI v1.8.0 and v1.8.1. These identify exact assets and have no incident or infrastructure attribution. The record locators identify the commits and paths. [Software fingerprints](software-fingerprints.csv)

## Context and open leads

Eye Security's incident report and UK NCSC's guidance supplied context. Wiz's three explicitly attributed ARTEX operator addresses were already recorded, and its remaining mixed-framework addresses lack individual ARTEX or CyberStrikeAI attribution. This run produced zero independently verified malicious IOCs. The 35 unverified catalog relationships and 25 private leads retain their open status. [Eye Security](https://eye.security/blog/ai-vs-ai-artex-autonomous-attack-incident-response/) · [UK NCSC](https://www.ncsc.gov.uk/blogs/familiar-weaknesses-exploited-faster-defending-against-agentic-cyber-attacks) · [Wiz](https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks)
