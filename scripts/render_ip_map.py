#!/usr/bin/env python3
"""Render an offline IP evidence map and static SVG; no network access or dependencies.

Input: data/ip-overview.json (a flat list of canonical-IP records).
Geometry: a reviewed India-view GeoJSON supplied locally. This script never downloads
or substitutes a default boundary dataset. All displayed text remains untrusted data.
"""
import argparse
import base64
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
            properties = feature.get('properties') or {}
            code = properties.get('iso_a2_eh') or properties.get('iso_a2') or ''
            if not isinstance(code, str) or len(code) != 2: code = ''
            name = properties.get('name_en') or properties.get('name') or ''
            output.append('<path data-country="'+html.escape(code,quote=True)+'" data-name="'+html.escape(str(name),quote=True)+'" d="' + ' '.join(pieces) + '"/>')
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


def static_svg(records, world, metadata, font_data=''):
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
    counts=collections.Counter(row.get('country_code') for row in records if row.get('country_code'))
    maximum=max(counts.values(),default=1)
    def shade(match):
        count=counts.get(match.group(1),0)
        if not count:fill='#e2e8f0'
        else:
            ratio=min(count/maximum,1)
            start,end,t=((226,232,240),(236,201,75),ratio*2) if ratio<=.5 else ((236,201,75),(220,60,40),(ratio-.5)*2)
            fill='rgb('+','.join(str(round(a+(b-a)*t)) for a,b in zip(start,end))+')'
        return match.group(0)+' fill="'+fill+'"'
    world=re.sub(r'<path data-country="([^"]*)"',shade,world)
    # Keep the source site's blue point family in the static all-category preview.
    markers=[marker.replace('#168b94','#2b6cb0').replace('#d9fbf4','#ffffff') for marker in markers]
    title=f'{len(records):,} unique IPs · {mapped:,} located · {len(records)-mapped:,} without coordinates'
    caption='Approximate hosting locations; not victim locations. All evidence categories included. Open the HTML map to filter.'
    source='IP Geolocation by DB-IP · CC BY 4.0. Natural Earth India-view boundaries; see repository provenance.'
    font_style=f"@font-face{{font-family:Inter;src:url(data:font/woff2;base64,{font_data}) format('woff2');font-weight:100 900}}" if font_data else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" role="img" aria-labelledby="title desc">
<title id="title">AI Attacker Threat Research — infrastructure overview</title><desc id="desc">{html.escape(title+'. '+caption)}</desc>
<metadata>{html.escape(json.dumps(metadata,ensure_ascii=False,allow_nan=False))}</metadata><style>{font_style}text{{font-family:Inter,system-ui,sans-serif}}</style>
<rect width="1200" height="850" fill="#f1f5f9"/><rect width="1200" height="50" fill="#fff"/><path d="M0 50H1200" stroke="#e2e8f0"/>
<text x="27" y="31" font-size="16" font-weight="700" fill="#1a365d">AI Attacker Threat Research</text>
<text x="1173" y="31" text-anchor="end" font-size="11" fill="#94a3b8">Snapshot {metadata['rendered_at_utc'][:10]} UTC</text>
<text x="600" y="117" text-anchor="middle" font-size="61" font-weight="900" letter-spacing="-3" fill="#dc2626">{len(records):,}</text>
<text x="600" y="145" text-anchor="middle" font-size="13" fill="#64748b">{html.escape(title)}</text>
<rect x="23" y="174" width="1154" height="625" rx="14" fill="#fff" stroke="#e2e8f0"/>
<svg x="39" y="190" width="1122" height="561" viewBox="0 0 1200 600"><rect width="1200" height="600" rx="10" fill="#eef2f6"/><g stroke="#1a1a1a" stroke-width=".45" fill-rule="evenodd">{world}</g>{''.join(markers)}</svg>
<text x="45" y="779" font-size="11" fill="#64748b">{html.escape(caption)}</text><a href="https://db-ip.com"><text x="26" y="830" font-size="11" fill="#64748b">{html.escape(source)}</text></a></svg>'''


UI_DIR = Path(__file__).resolve().with_name('map-ui')
STYLE = (UI_DIR / 'atlas.css').read_text(encoding='utf8')
BODY = (UI_DIR / 'atlas.html').read_text(encoding='utf8')
SCRIPT = (UI_DIR / 'map-math.js').read_text(encoding='utf8') + '\n' + (UI_DIR / 'atlas.js').read_text(encoding='utf8')


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
    font_bytes = (root / 'maps/assets/inter-latin-variable.woff2').read_bytes()
    font_data = base64.b64encode(font_bytes).decode('ascii')
    metadata['ui_reference'] = 'https://github.com/Ella-Bakshi/cctv-scanner-result/tree/b234b7533d7d10933c43727e4f858500c88d587b'
    metadata['embedded_font_sha256'] = hashlib.sha256(font_bytes).hexdigest()
    substitutions = dict(STYLE=STYLE.replace('__FONT_DATA__',font_data), WORLD=world, SCRIPT=SCRIPT, DATA=safe_json(records), META=safe_json(metadata))
    rendered = re.sub(r'__(STYLE|WORLD|SCRIPT|DATA|META)__', lambda match: substitutions[match.group(1)], BODY)
    out = root / 'maps'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(rendered, encoding='utf-8', newline='\n')
    (out / 'world.svg').write_text(static_svg(records, world, metadata, font_data), encoding='utf-8', newline='\n')
    (out / 'render-metadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2, allow_nan=False)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps(metadata, indent=2))


if __name__ == '__main__':
    main()
