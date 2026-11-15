# CyberStrikeAI-lineage Linux artifact: additional native URL routes

Reviewed on 15 November 2026. This pass derives two additional configured HTTP URL prefixes from the exact historical ELF `f825c06b278627ab9753ccdeffd510a32f6bc706845931906597d1f8d978913d` (6,168,868 bytes). It was acquired during the earlier pass from the public 7 October 2026 daily archive; its identity and original acquisition time are retained. This is new analysis of an existing artifact, not a new sample acquisition or a newly discovered malicious C2.

| Configured prefix | Native function | Evidence scope |
|---|---|---|
| `http://23[.]254[.]195[.]48:18443/tasks` | `main.fetchTasks`, entry `0x65e380` | Native composition of HTTP GET URL. Runtime session query is omitted. |
| `http://23[.]254[.]195[.]48:18443/file/` | `main.fetchC2FileByID`, entry `0x65c520` | Native composition of HTTP GET file-transfer URL. Runtime file identifier is omitted; a separate TCP branch precedes this HTTP route. |

[Structured evidence](linux-native-prefix-evidence.json) preserves the original ELF identity, Go-string descriptors and lengths, mapped byte offsets, format-call and HTTP-constructor locations, and URL-result forwarding checks. Ghidra 12.1.4 produced C-like reconstructions using recovered Go function boundaries. Capstone 5.0.6 independently checked the concrete pointer, length, GET-method and call/register evidence. The decompiler's recovered types and inferred Go ABI are approximations, not original source.

All 66 recovered `main.`-prefixed application functions completed reconstruction. This finite application scope excludes exhaustive decompilation of runtime/dependency functions in the 6,459-function inventory. Three selected functions have detailed independent operand checks. Conditional Linux persistence also corroborates existing `.bashrc`/cron source patterns: its presence establishes code capability, not installation on a victim. These existing values are not counted again.

The prefixes have High confidence in exact artifact/native construction and evidence score 60 for static configuration. Prior code comparison supports CyberStrikeAI beacon-template lineage; the exact generating revision, operator, named campaign, victims, successful exchanges and current operation remain unknown. The target, controller and persistence commands were never executed. Keys, token values, dynamic identifiers, raw C/ASM and sample binaries are excluded from publication.

## Exact-sample acquisition effort

Two publisher-linked Linux sample identities remain sought: `5d1b591d…` (the explicitly bridged Securelist `09e1…` sample) and `1c6498f0…` (Securelist `805b…`). Additional exact ARTEX-associated seeds were included in the same finite metadata checks to avoid redundant requests. Fifty-one newly completed or previously incomplete daily-archive directories, covering 30,814 entries, contained no exact seed filename match. The former 21/22 October parser gaps were closed using explicit ZIP64 support. The 14 November archive returned 404. These results cover the recorded windows only and do not prove absence from all repositories.

Subsequent normal public OpenTIP rendering supplied explicit digest bridges for all three formerly untyped CyberStrikeAI/script hashes. These publisher metadata identities are now supported; exact sample bytes remain unacquired. The two CT sibling-domain campaign relationships remain unresolved. See the [identity review](../../../reports/2026/2026-11-15-exact-artifact-review/README.md).

No candidate network requests, DNS resolution, scanning, sample submission, malware execution or paid-provider calls occurred. Public sources with authentication or verification restrictions were not bypassed.
