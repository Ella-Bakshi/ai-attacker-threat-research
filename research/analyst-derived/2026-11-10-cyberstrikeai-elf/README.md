# Our CyberStrikeAI-lineage sample analysis

Analyzed 2026-11-10, without execution or endpoint contact. SHA256: `cbf1045bb2d4de52142b68d825d265588e1c94ec7d4132284deea8fef67fe4d4`. Native/source evidence supports generated CyberStrikeAI beacon lineage. The exact operator, named campaign, current live C2 and India targeting remain unknown.

The configured base is `hxxp://23[.]254[.]195[.]48:8443`, with direct POST check-in/result URLs and task/file URL constructions. Static configuration is not an observed network connection. All 66 recovered main functions were decompiled, with 32 containing inline warnings; dependency/runtime functions were not bulk-decompiled. Byte offsets and direct call operands corroborate the configuration claims.

The additional ten observations cover conditional cron/bashrc persistence, screenshot staging, UUID construction, check-in and file-transfer structures. Static capabilities do not show that a victim artifact was actually created. [Additional analysis](additional-analysis.md), [CSV](indicators.csv), [JSON](indicators.json), [sanitized evidence](evidence.json).

The generated-beacon and persistence YARA rules match this sample within finite controls. The older transport-template rule misses this HTTP sample, so broad beacon coverage is not claimed. The screenshot Sigma rule is experimental and lacks backend/sensor validation. Secrets and sample binaries are omitted.
