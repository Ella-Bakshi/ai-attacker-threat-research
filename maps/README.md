# AI Attacker Threat Research — map

![All-category IP overview](world.svg)

The [interactive map](index.html) contains the complete unique-IP inventory, evidence filters, a searchable table, source references and CSV export. Its layout reuses the requested CCTV scanner results interface; [UI source and asset attribution](../docs/map-interface-reference.md) records the pinned reference. GitHub displays an HTML file as source; download `index.html` and open it in a browser to use the interactive view. The single file works from `file://` without an API key, external scripts, map tiles or an internet connection. If this repository is served through an existing static site, the same file can be opened there.

All evidence categories are selected initially. Numbered markers aggregate nearby estimated locations and count unique addresses. Some IPs have several roles or memberships; a shared marker is not a claim that its members belong to the same campaign. Addresses without coordinates remain in the total, table and CSV. Zero latitude/longitude is retained only when actually present in the source data.

The India C2 shortcut requires `india_campaign_c2_supported=true`, computed from C2 and India campaign evidence in the **same** original source record. Other address membership filters can combine associations from different original records and do not establish that those observations came from one campaign.

Filters cover evidence category, framework/research corpus, India targeting scope, estimated hosting country, C2 role, our derivations and minimum confidence rubric score. Presets provide all addresses, source-reported membership, our analysis and same-record India C2. A search also matches IP, ASN, network name, city, campaign and source record IDs. Country and framework bar charts filter the same population; framework memberships may overlap. Active filter chips can be removed individually.

Activate a marker or IP for evidence details and original source references. Cluster selection zooms to the group and opens a complete, paged member list with its own search; co-located addresses remain accessible at maximum zoom. Selecting an address highlights it on the map and in the inventory. Its pinned details remain accessible when filters later exclude it. View hashes preserve filters, camera and pinned address across reloads.

The table shows 100 rows per page and supports IP, score and timestamp sorting. **Export CSV** exports every selected address, including those on other pages and without coordinates. Exported text cells beginning with spreadsheet formula characters receive a leading apostrophe for safe viewing; authoritative canonical values remain in `data/ip-overview.json`.

Drag to pan, scroll over the map to zoom around the pointer, or pinch with two fingers. The map buttons zoom, fit the filtered addresses and reset to the world. Keyboard focus supports plus/minus, arrow keys and Home; markers work with Enter or Space. Escape dismisses details. The table provides the same data without map interaction. Light/dark preference is stored locally; it requires no account.

Approximate hosting location is not victim location or evidence of Indian targeting. The announcing network/ASN organization does not identify the operator, customer or verified hosting vendor. Enrichment describes the selected provider snapshot; it does not reconstruct attack-time location or ownership. Confidence scores summarize an evidence rubric, not a probability of maliciousness. Passive deployment leads, legitimate/shared services and unresolved findings must not become an automatic block list.

## Sources and boundaries

[IP Geolocation by DB-IP](https://db-ip.com) is used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). DB-IP Lite is a reduced-coverage/accuracy monthly product. The IP overview documents the actual downloaded release and hash, ASN data sources and scoring rules. The map does not perform live lookups or test whether any service is currently reachable.

The world geometry uses **Natural Earth India point of view**, sourced through [geojson-regions at a pinned commit](https://github.com/AshKyd/geojson-regions/tree/cb0234d2e0a0bf392b79f742a6c2c8d9ca35e488/static/countries/pov/ind/10m), rather than the default Natural Earth boundary viewpoint. Natural Earth source data is public domain. The reviewed local asset preserves India's requested territorial depiction and is simplified for display; it is not a Survey of India certified map. Geography depicts countries and territories without making each feature an official sovereignty/recognition assertion. Source provenance and boundary limitations are documented under `maps/assets/`. The original dataset scale is 1:10 million; “10m” does not mean 10-metre resolution.

`render-metadata.json` records input/geometry hashes, counts, timestamp, any additional display simplification and rendering limits. The reviewed simplified asset is used unchanged by the renderer's default settings.

## Rebuild

From the repository root, with Python 3.12 or later:

```text
python scripts/render_ip_map.py --root . --geometry maps/assets/world-india-view.geojson
```

The renderer uses only the Python standard library. It reads the canonical flat list in `data/ip-overview.json` and the locally reviewed GeoJSON, then writes `maps/index.html`, `maps/world.svg` and `maps/render-metadata.json`. No network access occurs. To reproduce byte-identical output, provide the same inputs and the prior UTC render timestamp:

```text
python scripts/render_ip_map.py --root . --geometry maps/assets/world-india-view.geojson --rendered-at 2026-11-10T18:00:00Z
```

Replace the example timestamp with the one recorded in the metadata being reproduced. Do not substitute unreviewed default-view boundary data. To refresh ASN and location metadata before rendering, follow the [enrichment guide](../docs/enrichment-and-map.md). Routine refreshes preserve the selected addresses in the authoritative IP CSV.
