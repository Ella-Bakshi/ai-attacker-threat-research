# LeadStack npm package: exact artifact review

Nine source-linked `@leadstack/crm-connect` archives from the 16 November 2026 release sequence were acquired from the registry mirror referenced by [SafeDep’s original report](https://safedep.io/blog/malicious-npm-leadstack-crm-connect-hermes-agent-backdoor), published 19 November. All nine archive SHA256 values match the [publisher’s typed indicator attachment](https://safedep.io/data/blogs/malicious-npm-leadstack-crm-connect-hermes-agent-iocs.csv). Registry SHA1 and npm SHA512 integrity values were also independently recomputed.

The archives total 34,025 bytes. They were parsed as hostile data in memory. Nothing was installed, imported, run, or extracted to archive-supplied paths. Embedded addresses, URLs and instructions were never followed.

The 38 independently derived memberships comprise 17 SHA256 identities, nine package versions, nine static URLs, one IPv4 address, one explicitly written host/port and one tenant hostname. Twenty-eight values overlap the separate external-report memberships; ten add values beyond those external rows and the baseline. The IPv4 address already appears in the source-reported packet and is not an additional global address.

The 17 hashes identify nine complete archives, five source-reported helper scripts and three separately parsed configuration files. Configuration-file hashes identify non-executable data within the malicious package; they are not stand-alone malware verdicts. All own rows use evidence score 60 for exact bytes/static configuration. External source-only rows retain their separate scores and provenance.

| Versions | Reviewed delivery behavior |
| --- | --- |
| 1.0.15 | Install hook prepares Hermes Agent and explicitly requests a root system service, then renames its unit. |
| 1.0.18 | SDK-triggered agent setup adds a user-service persistence path. |
| 1.0.19–1.0.21 | Helper code expects a remote JavaScript module and starts the returned file in a separate Node process. |
| 1.0.29–1.0.30 | Install helper contains a platform/version download template and a subsequent local execution call. |
| 1.1.0–1.1.1 | Install helper resolves a platform package and invokes its setup path; the original report says those platform packages were not published. |

The evidence preserves each archive’s acquisition URL and time, exact hashes and size, member hashes, uncompressed TAR offsets, and selected member byte offsets/line numbers. Six explicit static checks cover the service override, unit rename, module-cache destination, detached worker, binary-download template and platform-package setup path. URLs formed from a literal configuration origin plus a literal source suffix are identified as static constructions.

The real remote `.env`, persona, JavaScript module and native payload were not obtained. Static defaults and command arrays do not establish a successful victim installation, callback, privilege gain or present operation. Borrowed unrelated-domain defaults and generic Hermes unit patterns were excluded from malicious indicators. Nous Research’s Hermes Agent and the unofficial npm wrapper remain legitimate software; the source-reported malicious package installed them without the machine owner’s authorization.

`records.json` contains independently written facts and typed observables. `sample-evidence.json` is the compact artifact evidence. Raw archives and scripts remain private; no credentials, raw package content or vendor article copies are redistributed.
