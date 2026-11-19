# Exact supporting artifacts and ARTEX software reference

On 19 November 2026 we acquired three exact public artifacts using bounded reads of published MalwareBazaar daily archives. No executable, loader, controller, hook or setup script was run. Raw binaries, C/ASM, projects and captures remain private.

Two files match [CrowdStrike's original VAPOR PANDA report](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/): the legitimate GameHook executable (`49fe7041…`, 159,952 bytes) and the publisher-reported BLOODALCHEMY loader DLL (`3fb5a9fb…`, 96,768 bytes). Their three locally computed hashes corroborate existing source records. These are supporting components, separate from ARTEX/CyberStrikeAI controllers and beacons. GameHook identities remain legitimate supporting context at score 0; exact loader identities have score 60, with campaign attribution retained to the publisher.

Ghidra 12.1.4 reconstructed 15 selected functions per supporting artifact, 30 total, from inventories of 460 and 333 functions. Runtime/library inventories were not fully reconstructed. Exact bytes and native arguments establish three host/software facts, capped at 20:

| Value | Exact static relationship | Limit |
|---|---|---|
| `graphics-hook_config.bin` | Loader function `0x18000118c` decodes the filename; caller `0x180001238` builds a colocated path and opens it | Encrypted payload bytes were not obtained; filename alone is not a maliciousness indicator |
| `graphics-hook-filter64.dll` | GameHook `0x140001050` constructs a sibling path and passes it to `LoadLibraryA` | Legitimate dependency name; no observed load or compromise |
| `ISR_GAMEHOOK_64` | Exact UTF-16LE argument to GameHook's `CreateMutexW` call | Legitimate GameHook marker, not ARTEX-specific |

[Scientific evidence](static-artifact-evidence.json) records hashes, offsets, native functions/call sites, the inert byte-arithmetic filename decode and coverage limits. An independent reviewer reproduced the file identities, decoded filename and Go metadata. No target code was executed, and static capability does not establish a victim event.

One hash in [ReversingLabs' 18 November operator-software list](https://www.reversinglabs.com/blog/threat-researchers-notebook-detection-strategies-for-artex-and-related-forks), `44f8cb79…`, matched a retained 28 October archive directory. Its exact 38,142,078-byte ELF64 AArch64 file was acquired. Static metadata reports Go 1.26.3, linux/arm64, package `github.com/Autumn-27/artex/cmd/artex`, revision `ee413324c868ec09d5ccbae31d04da7a6e24076d` and `modified=false`. These compiler-supplied fields may be forged. That revision was not found in BaaRai/ARTEX, so no exact generating public revision is established. The three local hashes are software reference evidence at score 20, separate from malicious operator or deployment claims. No full controller reconstruction was performed; the other three matching operator artifacts were not acquired.

This packet adds 12 own memberships: six existing supporting-file identity corroborations, three host/software facts and three software-reference hashes. Six values are new to the baseline master; simultaneous source additions may overlap. It adds zero IPs, malicious C2 values or resolved public attribution questions.
