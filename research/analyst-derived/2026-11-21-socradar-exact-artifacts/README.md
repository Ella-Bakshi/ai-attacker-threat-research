# Exact public PHP2Shell campaign artifacts: independent static review

Reviewed **21 November 2026**. We acquired **10 exact source-backed custom script/PHP artifacts** from the [18 November public MalwareBazaar archive](https://datalake.abuse.ch/malware-bazaar/daily/2026-11-18.zip), totaling **134,626 bytes**. Each file matched the original publisher's SHA256, the archive's CRC and the declared byte count. Files were treated as hostile data and were never executed or imported.

This is the separate **PHP2Shell maq/modified-omp campaign** described by [SOCRadar](https://socradar.io/blog/php2shell-ai-agents-credential-harvesting/). No ARTEX or CyberStrikeAI association is claimed.

The supplement adds **36 independently derived memberships**: 30 file identities (10 SHA256 corroborations and 20 newly computed MD5/SHA1 identities) and six narrowly scoped static network facts. They represent **21 new type/value pairs** and 15 existing-value corroborations. No new IP is introduced.

The newly cataloged configured endpoint is **`206.245.153.56:42283`**. Exact bytes in the source-reported `j364_hook.php` artifact, SHA256 `4712fe539da6b81329dfe25d1b0e38a04539a68fac58bd8f6a537807b3f15cf5`, reference this destination in both a process-check expression and a conditional reverse-shell launch. These are static strings/dataflow; no successful callback is asserted.

Other facts independently corroborate the known `206.245.153.56` host, the default HTTP upload endpoint on **8088**, a qualified upload-path template and the exact `tools/php-loot.php` download path. Collector upload defaults are overridable through the environment and depend on runtime job IDs and branch conditions.

Two acquired `keep.sh` variants configure **43402 as the remote-forward listener on the SSH server**, forwarding to a loopback Dropbear endpoint. It is **not** the client's outbound SSH destination port; the loopback target is not published as exposed victim infrastructure. The source variants remain distinct exact file identities.

[Evidence](sample-evidence.json) and [records](records.json) retain artifact/member identities, acquisition UTC times, byte offsets, line numbers, literal lengths and derivation methods. Score **60** expresses independently examined static artifact evidence. Original campaign/unauthorized-activity attribution remains the publisher's moderate-confidence assessment; operator identity, successful execution, current service operation and country targeting remain unestablished.

Three staged public exploit artifacts were deliberately not acquired. Loopback, container, cloud-metadata and scanner-example destinations were excluded. Raw scripts, private keys, authentication values and full shell commands are not redistributed. These observations are for qualified historical correlation, not an automatic block list.
