# Adding or correcting a report

1. Copy `templates/report-README.md` and `templates/indicators.csv` into `reports/YYYY/YYYY-MM-DD-short-title/`.
2. Supply exact primary-source evidence, role, confidence scope and separate publication/activity/retrieval dates. Do not import unrelated campaigns or silently change provenance.
3. Keep software fingerprints, supporting tools, deployment leads and unresolved claims in their research categories. India tagging needs target evidence, not IP hosting geography.
4. For the indexed dataset, update the appropriate JSON shard and compact CSV/master consistently. Do not make first-ever/global novelty or live-C2 claims without evidence.
5. Run `python scripts/update_manifest.py` and `python scripts/validate.py`. Optional local YARA compilation: `python scripts/validate.py --with-yara` (requires yara-python).

CI is offline and does not scan targets, query providers, fetch malware or require API keys. Use the correction issue template for stale/reassigned addresses or source/attribution errors.
