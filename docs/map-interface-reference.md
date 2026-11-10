# AI Attacker Threat Research map interface

The interface adapts the project's requested [CCTV scanner results page](https://ella-bakshi.github.io/cctv-scanner-result/) and its [pinned public source](https://github.com/Ella-Bakshi/cctv-scanner-result/tree/b234b7533d7d10933c43727e4f858500c88d587b). The layout and styling are reused; camera data, scan claims and regulatory text are not imported.

| Reference component | Adaptation here |
|---|---|
| White/navy top bar and centered red count | Exact project title and filtered unique-IP count |
| Inter typography and light/dark variables | Same type family, weights, palette and persisted theme; font embedded locally |
| Rounded map card and density legend | World country/territory address density and classified evidence markers |
| Right-hand blue/orange bar panels | Hosting-country and framework membership facets |
| Navy tooltips and detail modal | Safe text rendering, complete cluster membership and source-attributed record details |
| Responsive content and reference footer | Mobile controls, evidence-method notes and provider/boundary attribution |

Map navigation adds pointer drag, pointer-anchored wheel zoom, touch pinch, keyboard controls, fit selection and world reset. Cluster selection zooms to its members and opens a paged, searchable complete list. Selecting an address links its map highlight, inventory row and evidence details. A pinned address remains accessible when later filters exclude it. URL hashes preserve filters, camera position and a pinned record; no server state is created.

`scripts/map-ui/` contains the source HTML, CSS, JavaScript and pure camera helpers. `scripts/render_ip_map.py` embeds them, the canonical IP data, reviewed geometry paths and the font into one standalone HTML file. It also generates the static SVG preview. No D3, font server, map tile, tracking or API request is required at runtime.

The Inter Latin variable font is distributed under the [SIL Open Font License](../maps/assets/INTER-OFL.txt). Its [source receipt](../maps/assets/INTER-SOURCE.json) identifies the downloaded asset. Names outside the included character subset use the system fallback font. The [boundary asset](../maps/assets/world-india-view.geojson) and its existing provenance are unchanged.

Country shading counts selected addresses; it is not a threat score or targeting map. Marker colors preserve evidence categories, and the India C2 preset requires the original same-record support flag. The confidence rubric, source/activity/enrichment dates and source links remain available in each record.
