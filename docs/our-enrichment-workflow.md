# How we collect and enrich evidence

Updated 11 November 2026 in India. Our contribution includes independent analysis of public artifacts and two first-party network observations. This is a bounded investigation, not an internet-wide scanning service or an exhaustive IOC feed.

| Layer | What we did | Provenance and limits |
|---|---|---|
| Primary reporting | Rechecked publisher reports and CERT-In notices, preserving exact roles and dates | External facts; hosting country does not establish Indian victims. |
| Public artifact collection | Downloaded four exact-hash sandbox reports, public CT records/certificate bytes and historical URLscan search metadata | Provider-produced telemetry; our acquisition, extraction, byte/hash checks and correlation are independent. |
| Artifact analysis | Matched six TLS flows to a vendor-listed beacon; corroborated 80 callback attempts for an acquired ELF; parsed DER certificates and verified native retry timing | Our derived observations. Attempts do not prove registration; certificate validity does not prove deployment. |
| First-party observation | Two single root GETs, one domain lookup and one normally validated TLS handshake | Our measurements: HTTP 521 and 404. No working C2, origin ownership or India association established. |
| Bulk metadata | Joined IPtoASN and DB-IP Lite locally | External ASN and approximate geolocation, with snapshot hashes and attribution. Metadata never increases threat confidence. |
| Review and release | Assigned scoped categories/confidence; checked sources, dates, secret exclusion and integrity; regenerated CSV/map | Shared CDN edges, unverified siblings, provider leads and incident IOCs remain distinct. |

See [independent enrichment](../independent-enrichment/README.md), [normalized CSV](../independent-enrichment/observations.csv), [source receipts](../independent-enrichment/source-receipts.json), [sanitized evidence](../independent-enrichment/sanitized-evidence.json) and [first-party observations](../research/first-party/README.md). Original sample configuration, public sandbox behavior and our current HTTP response are separate claims.

## Reproduce collection locally

Create a local Python environment. The artifact parser uses `cryptography` only for X.509 parsing; the seed observer uses the standard library. Keep raw captures outside publication.

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements-research.txt
.venv\Scripts\python -B scripts/extract_public_sandbox_cti.py --fetch --capture-root work/private-captures --out work/reproduction/independent-enrichment
.venv\Scripts\python -B scripts/build_independent_records.py --root work/reproduction
```

The collector uses fixed public-source seeds and a strict HTTPS/redirect allowlist. It does not submit scans or contact the referenced actor/victim endpoints. Without `--fetch`, it processes existing captures offline. Public pages and coverage windows can change: compare receipts and verify exact sample/domain relationships. Review generated candidates before incorporating them into the publication.

To intentionally repeat the two direct measurements:

```powershell
python -B scripts/observe_two_seeds.py --observe --output work/first-party-observations-new.json
```

This performs at most one GET `/` per fixed seed, follows no redirects and does not authenticate, request agent/task routes or execute malware. Normal certificate validation remains enabled. Each endpoint has a ten-second budget and a 16 KiB response-prefix limit. Exports omit response bodies and headers. These direct measurements are opt-in and **not run by GitHub Actions**.

## Review, enrich and update the map

Keep source observation, sandbox submission, certificate validity, local measurement, review and enrichment times separate. Require an explicit link between the framework, infrastructure role and India-targeting campaign before adding a framework-specific India C2. Campaign-level target intent is sufficient; successful compromise is a separate question. The [fresh source review](../india/2026-11-11-source-review.md) found no additional public indicator meeting all three conditions.

After accepting records, update the master/index and follow the [bulk enrichment setup](enrichment-and-map.md). A one-time `--seed-from-catalog` imports new literal IPs. Routine refreshes respect the CSV selection; domains are not silently resolved into malicious-IP assertions. Map details show artifact dates, original roles and our measurements. Shared CDN contexts receive zero standalone maliciousness confidence. Scores are ordinal evidence labels, not probabilities.

```powershell
python -B scripts/refresh_ip_overview.py --db-dir work/enrichment-data --seed-from-catalog
python -B scripts/render_ip_map.py --root .
```

Updating the CSV on `main` makes the existing workflow refresh open metadata and regenerate the map in a build job with read-only repository access. Separate jobs commit the generated inventory/map files and deploy GitHub Pages. The CSV remains authoritative: routine refreshes do not add catalog-only addresses or automatically promote discoveries, infer India targeting or poll commercial accounts. Current responses do not overwrite historical evidence.

## Commercial sources

IPinfo and Hunt observations belong to their providers. Browser sign-in is not an API credential. Private Hunt listing exports remain outside this public repository; restricted hosts/previews were not bypassed. The public repository contains no account-only Hunt data or private rules. [Hunt's public methods and supported exports](hunt-and-independent-methods.md) explain its larger collection model. No new Censys calls were made during this update.
