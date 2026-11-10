# Indicator record fields

The machine definition is [indicator.schema.json](../schemas/indicator.schema.json). Each file in the [JSON index](../data/index.json) is an array of these records. [Compact catalog](../data/catalog.csv) omits large evidence arrays, which remain in the JSON shards.

| Fields | Meaning |
|---|---|
| record_id, framework, publication_category | Stable record identity and evidence category |
| indicator_type, indicator, indicator_defanged | Canonical machine observable and readable network rendering |
| role, association_scope | What the value is reported or statically shown to do |
| confidence, confidence_scope, evidence_confidence | Scoped assessment; not a measured detection percentage |
| verification_status, origin, analyst_contribution | External report, local static derivation, identity check or passive provider evidence |
| source_published_date, first_seen, last_seen | Publisher date separately from source activity/index observations; unknown remains blank |
| primary_source_url, source_references | Original references, source roles, hashes and supporting byte/function evidence |
| india_relevance, india_evidence_url, india_evidence_basis | Geographic relationship and its exact supporting evidence |
| per_indicator_india_targeting_confirmed | Whether an individual indicator has supported India-targeting evidence; currently false throughout |
| limitations, recommended_use | Context, conditional behavior and no-automatic-block constraints |

Per-family research views and report-local exports can overlap; do not sum them as unique malicious systems. The master deduplicates by type/value, while record identity also preserves framework/category differences.
