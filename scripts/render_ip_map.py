#!/usr/bin/env python3
"""Render an offline IP evidence map and static SVG; no network access or dependencies.

Input: data/ip-overview.json (a flat list of canonical-IP records).
Geometry: a reviewed India-view GeoJSON supplied locally. This script never downloads
or substitutes a default boundary dataset. All displayed text remains untrusted data.
"""
import argparse
import collections
import datetime as dt
import hashlib
import html
import ipaddress
import json
import math
import re
from pathlib import Path

WIDTH, HEIGHT = 1200, 600


def safe_json(value):
    """JSON safe inside an HTML script data element (including hostile </script>)."""
    return (json.dumps(value, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
            .replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e')
            .replace('\u2028', '\\u2028').replace('\u2029', '\\u2029'))


def coordinate(record):
    lat, lon = record.get('latitude'), record.get('longitude')
    if isinstance(lat, bool) or isinstance(lon, bool):
        return None
    if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
        return None
    if not math.isfinite(lat) or not math.isfinite(lon) or not -90 <= lat <= 90 or not -180 <= lon <= 180:
        return None
    return ((lon + 180) * WIDTH / 360, (90 - lat) * HEIGHT / 180)


def simplify(points, tolerance):
    """Iterative Douglas-Peucker for display paths; original GeoJSON stays unchanged."""
    if len(points) <= 4 or not tolerance:
        return points
    closed = points[0] == points[-1]
    # A closed ring's initial coincident ends are fine: select its farthest vertex,
    # then continue the two branches. At least three distinct vertices are retained.
    keep = {0, len(points) - 1}
    stack = [(0, len(points) - 1)]
    limit = tolerance * tolerance
    while stack:
        start, end = stack.pop()
        ax, ay = points[start][:2]
        bx, by = points[end][:2]
        dx, dy = bx - ax, by - ay
        denom = dx * dx + dy * dy
        furthest, maximum = None, limit
        for idx in range(start + 1, end):
            px, py = points[idx][:2]
            t = max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / denom)) if denom else 0
            distance = (px - ax - t * dx) ** 2 + (py - ay - t * dy) ** 2
            if distance > maximum:
                furthest, maximum = idx, distance
        if furthest is not None:
            keep.add(furthest)
            stack.extend(((start, furthest), (furthest, end)))
    result = [points[i] for i in sorted(keep)]
    return points if closed and len(result) < 4 else result


def paths_from_geometry(geometry, tolerance):
    features = geometry.get('features', []) if geometry.get('type') == 'FeatureCollection' else [{'geometry': geometry}]
    output, ring_count, original_points, display_points = [], 0, 0, 0
    for feature in features:
        shape = feature.get('geometry') or {}
        kind, coords = shape.get('type'), shape.get('coordinates', [])
        polygons = [coords] if kind == 'Polygon' else coords if kind == 'MultiPolygon' else []
        pieces = []
        for polygon in polygons:
            for ring in polygon:
                if len(ring) < 4:
                    continue
                for point in ring:
                    if len(point) < 2 or not all(isinstance(v, (int, float)) and math.isfinite(v) for v in point[:2]):
                        raise ValueError('Non-finite or nonnumeric geometry coordinate')
                    if not -180.00001 <= point[0] <= 180.00001 or not -90.00001 <= point[1] <= 90.00001:
                        raise ValueError('Geometry outside geographic WGS84 coordinate bounds')
                reduced = simplify(ring, tolerance)
                ring_count += 1
                original_points += len(ring)
                display_points += len(reduced)
                path = []
                for index, (lon, lat, *_) in enumerate(reduced):
                    x, y = (lon + 180) * WIDTH / 360, (90 - lat) * HEIGHT / 180
                    path.append(('M' if index == 0 else 'L') + f'{x:.2f},{y:.2f}')
                pieces.append(' '.join(path) + ' Z')
        if pieces:
            output.append('<path d="' + ' '.join(pieces) + '"/>')
    if not output:
        raise ValueError('No polygon countries in geometry')
    return '\n'.join(output), dict(features=len(output), rings=ring_count, original_vertices=original_points,
                                  displayed_vertices=display_points, simplification_degrees=tolerance)


def normalize_records(records):
    if not isinstance(records, list):
        raise ValueError('data/ip-overview.json must contain a flat list')
    addresses = set()
    lists = ('publication_categories', 'frameworks', 'campaigns', 'network_roles', 'india_targeting_scopes', 'record_ids', 'source_urls')
    output = []
    for row in records:
        if not isinstance(row, dict) or not row.get('ip'):
            raise ValueError('Every record needs an IP')
        address = str(ipaddress.ip_address(row['ip']))
        if address != row['ip'] or address in addresses:
            raise ValueError('IP values must be canonical and unique: ' + address)
        addresses.add(address)
        result = dict(row)
        for field in lists:
            value = row.get(field, [])
            if not isinstance(value, list) or any(not isinstance(x, str) for x in value):
                raise ValueError(field + ' must be an array of strings')
            result[field] = sorted(set(value))
        if 'india_campaign_c2_supported' in row and not isinstance(row['india_campaign_c2_supported'], bool):
            raise ValueError('india_campaign_c2_supported must be boolean')
        if not isinstance(row.get('self_derived', False), bool):
            raise ValueError('self_derived must be boolean')
        result['self_derived'] = row.get('self_derived', False)
        score = row.get('confidence_score')
        if score is not None and (isinstance(score, bool) or not isinstance(score, (int, float)) or not math.isfinite(score) or not 0 <= score <= 100):
            raise ValueError('confidence_score must be null or numeric 0–100')
        lat, lon = row.get('latitude'), row.get('longitude')
        if (lat is not None or lon is not None) and coordinate(row) is None:
            raise ValueError('Coordinates must be a valid pair, or both null: ' + address)
        output.append(result)
    return sorted(output, key=lambda r: (ipaddress.ip_address(r['ip']).version, int(ipaddress.ip_address(r['ip']))))


def static_svg(records, world, metadata):
    bins = collections.defaultdict(list)
    for row in records:
        point = coordinate(row)
        if point is not None:
            bins[(int(point[0] // 36), int(point[1] // 36))].append(point)
    mapped = sum(len(v) for v in bins.values())
    markers = []
    for points in bins.values():
        x = sum(p[0] for p in points) / len(points)
        y = sum(p[1] for p in points) / len(points)
        radius = min(17, 4 + math.log2(len(points) + 1) * 1.5)
        markers.append(f'<g><title>{len(points)} unique IPs; approximate cluster position</title><circle cx="{x:.2f}" cy="{y:.2f}" r="{radius:.2f}" fill="#168b94" fill-opacity=".87" stroke="#d9fbf4" stroke-width=".7"/>' +
                       (f'<text x="{x:.2f}" y="{y + 3.5:.2f}" text-anchor="middle" fill="white" font-size="10" font-family="sans-serif" font-weight="bold">{len(points)}</text>' if len(points) > 1 else '') + '</g>')
    title = f'{len(records):,} unique IPs · {mapped:,} located · {len(records)-mapped:,} without coordinates'
    caption = 'Approximate hosting estimates; not victim locations or proof of malicious activity. All evidence categories included.'
    source = 'India-view boundaries: Natural Earth via geojson-regions; display paths simplified. IP Geolocation by DB-IP (CC BY 4.0).'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 750" role="img" aria-labelledby="title desc">
<title id="title">IP evidence overview — all categories</title><desc id="desc">{html.escape(title+'. '+caption+' '+source)}</desc>
<metadata>{html.escape(json.dumps(metadata, ensure_ascii=False, allow_nan=False))}</metadata>
<rect width="1200" height="750" fill="#0c1b2b"/><text x="24" y="35" fill="#f1f6fd" font-size="22" font-family="sans-serif" font-weight="bold">IP evidence overview</text>
<text x="24" y="62" fill="#a9bfd6" font-size="15" font-family="sans-serif">{title}</text>
<svg x="0" y="78" width="1200" height="600" viewBox="0 0 1200 600"><g fill="#253c50" stroke="#7890a4" stroke-width=".32" fill-rule="evenodd">{world}</g>{''.join(markers)}</svg>
<rect x="0" y="690" width="1200" height="60" fill="#0c1b2b"/>
<text x="24" y="710" fill="#c9d8e8" font-size="12" font-family="sans-serif">{html.escape(caption)}</text>
<a href="https://db-ip.com"><text x="24" y="733" fill="#91d8df" font-size="11" font-family="sans-serif">{html.escape(source)}</text></a></svg>'''


STYLE = r'''
:root{color-scheme:dark;--bg:#091522;--panel:#112338;--line:#284057;--muted:#a9bfd2;--text:#edf4fb;--accent:#74e0d5}*{box-sizing:border-box}body{margin:0;overflow-wrap:anywhere;background:var(--bg);color:var(--text);font:15px/1.5 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}main{max-width:1500px;margin:auto;padding:28px}h1{font-size:clamp(27px,4vw,42px);line-height:1.15;margin:8px 0 12px}h2{font-size:19px;margin:0 0 12px}h3{font-size:16px;margin:10px 0}p{margin:8px 0}.eyebrow{letter-spacing:.13em;font-size:12px;color:var(--accent);font-weight:700}.intro{max-width:1040px;color:var(--muted)}a{color:#8de9df}button,input,select{font:inherit}button,select,input{color:var(--text);background:#0c1c2d;border:1px solid #49657d;border-radius:6px;padding:9px 11px;min-height:42px}button{cursor:pointer}button:hover{border-color:var(--accent);background:#183c4c}button:disabled{opacity:.4;cursor:default}input[type=checkbox]{min-height:auto;accent-color:var(--accent)}input[type=range]{padding:0;accent-color:var(--accent)}:focus-visible{outline:3px solid #fae38b;outline-offset:3px}label{display:flex;flex-direction:column;gap:5px;font-size:13px;color:var(--muted)}.panel{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:18px;margin-top:18px}.filters{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}.filters input,.filters select{width:100%;min-width:0}.check{flex-direction:row;align-items:center;gap:8px}.controls{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:14px}.pill{border-radius:20px;padding:7px 12px}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:18px 0 0}.stat{background:#142b40;border-radius:8px;padding:13px}.stat strong{font-size:26px;line-height:1.2;display:block}.stat span{font-size:12px;color:var(--muted)}.maphead{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}.maphead .controls{margin:0}.mapframe{position:relative;overflow:hidden;background:#0c1b2b;border:1px solid #35506a;border-radius:8px;margin-top:12px}#map{width:100%;height:auto;display:block;aspect-ratio:2/1;touch-action:pan-y}#land{fill:#253c50;stroke:#7890a4;stroke-width:.32;fill-rule:evenodd}.marker{cursor:pointer}.marker:focus-visible circle{stroke:#fae38b;stroke-width:2}.legend{display:flex;gap:12px;flex-wrap:wrap;margin:10px 0;color:var(--muted);font-size:12px}.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:5px}.note{font-size:13px;color:var(--muted)}.grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:18px}.country-list{display:grid;grid-template-columns:1fr 1fr;gap:7px}.country{position:relative;text-align:left;overflow:hidden;font-size:13px;padding:8px 10px;isolation:isolate}.country:before{content:"";position:absolute;inset:0 auto 0 0;width:var(--bar);background:#1b4853;z-index:-1}.country b{float:right}.details{word-break:break-word}.details dl{display:grid;grid-template-columns:120px minmax(0,1fr);gap:6px;margin:8px 0}.details dt{color:var(--muted)}.details dd{margin:0}.ip-list{display:flex;flex-wrap:wrap;gap:6px}.ip-list button{font:12px ui-monospace,monospace;min-height:34px;padding:5px 8px}.scroll{overflow:auto;max-width:100%;max-height:650px}table{border-collapse:collapse;width:100%;font-size:13px;min-width:1080px}th,td{padding:11px 10px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}th{color:var(--muted);font-size:12px;position:sticky;top:0;background:var(--panel);z-index:1}td button{font:13px ui-monospace,monospace;min-height:34px;padding:4px 7px}.pagination{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:12px}.pagination .controls{margin:0}.empty{padding:18px;color:var(--muted)}footer{margin:22px 0;color:var(--muted);font-size:12px}summary{cursor:pointer}details ul{padding-left:20px}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}@media(max-width:800px){main{padding:18px}.filters{grid-template-columns:1fr 1fr}.grid{grid-template-columns:1fr}.country-list{grid-template-columns:1fr 1fr}}@media(max-width:420px){main{padding:10px}.panel{padding:12px}.filters{grid-template-columns:1fr}.stats{grid-template-columns:1fr 1fr}.country-list{grid-template-columns:1fr}.maphead h2{margin:0}.maphead button{padding:8px 10px}.details dl{grid-template-columns:90px minmax(0,1fr)}.pagination{align-items:flex-start;flex-direction:column}}
'''


BODY = r'''
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="referrer" content="no-referrer"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; connect-src 'none'; base-uri 'none'; object-src 'none'; form-action 'none'"><title>IP evidence atlas · AI Attacker Threat Research</title><style>__STYLE__</style></head>
<body><main><header><div class="eyebrow">AI ATTACKER THREAT RESEARCH / PASSIVE ENRICHMENT</div><h1>IP evidence atlas</h1><p class="intro">Explore every collected address, including source-reported incident indicators, independently inspected endpoints, passive deployment leads and unresolved findings. These categories carry different evidence; a plotted address does not establish malicious activity or a currently reachable service.</p><p class="note" id="snapshot"></p></header>
<section class="panel" aria-labelledby="filter-title"><h2 id="filter-title">Filter the evidence</h2><div class="filters">
<label>Evidence category<select id="category"><option value="">All categories</option></select></label><label>Framework / research corpus<select id="framework"><option value="">All frameworks</option></select></label><label>India evidence scope<select id="india"><option value="">All targeting scopes</option><option value="__supported__">India-linked campaign / targeting evidence</option><option value="__c2supported__">India campaign C2 · same-record support</option></select></label><label>Estimated hosting country<select id="country"><option value="">All hosting countries</option></select></label>
<label>Network role<select id="role"><option value="">All network roles</option><option value="__c2__">Reported / identified C2 role</option></select></label><label>Search IP, ASN, host, city, campaign<input id="search" type="search" placeholder="Address or evidence text" autocomplete="off"></label><label>Minimum rubric score: <span id="score-label">0 / 100</span><input id="score" type="range" min="0" max="100" step="1" value="0"></label><label class="check"><input id="self" type="checkbox"> Our static/sample-derived addresses only</label></div>
<div class="controls"><button class="pill" id="all">All addresses</button><button class="pill" id="india-c2">India-linked campaign C2</button><button class="pill" id="own">Our derived addresses</button><button id="download">Download selected CSV</button></div><p class="note">Confidence scores apply a documented evidence rubric; they are not probabilities of maliciousness. Unknown scores are included at minimum 0. India filters use campaign/targeting evidence, never server geography. The India C2 shortcut requires support in the same source record; other membership filters may combine separate records for one address.</p></section>
<div class="stats" aria-live="polite" aria-atomic="true"><div class="stat"><strong id="selected-count">0</strong><span>selected unique IPs</span></div><div class="stat"><strong id="located-count">0</strong><span>with estimated coordinates</span></div><div class="stat"><strong id="unknown-count">0</strong><span>without coordinates · retained in table</span></div><div class="stat"><strong id="self-count">0</strong><span>our derived addresses in selection</span></div></div>
<section class="panel" aria-labelledby="map-title"><div class="maphead"><h2 id="map-title">Approximate hosting geography</h2><div class="controls"><button id="zoom-in" aria-label="Zoom map in">Zoom +</button><button id="zoom-out" aria-label="Zoom map out">Zoom −</button><button id="reset-map">Reset map</button></div></div><div class="mapframe"><svg id="map" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600" role="group" aria-labelledby="map-title map-desc" tabindex="0"><desc id="map-desc">Approximate IP hosting locations. Numbered markers aggregate addresses; activate one to inspect its members. Use zoom buttons, or plus/minus and arrow keys when this map is focused. The table provides the same addresses without requiring map interaction.</desc><g id="land">__WORLD__</g><g id="markers"></g></svg></div>
<div class="legend"><span><i class="dot" style="background:#eb9665"></i>Sourced incident membership</span><span><i class="dot" style="background:#65bce8"></i>Our derived membership</span><span><i class="dot" style="background:#d6b85b"></i>Deployment leads</span><span><i class="dot" style="background:#bc9ce6"></i>Unverified / other research</span><span><i class="dot" style="background:#168b94"></i>Multiple IPs / mixed evidence</span></div>
<p class="note">Single-IP colors prioritize sourced incident membership, then our derivation, then deployment leads; details retain every membership. Numbered markers aggregate multiple IPs without assigning one campaign.</p><p class="note" id="map-status" aria-live="polite"></p><p class="note"><strong>Hosting estimate ≠ victim location.</strong> Coordinates are provider estimates from the stated database snapshot. Network/ASN organization does not identify the campaign operator or prove which hosting customer used an address. Current enrichment does not establish attack-time location or ownership.</p><p class="note">India-view boundary rendering is provided for the requested map presentation; geometry and simplification provenance are recorded in the renderer metadata. <a href="https://db-ip.com" target="_blank" rel="noopener noreferrer">IP Geolocation by DB-IP</a> · CC BY 4.0.</p></section>
<div class="grid"><section class="panel" aria-labelledby="countries-title"><h2 id="countries-title">Selected IPs by estimated hosting country</h2><div id="country-list" class="country-list"></div><p class="note">Top 12 groups, counting unique selected addresses. Use the country filter for every group. Unknown country is retained. These are hosting estimates, not targeted countries.</p></section><section class="panel details" id="details" tabindex="-1" aria-labelledby="details-title"><h2 id="details-title">Address / cluster details</h2><div id="detail-body"><p class="note">Choose a numbered marker or an IP in the table. Sources, original roles, confidence basis and record references appear here.</p></div></section></div>
<section class="panel" aria-labelledby="table-title"><div class="maphead"><h2 id="table-title">Selected address inventory</h2><span class="note">100 rows per page · CSV contains all selected rows</span></div><div class="scroll"><table><caption class="sr-only">Filtered unique IP inventory. Activate an IP to view its complete evidence and source links.</caption><thead><tr><th scope="col">IP / details</th><th scope="col">Evidence category</th><th scope="col">Framework / corpus</th><th scope="col">ASN / announcing network</th><th scope="col">Estimated location</th><th scope="col">Rubric score</th><th scope="col">Timestamp</th></tr></thead><tbody id="rows"></tbody></table></div><div class="pagination"><span id="page-status" class="note" aria-live="polite"></span><div class="controls"><button id="previous">Previous</button><button id="next">Next</button></div></div></section>
<footer><details><summary>Data sources, boundary provenance and use limits</summary><p id="provenance"></p><p>No external libraries, map tiles, API calls, target requests or keys are required after opening this file. Source links open only when you choose them. Unlocated IPs remain in counts, table and export. This is an evidence inventory; it is not an automatic block list.</p><p>For enrichment source snapshot identities, scoring rules and original indicator provenance, consult the repository IP overview documentation and source record crosslinks. Renderer metadata: <code>maps/render-metadata.json</code>.</p></details></footer>
</main><script id="ip-data" type="application/json">__DATA__</script><script id="render-meta" type="application/json">__META__</script><script>__SCRIPT__</script></body></html>
'''


SCRIPT = r'''
'use strict';
const DATA=JSON.parse(document.getElementById('ip-data').textContent);
const META=JSON.parse(document.getElementById('render-meta').textContent);
const $=id=>document.getElementById(id), NS='http://www.w3.org/2000/svg';
const W=1200,H=600,PAGE=100;
let selected=[],page=0,view={x:0,y:0,w:W,h:H},renderedGroups=[];
const controls=['category','framework','india','country','role','search','score','self'];
const text=(tag,value,cls)=>{const n=document.createElement(tag);n.textContent=String(value??'Unknown');if(cls)n.className=cls;return n;};
const arr=(r,key)=>Array.isArray(r[key])?r[key]:[];
const flat=x=>Array.isArray(x)?x.join('; '):x!==null&&typeof x==='object'?JSON.stringify(x):String(x??'');
const located=r=>typeof r.latitude==='number'&&Number.isFinite(r.latitude)&&Math.abs(r.latitude)<=90&&typeof r.longitude==='number'&&Number.isFinite(r.longitude)&&Math.abs(r.longitude)<=180;
const point=r=>({x:(r.longitude+180)*W/360,y:(90-r.latitude)*H/180});
const countryKey=r=>r.country_code||'__unknown__';
const countryName=r=>r.country_name||r.country_code||'Unknown country';
const isIndia=r=>arr(r,'india_targeting_scopes').some(s=>['campaign','campaign_scope_only','targeting_supported'].includes(s));
const isC2=r=>arr(r,'network_roles').some(s=>/\bc2\b|command[\s-]*(?:and[\s-]*)?control/i.test(s));
const addOption=(node,value,label)=>{const o=document.createElement('option');o.value=value;o.textContent=label;node.append(o);};
for(const [id,key]of[['category','publication_categories'],['framework','frameworks'],['india','india_targeting_scopes'],['role','network_roles']]){
  [...new Set(DATA.flatMap(r=>arr(r,key)))].sort().forEach(v=>addOption($(id),v,v));
}
const countries=new Map();for(const r of DATA)countries.set(countryKey(r),countryName(r));
[...countries].sort((a,b)=>a[1].localeCompare(b[1])).forEach(([key,name])=>addOption($('country'),key,name));
$('snapshot').textContent=`${DATA.length.toLocaleString()} unique addresses · rendered ${META.rendered_at_utc} · timestamps in rows retain their documented source/enrichment meaning.`;
$('provenance').textContent=`Boundary source: ${META.geometry_source}. Display simplification: ${META.geometry_display.simplification_degrees} degrees; original geometry SHA-256 ${META.geometry_sha256}. Input SHA-256 ${META.input_sha256}. Geolocation values: DB-IP Lite; ASN and other enrichment provenance remain in the input documentation.`;

function matches(r){
  if($('category').value&&!arr(r,'publication_categories').includes($('category').value))return false;
  if($('framework').value&&!arr(r,'frameworks').includes($('framework').value))return false;
  const india=$('india').value;if(india&&(india==='__c2supported__'?r.india_campaign_c2_supported!==true:india==='__supported__'?!isIndia(r):!arr(r,'india_targeting_scopes').includes(india)))return false;
  if($('country').value&&countryKey(r)!==$('country').value)return false;
  const role=$('role').value;if(role&&(role==='__c2__'?!isC2(r):!arr(r,'network_roles').includes(role)))return false;
  if($('self').checked&&!r.self_derived)return false;
  const minimum=Number($('score').value);if(minimum>0&&(typeof r.confidence_score!=='number'||r.confidence_score<minimum))return false;
  const query=$('search').value.trim().toLowerCase();
  return !query||[r.ip,r.asn,r.hosting,r.country_name,r.country_code,r.city,...arr(r,'frameworks'),...arr(r,'campaigns'),...arr(r,'network_roles'),...arr(r,'record_ids')].map(flat).join(' ').toLowerCase().includes(query);
}
function color(r){
  const cats=arr(r,'publication_categories');
  if(cats.some(s=>['main-iocs','sourced-iocs'].includes(s)))return '#eb9665';
  if(r.self_derived)return '#65bce8';
  if(cats.some(s=>/deployment/.test(s)))return '#d6b85b';
  return '#bc9ce6';
}
function update(){
  selected=DATA.filter(matches);page=0;
  const count=selected.filter(located).length;
  $('selected-count').textContent=selected.length.toLocaleString();$('located-count').textContent=count.toLocaleString();$('unknown-count').textContent=(selected.length-count).toLocaleString();$('self-count').textContent=selected.filter(r=>r.self_derived).length.toLocaleString();
  $('score-label').textContent=$('score').value+' / 100';$('download').disabled=!selected.length;
  drawMap();drawCountries();drawTable();
  $('detail-body').replaceChildren(text('p','Choose a marker or IP to view evidence in this selection.','note'));
}
function resetFilters(){for(const id of controls){if(id==='self')$(id).checked=false;else $(id).value=id==='score'?'0':'';}}
controls.forEach(id=>$(id).addEventListener(id==='search'||id==='score'?'input':'change',update));
$('all').addEventListener('click',()=>{resetFilters();resetMap(false);update();});
$('india-c2').addEventListener('click',()=>{resetFilters();$('india').value='__c2supported__';resetMap(false);update();});
$('own').addEventListener('click',()=>{resetFilters();$('self').checked=true;resetMap(false);update();});
function clampView(){view.w=Math.max(50,Math.min(W,view.w));view.h=view.w*H/W;view.x=Math.max(0,Math.min(W-view.w,view.x));view.y=Math.max(0,Math.min(H-view.h,view.y));}
function zoom(factor){const next=Math.max(50,Math.min(W,view.w*factor));view.x+=(view.w-next)/2;view.y+=(view.h-next*H/W)/2;view.w=next;clampView();drawMap();}
function resetMap(draw=true){view={x:0,y:0,w:W,h:H};if(draw)drawMap();}
$('zoom-in').addEventListener('click',()=>zoom(.65));$('zoom-out').addEventListener('click',()=>zoom(1/.65));$('reset-map').addEventListener('click',()=>resetMap());
$('map').addEventListener('keydown',event=>{if(event.target!==$('map'))return;let handled=true;switch(event.key){case '+':case '=':zoom(.65);break;case '-':zoom(1/.65);break;case 'ArrowLeft':view.x-=view.w*.12;break;case 'ArrowRight':view.x+=view.w*.12;break;case 'ArrowUp':view.y-=view.h*.12;break;case 'ArrowDown':view.y+=view.h*.12;break;case 'Home':resetMap(false);break;default:handled=false;}if(handled){event.preventDefault();clampView();drawMap();}});
function drawMap(){
  $('map').setAttribute('viewBox',`${view.x} ${view.y} ${view.w} ${view.h}`);
  const units=view.w/Math.max(280,$('map').getBoundingClientRect().width),cell=34*units,bins=new Map();let outside=0;
  for(const r of selected){if(!located(r))continue;const p=point(r);if(p.x<view.x||p.x>view.x+view.w||p.y<view.y||p.y>view.y+view.h){outside++;continue;}const key=Math.floor(p.x/cell)+','+Math.floor(p.y/cell);if(!bins.has(key))bins.set(key,[]);bins.get(key).push(r);}
  let groups=[...bins.values()].map(rows=>({rows,xsum:rows.reduce((s,r)=>s+point(r).x,0),ysum:rows.reduce((s,r)=>s+point(r).y,0)}));
  // Merge adjacent grid clusters whose labels would collide at this viewport size.
  const threshold=(36*units)**2;
  for(let pass=0;pass<10;pass++){const merged=[];let changed=false;for(const group of groups){const x=group.xsum/group.rows.length,y=group.ysum/group.rows.length;let nearest=null,best=threshold;for(const candidate of merged){const dx=x-candidate.xsum/candidate.rows.length,dy=y-candidate.ysum/candidate.rows.length,distance=dx*dx+dy*dy;if(distance<best){nearest=candidate;best=distance;}}if(nearest){nearest.rows.push(...group.rows);nearest.xsum+=group.xsum;nearest.ysum+=group.ysum;changed=true;}else merged.push(group);}groups=merged;if(!changed)break;}
  renderedGroups=groups.map(group=>group.rows);const fragment=document.createDocumentFragment();
  for(const rows of renderedGroups){const positions=rows.map(point),x=positions.reduce((s,p)=>s+p.x,0)/rows.length,y=positions.reduce((s,p)=>s+p.y,0)/rows.length,g=document.createElementNS(NS,'g'),circle=document.createElementNS(NS,'circle'),title=document.createElementNS(NS,'title');
    g.setAttribute('class','marker');g.setAttribute('role','button');g.setAttribute('tabindex','0');g.setAttribute('aria-label',`${rows.length} unique IP${rows.length===1?'':'s'}; open ${rows.length===1?rows[0].ip:'cluster'} details`);
    title.textContent=`${rows.length} unique IP${rows.length===1?'':'s'} · ${[...new Set(rows.map(countryName))].slice(0,4).join(', ')}. Activate to inspect evidence.`;
    circle.setAttribute('cx',x);circle.setAttribute('cy',y);circle.setAttribute('r',(rows.length===1?5:Math.min(17,9+Math.log2(rows.length+1)))*units);circle.setAttribute('fill',rows.length===1?color(rows[0]):'#168b94');circle.setAttribute('stroke','#d9fbf4');circle.setAttribute('stroke-width',.7*units);g.append(title,circle);
    if(rows.length>1){const label=document.createElementNS(NS,'text');label.setAttribute('x',x);label.setAttribute('y',y+4*units);label.setAttribute('text-anchor','middle');label.setAttribute('font-size',12*units);label.setAttribute('font-weight','700');label.setAttribute('fill','white');label.setAttribute('pointer-events','none');label.textContent=rows.length;g.append(label);}
    const activate=()=>showGroup(rows);g.addEventListener('click',activate);g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();activate();}});fragment.append(g);
  }
  $('markers').replaceChildren(fragment);$('map-status').textContent=`${renderedGroups.length.toLocaleString()} visible markers represent ${renderedGroups.reduce((s,r)=>s+r.length,0).toLocaleString()} located selected IPs. ${outside.toLocaleString()} additional located IPs are outside the zoomed viewport. Marker numbers count unique IPs; cluster positions summarize approximate provider coordinates.`;
}
function showGroup(rows){
  if(rows.length===1){showRecord(rows[0]);return;}
  const body=$('detail-body');body.replaceChildren(text('h3',`${rows.length.toLocaleString()} unique IPs in this cluster`),text('p','A cluster may combine different campaigns, roles and evidence categories. Select an IP below; all members remain in the filtered table and CSV.','note'));
  const list=text('div','','ip-list');for(const row of rows.slice(0,50)){const b=text('button',row.ip);b.addEventListener('click',()=>showRecord(row));list.append(b);}body.append(list);if(rows.length>50)body.append(text('p',`First 50 members shown here. ${rows.length-50} more are available in the table/export.`,'note'));
  $('details').focus({preventScroll:true});
}
function showRecord(r){
  const body=$('detail-body');body.replaceChildren(text('h3',r.ip));const dl=document.createElement('dl');
  const values=[['Category',arr(r,'publication_categories')],['Framework',arr(r,'frameworks')],['Campaign',arr(r,'campaigns')],['Network role',arr(r,'network_roles')],['India scope',arr(r,'india_targeting_scopes')],['India C2 link',r.india_campaign_c2_supported===true?'Supported in the same original source record':'Not established by same-record support'],['Own derivation',r.self_derived?'Yes — independent derivation/verification; not global novelty':'No'],['Rubric score',r.confidence_score==null?'Unknown':`${r.confidence_score} / 100`],['Score basis',r.confidence_basis],['ASN',r.asn],['Network',r.hosting],['Hosting estimate',[r.city,countryName(r)].filter(Boolean)],['Coordinates',located(r)?`${r.latitude}, ${r.longitude} (approximate)`:'Unknown / not plotted'],['Timestamp',r.timestamp],['Time meaning',r.timestamp_basis],['Enriched UTC',r.enriched_at_utc],['Geo snapshot',r.geo_dataset_build_utc],['ASN snapshot',r.asn_dataset_last_modified],['Geo status',r.geo_status],['Status',r.status||r.enrichment_status],['Record IDs',arr(r,'record_ids')]];
  for(const [name,value]of values){dl.append(text('dt',name),text('dd',flat(value)||'Unknown'));}body.append(dl);
  body.append(text('h3','Source references'));const ul=document.createElement('ul');let safe=0;for(const source of arr(r,'source_urls')){try{const url=new URL(source);if(!['http:','https:'].includes(url.protocol))continue;const li=document.createElement('li'),a=document.createElement('a');a.href=url.href;a.target='_blank';a.rel='noopener noreferrer';a.textContent=source;li.append(a);ul.append(li);safe++;}catch{}}
  body.append(safe?ul:text('p','See source record IDs and the original inventory for source locators.','note'));$('details').focus({preventScroll:true});
}
function drawCountries(){
  const counts=new Map();for(const row of selected){const key=countryKey(row);if(!counts.has(key))counts.set(key,{name:countryName(row),count:0});counts.get(key).count++;}
  const entries=[...counts].sort((a,b)=>b[1].count-a[1].count||a[1].name.localeCompare(b[1].name)).slice(0,12),max=entries.length?entries[0][1].count:1;
  const fragment=document.createDocumentFragment();for(const [key,group]of entries){const button=text('button',group.name,'country');button.style.setProperty('--bar',(group.count/max*100)+'%');button.append(text('b',group.count.toLocaleString()));button.setAttribute('aria-label',`Filter estimated hosting country ${group.name}, ${group.count} selected unique IPs`);button.addEventListener('click',()=>{$('country').value=key;update();});fragment.append(button);}
  $('country-list').replaceChildren(fragment);if(!entries.length)$('country-list').append(text('p','No IPs match these filters.','note'));
}
function drawTable(){
  const fragment=document.createDocumentFragment();for(const r of selected.slice(page*PAGE,(page+1)*PAGE)){const tr=document.createElement('tr'),first=document.createElement('td'),button=text('button',r.ip);button.setAttribute('aria-label','View evidence for '+r.ip);button.addEventListener('click',()=>showRecord(r));first.append(button);tr.append(first);
    for(const value of [arr(r,'publication_categories').join('; '),arr(r,'frameworks').join('; '),[flat(r.asn),flat(r.hosting)].filter(Boolean).join(' · '),[r.city,countryName(r)].filter(Boolean).join(', '),r.confidence_score==null?'Unknown':r.confidence_score+' / 100',flat(r.timestamp)||'Unknown'])tr.append(text('td',value));fragment.append(tr);}
  $('rows').replaceChildren(fragment);if(!selected.length){const tr=document.createElement('tr'),td=text('td','No addresses match these filters.','empty');td.colSpan=7;tr.append(td);$('rows').append(tr);}
  const pages=Math.max(1,Math.ceil(selected.length/PAGE));$('page-status').textContent=`Page ${page+1} of ${pages} · ${selected.length.toLocaleString()} selected unique IPs`;$('previous').disabled=page===0;$('next').disabled=page>=pages-1;
}
$('previous').addEventListener('click',()=>{if(page>0){page--;drawTable();}});$('next').addEventListener('click',()=>{if((page+1)*PAGE<selected.length){page++;drawTable();}});
function csvCell(value){let s=flat(value);if(/^[=+\-@\t\r]/.test(s))s="'"+s;return '"'+s.replaceAll('"','""')+'"';}
function selectedCSV(){const preferred=['ip','timestamp','asn','hosting','country_code','country_name','city','latitude','longitude','publication_categories','frameworks','campaigns','network_roles','india_targeting_scopes','india_campaign_c2_supported','self_derived','confidence_score','confidence_basis','record_ids','geo_status','status','source_urls'];const fields=[...new Set([...preferred,...selected.flatMap(Object.keys)])];return '\ufeff'+[fields.map(csvCell).join(','),...selected.map(r=>fields.map(k=>csvCell(r[k])).join(','))].join('\r\n')+'\r\n';}
$('download').addEventListener('click',()=>{const blob=new Blob([selectedCSV()],{type:'text/csv;charset=utf-8'}),url=URL.createObjectURL(blob),link=document.createElement('a');link.href=url;link.download='selected-ip-evidence.csv';document.body.append(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);});
let resizeTimer;new ResizeObserver(()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(drawMap,100);}).observe($('map'));
update();
// Read-only diagnostics support finite browser validation without a network service.
window.mapDiagnostics=()=>({input:DATA.length,selected:selected.length,located:selected.filter(located).length,unknown:selected.filter(r=>!located(r)).length,visibleRepresented:renderedGroups.reduce((s,r)=>s+r.length,0),markers:renderedGroups.length,page,view:{...view}});
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True, help='Repository root containing data/ip-overview.json')
    parser.add_argument('--geometry', type=Path, help='Reviewed India-view GeoJSON (default maps/assets/world-india-view.geojson)')
    parser.add_argument('--simplify-degrees', type=float, default=0, help='Optional display-only simplification; default 0 preserves reviewed asset')
    parser.add_argument('--geometry-source', default='Natural Earth public-domain data via AshKyd/geojson-regions India POV; see maps/assets geometry provenance')
    parser.add_argument('--rendered-at', help='Reproducible render UTC timestamp; defaults to current UTC')
    args = parser.parse_args()
    if not math.isfinite(args.simplify_degrees) or not 0 <= args.simplify_degrees <= 1:
        parser.error('--simplify-degrees must be between 0 and 1')
    root = args.root.resolve()
    source = root / 'data/ip-overview.json'
    geometry_path = (args.geometry or root / 'maps/assets/world-india-view.geojson').resolve()
    raw, geo_raw = source.read_bytes(), geometry_path.read_bytes()
    records = normalize_records(json.loads(raw.decode('utf-8-sig')))
    world, geometry_stats = paths_from_geometry(json.loads(geo_raw.decode('utf-8-sig')), args.simplify_degrees)
    rendered_at = args.rendered_at or dt.datetime.now(dt.timezone.utc).isoformat()
    parsed_at = dt.datetime.fromisoformat(rendered_at.replace('Z', '+00:00'))
    if parsed_at.tzinfo is None:
        parser.error('--rendered-at must include a UTC offset')
    located = sum(coordinate(row) is not None for row in records)
    metadata = dict(schema_version='1.0', renderer='scripts/render_ip_map.py', rendered_at_utc=parsed_at.astimezone(dt.timezone.utc).isoformat(),
                    input='data/ip-overview.json', input_sha256=hashlib.sha256(raw).hexdigest(),
                    geometry_source=args.geometry_source, geometry_asset='maps/assets/world-india-view.geojson',
                    geometry_sha256=hashlib.sha256(geo_raw).hexdigest(), geometry_display=geometry_stats,
                    input_unique_ips=len(records), mapped_unique_ips=located, unmapped_unique_ips=len(records)-located,
                    all_categories_default=True, external_runtime_requests_required=False, target_requests=False,
                    score_interpretation='Evidence rubric, not maliciousness probability',
                    geography_interpretation='Approximate provider hosting estimate at database snapshot; not targeting or historical attack-time attribution')
    substitutions = dict(STYLE=STYLE, WORLD=world, SCRIPT=SCRIPT, DATA=safe_json(records), META=safe_json(metadata))
    rendered = re.sub(r'__(STYLE|WORLD|SCRIPT|DATA|META)__', lambda match: substitutions[match.group(1)], BODY)
    out = root / 'maps'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(rendered, encoding='utf-8', newline='\n')
    (out / 'world.svg').write_text(static_svg(records, world, metadata), encoding='utf-8', newline='\n')
    (out / 'render-metadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2, allow_nan=False)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps(metadata, indent=2))


if __name__ == '__main__':
    main()
