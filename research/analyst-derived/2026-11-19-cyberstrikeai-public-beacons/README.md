# Independently examined public CyberStrikeAI beacon samples

Reviewed 19 November 2026. We acquired two exact members of the [8 October public MalwareBazaar archive](https://datalake.abuse.ch/malware-bazaar/daily/2026-10-08.zip), verified their hashes, size and CRC, and analyzed them offline. No sample was executed.

| Sample SHA256 | Configured HTTPS destination |
| --- | --- |
| `395ff8ba0708845abed2e6d4a3fc5b3c70702582d8a8f970ab46edb395f8509b` | `116.228.56.131:8443` |
| `5a8d7ca92610b3bb9d573e4aaf2dfec3e66f274e9609a7117ef6eab1a724cd2b` | `23.254.195.48:8443` |

Both contain specific CyberStrikeAI beacon-template code correspondence: 42 of 43 base function names match a [pinned official template](https://github.com/AIPentest/CyberStrikeAI/blob/6edc70f3fc6ece3678009b58c1900de02832690d/internal/c2/payload_templates/beacon.go.tmpl), and embedded metadata names `cyberstrike-ai v1.7.18+dirty`. The dirty working-tree flag prevents identifying an exact generating commit.

Ghidra reconstructed all 66 `main.` application functions in each finite inventory. The 6,372 total Go functions were inventoried, not all decompiled; complete semantic understanding is not claimed. Independent native operand checks verify POST `/check_in` and `/result`, plus GET `/tasks?session_id=` and `/file/` prefixes. Dynamic identifiers are omitted. [Evidence and exact offsets](sample-config-evidence.json).

These are our independently derived artifact observations from already public files. Score **60** means exact static configuration examined. It does not establish malicious use, a named campaign, successful communication, current operation or country targeting. They are separate from the still missing exact Kaspersky sample hashes and encrypted BLOODALCHEMY payload. MalwareBazaar labels their threat family unknown; differing vendor opinions do not override those limits.
