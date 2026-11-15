# Detection rules

Twelve candidate YARA rules concern software/assets, tool/reference builds, generated-beacon lineage or static persistence implementation. A match is not automatic proof of malicious operation or India targeting. The old transport-template rule misses the acquired HTTP beacon; broad beacon coverage is not claimed. The ELF-only lineage rule also misses the independently examined [Windows artifact](../research/analyst-derived/2026-11-15-cyberstrikeai-windows/cyberstrikeai-peak-review.md); its Linux CWD marker is absent. No cross-platform coverage is claimed.

Compound detector/catalog patterns remain explicitly qualified and appear in the separate unresolved export where operational efficacy is unverified. Constituent source/byte evidence does not establish production specificity.

[Experimental Sigma](experimental/sigma/linux_screenshot_staging.yml) describes a screenshot staging chain. Backend conversion, sensor replay and production false-positive assessment remain unestablished. Static persistence/screenshot capability does not prove execution. No detection calls Censys/Shodan, scans targets or requires a key.
