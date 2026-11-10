# World boundary source and viewpoint

The map uses the **Natural Earth India point of view**, via [AshKyd GeoJSON Regions](https://geojson-maps.kyd.au/countries/IND/ind), retrieved on 2026-11-10. Countries and territories outside India follow that provider's same viewpoint collection. This is a generalized third-party cartographic dataset; it is not Survey of India certification or a complete diplomatic recognition list.

The India outline includes the source dataset's Indian territorial claims, including northern Jammu and Kashmir/Ladakh areas, Aksai Chin, Shaksgam and Arunachal Pradesh. Representative location checks were retained for the original and simplified geometries. The provider folds Kosovo into Serbia but keeps Taiwan as a separate geographic feature; geographic separation in the map does not assert recognition as a sovereign state. Upstream sovereignty metadata is not used as an authoritative diplomatic list.

The geometry comes from [pinned source commit cb0234d2e0a0bf392b79f742a6c2c8d9ca35e488](https://github.com/AshKyd/geojson-regions/tree/cb0234d2e0a0bf392b79f742a6c2c8d9ca35e488/static/countries/pov/ind/10m). [Natural Earth data is public domain](https://www.naturalearthdata.com/about/terms-of-use/) and may be modified and redistributed. "Made with Natural Earth; India point of view; via AshKyd" is retained for provenance. The source scale is 1:10 million, not 10-metre accuracy.

For display, unused attributes were removed and geometry was simplified with topology preservation at 0.075 degrees, using 0.02 degrees for India. Original geometry was retained where a simplified candidate was invalid. No country affiliation fields were changed. The derived GeoJSON has 248 features and SHA256 `f16fb034333f7c07f0821cc63eeb7dd3f0818f656f0ba31ed0adcfae2c6240c8`.

The primary government references consulted for the requested India viewpoint were [Survey of India's Political Map page](https://surveyofindia.gov.in/pages/political-map-of-india) and the [MEA parliamentary answer concerning Jammu and Kashmir, Ladakh and Shaksgam](https://www.mea.gov.in/Images/CPV/RTI-02-05-03-2023-Das.pdf). These references do not confer official certification on the third-party geometry.

IP positions are approximate infrastructure geolocation, separate from boundary viewpoint. Country labels do not identify attacker nationality, victim location, ownership or maliciousness.
