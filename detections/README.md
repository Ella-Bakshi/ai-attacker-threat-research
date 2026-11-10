# Detection rules

Twelve YARA rules identify software/assets, tool/reference builds, generated-beacon lineage or static persistence implementation. A match is not automatic proof of malicious operation or India targeting. The old transport-template rule misses the acquired HTTP beacon; broad beacon coverage is not claimed.

[Experimental Sigma](experimental/sigma/linux_screenshot_staging.yml) describes a screenshot staging chain. Backend conversion, sensor replay and production false-positive assessment remain unestablished. Static persistence/screenshot capability does not prove execution. No detection calls Censys/Shodan, scans targets or requires a key.
