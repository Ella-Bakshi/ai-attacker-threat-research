# CyberStrikeAI campaign support script: exact public-content reconstruction

On 16 November 2026 we independently recovered an exact representation of the supporting `p1.ps1` PowerShell script displayed in [Kaspersky's original 2 November report](https://securelist.com/tr/cyberstrikeai-attacks/121715/). This is a supporting reverse shell, separate from the CyberStrikeAI Windows/Linux beacons and controller. No original script file or new beacon binary was downloaded.

The [publisher's image10](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2026/10/30191314/cyberstrikeai-attacks10.png), under execution and privilege escalation, displays the complete script over five visual rows. We transcribed it as inert data, reversed the publisher's explicit IP defanging, and compared 486 bounded combinations of row joins, outer line endings and UTF-8 BOM representation. Exactly one representation matched the reported 372-byte size and all three explicitly named publisher digest identities:

| Algorithm | Independently reproduced value |
|---|---|
| MD5 | `0bbd08af95f877f1d568b03de2eb76b4` |
| SHA-1 | `724a163071ef0ab58972f03325c68437933e77f0` |
| SHA-256 | `43b1e81adfbeb36dcc532471ee2468c861c4ec38cd34db433c4fa18ed6f91549` |

The matching representation is ASCII/UTF-8 without BOM, visual-row separators or a trailing line ending. Hashes authenticate that byte representation against the publisher's identity table; they do not independently authenticate its victim telemetry.

Static inspection of the reconstructed text confirms a TCP client destination of `185[.]186[.]245[.]144:5501`. The [structured evidence](script-static-evidence.json) records the image/report identities, reconstruction method, matching digest bridge, byte offsets, constructor and limits. No script, network client or controller was executed. No connection, successful shell, particular victim, current service or AI-authorship claim follows from this source inspection.

These are **four new independently derived evidence memberships for existing values**: three file identities and one supporting callback endpoint. There are zero new type/value pairs, zero new IP addresses and zero newly verified malicious C2 IPs. Their score 60 describes exact static artifact evidence, not a maliciousness probability. Original campaign roles remain attributed to Kaspersky; the portal and report are the same publisher.

Raw script bytes, screenshot copies and executable reverse-shell code remain private. The two publisher-identified Windows beacons remain unacquired through the finite lawful public routes reviewed here. Source-restricted API documentation was respected, and previously completed archive windows and fixed seed comparisons were not repeated.
