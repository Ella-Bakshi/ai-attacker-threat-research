# CyberStrikeAI console software references — 19 November 2026

Following [Spectrum's original research](https://www.spectrum.security/blog/offensive-ai-tools-in-the-wild), we examined [official source at a pinned revision](https://github.com/AIPentest/CyberStrikeAI/tree/af6cf7500c8eff357cc6c3f50e7c7b150fcfa836). Our two derivations are separate from Spectrum's reported fingerprints:

- SHA256 `b30b795f1fce8fa5541455cedbd8359ef9e305e629645817372c0ffbe99e673c` identifies the exact 102,811-byte `web/static/css/c2.css` reference stylesheet. It is not a malware hash.
- A three-marker HTML conjunction combines `brand-wordmark__core`, `/static/css/c2.css` and the `cyberstrike-theme` local-storage key. [Exact source lines, file identities and method](source-evidence.json) permit reproduction.

The conjunction is a runtime-untested software-identification hypothesis. Broad benign/default controls and production specificity were not measured. Both records remain software fingerprints at score 20; copied assets, authorized installations and source-to-served-content differences remain possible. No service deployment, operator, campaign, compromise or current C2 is established. Commit time is a repository event, not an attack sighting. Nothing was executed.
