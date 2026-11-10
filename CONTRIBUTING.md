# Adding or correcting a report

1. Copy `templates/report-README.md` and `templates/indicators.csv` into `reports/YYYY/YYYY-MM-DD-short-title/`.
2. Supply exact primary-source evidence, role, confidence scope and separate publication/activity/retrieval dates. Do not import unrelated campaigns or silently change provenance.
3. Keep software fingerprints, supporting tools, deployment leads and unresolved claims in their research categories. India tagging needs target evidence, not IP hosting geography.
4. For the indexed dataset, update the appropriate JSON shard and compact CSV/master consistently. Do not make first-ever/global novelty or live-C2 claims without evidence.
5. Review the changed records against their cited evidence and keep all CSV, JSON and readable report views consistent. For map changes, follow the [enrichment guide](docs/enrichment-and-map.md).

The map workflow downloads open metadata, rebuilds the selected IP inventory and publishes GitHub Pages. It does not scan indicator endpoints, fetch malware or require API keys. Use the correction issue template for stale/reassigned addresses or source/attribution errors.
