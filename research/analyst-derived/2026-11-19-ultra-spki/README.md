# Ultra-suite public-key representation — 19 November 2026

We independently reconstructed one **91-byte DER SubjectPublicKeyInfo** from the P-256 public point displayed in [crt.sh leaf 29831682796](https://crt.sh/?id=29831682796). Its SHA256 is `ed83de5e21330f4dcea9f6cdff13751307bf7ba1ee2d563ee83e2e220cd20e16`, matching the separately advertised SPKI lookup identity. Both a standard cryptographic-library encoding and an independent fixed DER-prefix construction produce that digest.

The [evidence](ct-spki-evidence.json) preserves the retained HTML identity, visible-text locator, exact public X/Y coordinates, curve, encoding method and byte counts. The public point is not a private key or credential.

This is **one own software/reference observation at score 20**, not a new malicious C2. Full certificate DER acquisition failed; the original certificate bytes, signature and CA path were not verified. Certificate issuance does not prove deployment. The historical certificate association with the Ultra origin is [Profero-reported](https://profero.io/blog/ultra-suite-artex-ai-attack-agents/); it is not inherited by the same host's historical CyberStrikeAI service on another port. Ownership, live operation and compromise remain separate questions. No target request, scan, submission or artifact execution occurred.
