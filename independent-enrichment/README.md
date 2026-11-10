# Independent public-artifact CTI analysis

Reviewed **10 November 2026 UTC**. This is independently collected and analyzed evidence from public sandbox pages, certificate bytes and historical scan metadata. It adds **16 scoped records**: six derived observations, two TLS fingerprints, two unverified sibling-domain hypotheses and six shared-CDN context addresses. It does not establish Indian targeting, identify an operator or claim first-ever discovery.

## Concrete findings

The [public behavioral report](https://tria.ge/261027-qmb8eaes6q/behavioral1) for SHA-256 `1c6498f081ff7a5ef0e851d2c106668aef53e1384b8d0c52fa667e53a5664c33` maps in its General table to MD5 `805b9e4ae74c903787416800999b8418`, which [Kaspersky lists as a CyberStrikeAI Linux beacon](https://securelist.com/tr/cyberstrikeai-attacks/121715/). Our extractor reads the page's embedded strict JSON without evaluating JavaScript. Six TLS flows match `media.fastcdn.bar` on TCP **2083**, with client JA3 `20b279993ae2e137e62b9647c6d768fb` and server JA3S `eb1d94daa7e0344597e756a1fb6e7054`. The useful relationship is the conjunction of domain, port and fingerprints; the fingerprints alone are not established as unique. These are task-capture observations, not PID-attributed victim telemetry.

Three public runs of the exact previously acquired CyberStrikeAI-lineage ELF `cbf1045bb2d4de52142b68d825d265588e1c94ec7d4132284deea8fef67fe4d4` contain **80 outbound `POST /check_in` attempts** to `23.254.195.48:8443`: [run one](https://tria.ge/261106-kvkxmaat3v/behavioral1), [run two](https://tria.ge/261106-wzxb1a11bs/behavioral1), [run three](https://tria.ge/261107-yeacvaex6v/behavioral1). This independently corroborates its static configuration; it does not discover a new IP. Completion-to-next-attempt gaps are **5,000–5,006 milliseconds** across 77 intervals. A narrow static ELF check resolves the retry calls and verifies the initial five-second interval at file offset **5,812,984**, plus its nanosecond conversion. Runtime configuration can change it; five-second repetition is a low-specificity behavior.

No HTTP response codes were admitted for those requests. Registration, command execution and current C2 availability are **not established**. The report does not disclose sufficient simulation configuration to exclude sinkholing or network emulation. We neither executed a sample nor downloaded PCAPs or authenticated artifacts. Token/header values are omitted. The cbf1045 sample's relationship to the Kaspersky incidents remains unestablished.

The [CT certificate for `media.fastcdn.bar`](https://crt.sh/?id=29635812593) was downloaded and parsed locally. Its **DER** SHA-256 is `6b03dfb3dbd4c42441bbd916ab6ebdac5a205dab1f219f95c6151e0549d8f298`; validity is **26 September–25 December 2026**. This fingerprint identifies the CT certificate, which was not observed in a live controller handshake. The PEM download-file hash is different. Four certificates were parsed; one wildcard entry is a **precertificate**, kept as CT context rather than a live-leaf fingerprint. `static.fastcdn.bar` and `www.fastcdn.bar` are certificate-backed sibling leads only. Shared parentage and issuer do not establish common malicious control or C2 use.

[Public URLscan search metadata](https://urlscan.io/api/v1/search/?q=domain%3Amedia.fastcdn.bar&size=100) supplies two scans dated **2 and 3 November 2026 UTC**, showing Cloudflare **523** and **521** origin errors. Detail APIs returned 403, and no bypass was attempted. These may be researcher scans, not campaign activity. Their edge addresses and the sandbox DNS A/AAAA answers fall within [Cloudflare's published IPv4](https://www.cloudflare.com/ips-v4) and [IPv6](https://www.cloudflare.com/ips-v6) ranges. These six shared addresses are context, with score hint zero; they are neither attacker-owned origins nor standalone blocking indicators. Cloudflare [documents 2083 as a supported proxied HTTPS port](https://developers.cloudflare.com/fundamentals/reference/network-ports/).

The public scan search disclosed a 30-day window. CT searches, sandbox runs and download checks are bounded observations, not exhaustive historical coverage. Certificate validity, sample submission, relative sandbox milliseconds, scan time and review time remain separate. Blank first/last dates mean victim activity dates are unknown. Two CDN context rows use exact URLscan task times with `timestamp_scope=source_scan`; those are not victim times.

## Files and reproduction

`records.json` follows the repository indicator schema. `observations.csv` is a readable/importable view. `sanitized-evidence.json` retains source hashes, absolute HTML byte offsets for strict JSON flow literals, JSON pointers, task submission times, selected flow facts, certificate metadata and observation limits. `native-timing-evidence.json` contains narrow verified ELF data/call locations and instruction hashes. `validation.json` records finite checks. Hypotheses and shared services remain in their own categories; evidence confidence is distinct from maliciousness confidence. `evidence_score_hint` is advisory, with no user `manual_score` override.

The public collector is restricted to HTTPS on `tria.ge`, `urlscan.io`, `crt.sh` and `www.cloudflare.com`; redirects outside that allowlist are blocked. It uses fixed exact artifact/report seeds, timeouts, per-artifact size limits and atomic successful writes. It does not submit scans or access actor/victim endpoints. Raw captures stay in a private working folder outside the publication.

To reproduce using new public captures in a private working folder:

```text
python scripts/extract_public_sandbox_cti.py --capture-root work/public-cti-captures --out work/reproduction/independent-enrichment --fetch
python scripts/build_independent_records.py --root work/reproduction
```

Install `requirements-research.txt` in a local virtual environment. `cryptography` is required to parse public X.509 certificate bytes. Omit `--fetch` to process previously captured files entirely offline. Public reports and search windows can change; compare each collection receipt rather than expecting identical whole-page hashes. Review reproduced data before replacing published records; the map workflow never runs this collector. Native confirmation is optional and requires the previously acquired exact ELF, which is intentionally not distributed:

```text
python scripts/extract_native_retry.py --sample PATH_TO_EXACT_CBF1045_SAMPLE --out independent-enrichment/native-timing-evidence.json
```

Do not publish raw HTML, full network requests, cookies, token values, malware binaries or failed authenticated responses. No broad production detection rule or victim/India attribution is made from this collection.
