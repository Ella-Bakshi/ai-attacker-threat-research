# Detection rules

Twelve YARA rules identify software/assets, tool/reference builds, generated-beacon lineage or static persistence implementation. A match is not automatic proof of malicious operation or India targeting. Finite validation results are in [validation](validation). The old transport-template rule misses the acquired HTTP beacon; only rules with relevant positives should be used for that sample.

[Experimental Sigma](experimental/sigma/linux_screenshot_staging.yml) describes a screenshot staging chain. YAML/synthetic control checks passed; no backend conversion, sensor replay or production false-positive assessment was performed. Static persistence/screenshot capability does not prove execution. No detection calls Censys/Shodan, scans targets or requires a key.
