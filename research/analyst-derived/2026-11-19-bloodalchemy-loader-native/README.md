# BLOODALCHEMY supporting loader: deeper native review

Reviewed 19 November 2026. This examines a **previously acquired** exact DLL from [CrowdStrike's VAPOR PANDA report](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/), SHA256 `3fb5a9fb3e2cb1d6208966bd4e55d10282d19c7250d827efa560463d60a12ee4`. It is campaign supporting malware, separate from the ARTEX framework itself.

Ghidra12.1.4 reconstructed all **333 discovered internal functions** in this finite import inventory. This includes runtime/library routines and does not prove absence of undiscovered code or complete behavioral understanding. Selected operand/control-flow claims were independently checked with Capstone.

Two new sample-specific observations are documented in [the evidence](native-loader-evidence.json):

- The sibling encrypted payload format uses its first 16 bytes as an AES-128 key and processes the remaining body as CBC with a zero initial IV. A separate inert algorithm translation matched an independent cryptographic reference on six synthetic inputs. The actual encrypted payload and its key/plaintext were not obtained.
- A conditional helper patches 12 bytes at host-module-base+0x1000 with a loader redirection, restores protection, and the loading path passes the decoded buffer to `EnumDateFormatsW` as a callback. This is a static capability, not an observed event. The patch address is not read from the host's PE entrypoint.

Both patterns remain **software/capability references at score 20**. Their operational specificity is untested; neither is an automatic blocking rule. No new malicious C2 address or victim activity was recovered. No sample, controller, payload or source setup hook was executed. Binaries, native projects and C/ASM remain private.
