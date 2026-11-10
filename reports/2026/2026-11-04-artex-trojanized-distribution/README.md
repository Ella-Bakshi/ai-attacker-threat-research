# Artex Trojanized Distribution

Report date: 2026-11-04. Collection reviewed: 2026-11-10. Source: [badbyte](https://badbyte.io/artex-backdoor-docker-image/). This folder contains 12 source-attributed observables with explicit categories and confidence scope; it is not a claim that every value is malicious or unique to ARTEX/CyberStrikeAI.

[CSV](indicators.csv) and [JSON](indicators.json) retain source URLs, published dates, available first/last observations, limitations and India evidence fields. The table defangs network values; machine exports preserve canonical values.

| Value | Type | Role | Confidence | Category |
|---|---|---|---|---|
| `congdonglinux/artex:latest` | container_image | Reported trojanized image tag (mutable) | Medium | main-iocs |
| `tomicdd/artex:latest` | container_image | Reported trojanized image tag (mutable) | Medium | main-iocs |
| `ce85d8369ccc1a85423f1f75d2f3afaa2fab759e580da37a6891af2f7392745e` | container_index_sha256 | Reported trojanized OCI image index | High | main-iocs |
| `009e2bdd6548886a363ee06d17331c7209741273d886f1bb818bceeb416f1654` | container_layer_sha256 | Layer containing the reported backdoored /app/artex executable | High | main-iocs |
| `cb85a7206290dc1813e3203e044741054b26c7a7c557c7d9d6d91af20aeb232b` | container_manifest_sha256 | Reported trojanized linux/amd64 image manifest | High | main-iocs |
| `d5070f52262effe216b840711343bff8f2787f39208d887d8dfd9c673f8d1573` | sha256 | Reported trojanized ARTEX executable (/app/artex) | High | main-iocs |
| `Docker Hub: tomicdd &#124; GitHub: trhhubsd (formerly ptasm)` | account | Accounts / tomicdd created 2026-10-08 18:50:38 UTC | Low | software-fingerprints |
| `a4f4d38c7b60f68abbd6a574aa59188063f2d86c` | git_commit_sha1 | Commit / compose image swap | Low | software-fingerprints |
| `v0.3.16-0.20261008134550-5c0dbd4bec94+dirty` | go_module_version | Go module version | Low | software-fingerprints |
| `github[.]com/trhhubsd/ARTEX` | repository | GitHub repository / formerly ARTEXX , repo ID 1410926671 | Low | software-fingerprints |
| `github.com/Autumn-27/artex/server.verifyCaptcha` | symbol | Go symbol | Low | software-fingerprints |
| `3aC1db3gGU08O4UHbAt4J` | web_build_id | UI build ID / visible in served HTML | Low | software-fingerprints |

[Evidence methodology](../../../docs/methodology.md).
