# Exact trojanized ARTEX artifact verified offline

On 21 November 2026, the user downloaded the exact original sample through the [YARAify provider UI](https://yaraify.abuse.ch/sample/d5070f52262effe216b840711343bff8f2787f39208d887d8dfd9c673f8d1573/). We verified its 51,210,988 bytes, SHA256 `d5070f52262effe216b840711343bff8f2787f39208d887d8dfd9c673f8d1573`, ZIP CRC and cross-hashes, then inspected it without executing it.

Native instructions connect `POST /api/auth/login` to a captcha-gated shell branch before username/password validation. The authentication wrapper allows this route without a JWT. The helper constructs `sh` with `-c` and the input, captures combined output, and returns it in an HTTP 200 JSON response. A configured database handle is a prerequisite. The ELF does not establish the service process identity or root UID. No request was sent to a console and no command was run.

We reconstructed 13 selected functions from an inventory of 31,087 function symbols and decoded all 407 embedded UI entries. Every non-directory compiler hash was checked. The known build ID is present. The embedded favicon matches the existing upstream asset, so it remains a shared software fingerprint. The index HTML hash identifies this build's asset; it does not prove that every server serving that asset has this backdoor. No new malicious IP or current operation was established.

The [sanitized evidence](static-backdoor-evidence.json) records native addresses, original file offsets, scope and limitations. Independent review checked the sample identity and critical native operands. Raw binary/ZIP, pseudocode/ASM and projects remain private. These are our independently derived observations of an already reported artifact, not a claim of first discovery.
