# Maintaining the IP overview and map

The main file is [data/ip-overview.csv](../data/ip-overview.csv). Its first five columns are **ip, timestamp, asn, hosting, location**. [JSON](../data/ip-overview.json) preserves lists and types; [source snapshots](../data/enrichment/sources.json) preserve dataset URLs, hashes, retrieval times and data-effective headers. [Coverage](../data/enrichment/summary.json) reports matched and unmatched values.

The [live map](https://ella-bakshi.github.io/ai-attacker-threat-research/) and [standalone map](../maps/index.html) include every selected IP, with filters for evidence class, framework, India campaign scope, C2 and our derivations. Domain-only C2 remains in the [separate C2 list](../india/C2-INFRASTRUCTURE.md); no current DNS result is silently converted into a historical campaign IP.

## Automatic service

The [refresh workflow](../.github/workflows/refresh-ip-map.yml) runs when `data/ip-overview.csv` changes on `main`, or through **Actions → Refresh IP overview and publish map → Run workflow**. It downloads open snapshots, fills ASN and location fields, renders HTML/SVG, runs tests, updates integrity hashes, commits generated files and deploys GitHub Pages. No Censys, Shodan or IPinfo key is required. Indicator IPs are not contacted.

To add an IP, append a row to the CSV. You may leave ASN, hosting and location blank; enrichment fills those output fields. Preserve the header. For example, the shape of a minimal import is:

```csv
ip,timestamp,asn,hosting,location
YOUR_PUBLIC_IP,YOUR_OBSERVATION_TIMESTAMP,,,
```

Replace both placeholders with real evidence. The literal placeholders are not accepted as addresses. Use an ISO timestamp with an explicit offset when you know one; otherwise preserve the source precision and explain it. Blank observation time means unknown. `enriched_at_utc` is a separate lookup time and never substitutes for an attack observation.

New CSV-only addresses enter as **unreviewed, confidence 0** with no inferred campaign or India association. An analyst may supply optional `manual_score` and `manual_confidence_basis` columns after review; the score is labeled contributor review, not independent validation. A score without a basis fails validation. Update the underlying source-attributed catalog to establish a verified campaign relationship.

The CSV is authoritative for the routine refresh: removing a row removes it from the next map. To add newly researched catalog addresses in bulk while preserving existing CSV rows, run the seed command below. The seed also includes historical IP literals found only in the full master, separately labeled `master-only-passive-lead`, with score 10; it does not promote shared CDN addresses or old software sightings to C2.

Repository updates use the workflow's scoped GitHub token; no personal access token is embedded. The refresh runs on trusted `main` pushes and manual dispatch, never on an external pull request with write access. A failed refresh leaves the prior published map available. Concurrent work uses ordinary fast-forward pushes; no force push is used.

## Run it yourself

From the repository folder, with Python 3.12 or newer:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-enrichment.txt
python -B scripts/download_enrichment_data.py --db-dir work/enrichment-data
python -B scripts/refresh_ip_overview.py --db-dir work/enrichment-data
python -B scripts/render_ip_map.py --root .
python -B -m unittest discover -s tests -p "test_*.py"
python -B scripts/update_manifest.py
python -B scripts/validate.py
```

For a first catalog-derived inventory, add `--seed-from-catalog` to the refresh command. To import a separate five-column CSV, add `--input-csv path/to/input.csv`; the output remains `data/ip-overview.csv` and JSON. `download_enrichment_data.py --reuse` verifies and reuses an existing snapshot; `--month YYYY-MM` selects a documented DB-IP release. Download failures stop the job instead of substituting fabricated metadata.

The maps need no runtime API calls. Open `maps/index.html` directly, or serve the folder with `python -m http.server 8000 --directory maps`. The CSV and geometry are embedded in the generated page. The SVG preview is static; filtering is available on the HTML map.

## What the fields mean

| Field | Meaning |
|---|---|
| `timestamp`, `timestamp_basis` | A source observation or contributor timestamp, with its stated basis. Timezone/precision is not invented. |
| `first_seen_values`, `last_seen_values` | Original source/index dates retained as lists. A provider sighting is not proof of an attack. |
| `enriched_at_utc` | Time the local snapshot lookups were performed. |
| `asn`, `asn_org`, `asn_range_start/end` | Matched inclusive network range and AS description from IPtoASN. Unrouted or unmatched ASN remains blank. |
| `hosting`, `hosting_basis` | AS network organization used as a transparent hosting/network label. It does not identify a reseller, tenant or threat operator. |
| `location`, `latitude`, `longitude`, `geo_status` | Approximate DB-IP Lite location at its snapshot. Unknown coordinates stay blank/null. |
| `country_code`, `asn_country_code` | Different provider concepts: estimated IP location versus country attached to an ASN mapping. Neither establishes targeting. |
| `record_ids`, `source_urls` | Links back to the source-attributed catalog. `MASTER-…` IDs identify deterministic type/value rows in the historical master. |
| `india_campaign_c2_supported` | C2 role and India campaign evidence exist on the same source record. Cross-record role unions cannot manufacture this relationship. |
| `self_derived` | Includes analyst derivation/verification in the source records. It does not mean newly discovered malicious infrastructure. |

## Confidence rubric

Scores are **ordinal evidence-strength labels from 0 to 100, not calibrated probabilities of maliciousness**. Geography, ASN, company name and ping response never increase a score. The strongest applicable documented evidence is shown, with the supporting record IDs; other source roles remain visible.

| Score | Default evidence tier |
|---:|---|
| 0 | Unreviewed CSV input, legitimate shared service or explicitly nonindicative context |
| 10 | Unresolved attribution or a historical master-only passive lead |
| 20 | Passive software/deployment candidate or reference fingerprint |
| 55 | Source-reported historical campaign infrastructure/context |
| 60 | Our exact sample configuration, inspected statically; live operation unverified |
| 70 | Primary source reports the incident or campaign C2 role; present-day activity unverified |

Manual reviewed scores are separately labeled and require a written basis. A rebuild changes enrichment metadata, not the underlying threat assessment merely because an IP now belongs to another network.

## Data sources and location checks

- [IPtoASN](https://iptoasn.com/): open bulk range-to-AS mappings, licensed [PDDL 1.0](https://opendatacommons.org/licenses/pddl/1-0/). The website describes hourly updates; the actual retrieved file's `Last-Modified` header is retained rather than assuming the dump is current to the lookup second.
- [IP Geolocation by DB-IP](https://db-ip.com): [City Lite](https://db-ip.com/db/download/ip-to-city-lite), monthly, reduced coverage/accuracy, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This repository publishes a transformed matched subset and English labels, with attribution. Approximate hosting locations are not victim locations or attack-time locations.
- [Finite IPinfo cross-checks](../data/enrichment/ipinfo-cross-checks.json): read-only profile review, including existing provider measurements on two reported C2 addresses. No new measurement was initiated. Provider measurement dates and review times remain separate; they do not confirm that a historical C2 address is still malicious.
- [Boundary provenance and limitations](../maps/assets/BOUNDARY-NOTE.md): Natural Earth India point of view, pinned and tested. Country/territory labels from IP data are not a blanket statement of diplomatic recognition. The asset is not Survey of India certification.

For optional IPinfo automation, its [official Lite API documentation](https://ipinfo.io/developers/lite-api) describes basic ASN and country/continent data; Lite does not provide city coordinates or logged-in ProbeNet evidence. Use your own token in a local environment variable or GitHub Actions secret and check your plan's use/redistribution terms. Browser sign-in is not an API token and is never scraped by this pipeline. This repository's default bulk pipeline works without that optional service.
