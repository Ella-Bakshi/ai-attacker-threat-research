// Representative points on the atlas's Natural Earth India-view geometry.
// The first two anchors are near Crime Tracker's Lakshadweep and Andaman hit areas.
const islandPlaces = [
  ['lakshadweep', 'Lakshadweep, India', 72.642076, 10.566677],
  ['andaman', 'Andaman and Nicobar Islands, India', 92.854261, 12.559333],
  ['mv', 'Maldives', 73.491231, 4.173368],
  ['sc', 'Seychelles', 46.341195, -9.405979],
  ['mu', 'Mauritius', 57.559806, -20.333510],
  ['cv', 'Cape Verde', -23.685321, 15.167670],
  ['mt', 'Malta', 14.415035, 35.931586],
  ['lc', 'Saint Lucia', -60.961136, 13.995836],
  ['kn', 'Saint Kitts and Nevis', -62.706298, 17.287869],
  ['dm', 'Dominica', -61.362126, 15.337205],
  ['to', 'Tonga', -175.168437, -21.220269],
  ['tv', 'Tuvalu', 179.204986, -8.489801],
  ['nr', 'Nauru', 166.934701, -0.538344],
  ['pw', 'Palau', 134.600379, 7.487331],
  ['mh', 'Marshall Islands', 171.191054, 7.122667],
  ['fm', 'Federated States of Micronesia', 158.229079, 6.873318],
  ['ws', 'Samoa', -172.415028, -13.698948],
];

const islandTip = $('atlas-island-tooltip');
const islandPicker = $('island-jump');
const coarsePointer = matchMedia('(pointer: coarse)');
if (coarsePointer.matches) $('map-gesture').textContent = 'Drag to pan · Pinch to zoom';
const islandLandPaths = [...$('land').children].map(path => ({path, bounds: path.getBBox()}));
let islandSelection = null;
let islandHovered = null;

const islandNodes = islandPlaces.map(([id, name, longitude, latitude]) => {
  const anchor = point({longitude, latitude});
  option(islandPicker, id, name);
  const layer = svg('g', {'data-island': id});
  const guide = svg('line', {class: 'island-guide', x1: anchor.x, y1: anchor.y});
  const ring = svg('circle', {class: 'island-ring'});
  const hit = svg('circle', {class: 'island-hit'});
  layer.append(guide, ring, hit);
  $('atlas-island-hits').append(layer);
  const island = {id, name, anchor, layer, guide, ring, hit};

  function showTip(event) {
    if (event.pointerType === 'touch' || pointers.size) return;
    islandHovered = layer;
    layer.classList.add('island-hover');
    $('hover').style.display = 'none';
    islandTip.replaceChildren(text('strong', name), text('span', 'Select to zoom'));
    islandTip.hidden = false;
    const stage = $('stage').getBoundingClientRect();
    const left = Math.max(8, Math.min(stage.width - islandTip.offsetWidth - 8, event.clientX - stage.left + 13));
    const top = Math.max(8, Math.min(stage.height - islandTip.offsetHeight - 8, event.clientY - stage.top + 15));
    islandTip.style.left = `${left}px`;
    islandTip.style.top = `${top}px`;
  }

  hit.addEventListener('pointerenter', showTip);
  hit.addEventListener('pointermove', showTip);
  hit.addEventListener('pointerleave', hideIslandTip);
  hit.addEventListener('click', () => {
    if (performance.now() - lastDragAt >= 220) zoomToIsland(island);
  });
  return island;
});

function hideIslandTip() {
  islandHovered?.classList.remove('island-hover');
  islandHovered = null;
  islandTip.hidden = true;
}

function zoomToIsland(island) {
  hideIslandTip();
  islandSelection = island;
  islandPicker.value = island.id;
  $('island-selection').textContent = island.name;
  const ratio = aspect();
  const w = Math.min(camera.w, M.baseWidth(ratio) / 10);
  const h = w / ratio;
  setCamera({x: island.anchor.x - w / 2, y: island.anchor.y - h / 2, w, h});
  syncURL();
}

function clearIslandSelection() {
  hideIslandTip();
  islandSelection = null;
  islandPicker.value = '';
  $('island-selection').textContent = '';
}

islandPicker.addEventListener('change', () => {
  const island = islandNodes.find(entry => entry.id === islandPicker.value);
  if (island) zoomToIsland(island);
  else clearIslandSelection();
});
$('map').addEventListener('pointerleave', hideIslandTip);

const islandOffsets = [[0, 0], [-24, 17], [24, 17], [-31, -17], [33, -19], [0, 32], [0, -33],
  [-45, 13], [43, 14], [-24, 49], [0, 56], [34, 50], [-48, 52], [20, 68]];
const preferredIslandOffsets = {
  lakshadweep: [[-25, 10], [-26, 46], [-3, 51]],
  andaman: [[-13, 24], [18, 25], [26, 50]],
};

function atSea({x, y}) {
  return !islandLandPaths.some(({path, bounds}) =>
    x >= bounds.x && x <= bounds.x + bounds.width && y >= bounds.y && y <= bounds.y + bounds.height &&
    path.isPointInFill(new DOMPoint(x, y)));
}

function drawIslandTargets(units, groups) {
  const radius = (coarsePointer.matches ? 22 : 19) * units;
  const zoomLevel = M.baseWidth(aspect()) / camera.w;
  // Evidence clusters keep their click areas. Island guides can move seaward to avoid collisions.
  const taken = groups.map(group => ({x: group.xsum / group.rows.length, y: group.ysum / group.rows.length}));
  const worldCap = rect().width < 500 ? 3 : 5;
  let shown = 0;

  for (const island of islandNodes) {
    const {id, anchor, layer, guide, ring, hit} = island;
    const isSelected = island === islandSelection;
    const show = M.inView(anchor, camera) && (isSelected || zoomLevel >= 2.3 || shown < worldCap);
    const offsets = [...(preferredIslandOffsets[id] || []), ...islandOffsets];
    const target = show && offsets.map(([dx, dy]) => ({x: anchor.x + dx * units, y: anchor.y + dy * units}))
      .find(({x, y}) => x - radius >= camera.x && x + radius <= camera.x + camera.w &&
        y - radius >= camera.y && y + radius <= camera.y + camera.h &&
        taken.every(other => Math.hypot(x - other.x, y - other.y) > 2 * radius) && atSea({x, y}));
    if (!target) {
      layer.setAttribute('display', 'none');
      if (islandHovered === layer) hideIslandTip();
      continue;
    }
    layer.removeAttribute('display');
    layer.classList.toggle('island-hover', isSelected || islandHovered === layer);
    guide.setAttribute('x2', target.x);
    guide.setAttribute('y2', target.y);
    for (const circle of [ring, hit]) {
      circle.setAttribute('cx', target.x);
      circle.setAttribute('cy', target.y);
    }
    ring.setAttribute('r', 5 * units);
    hit.setAttribute('r', radius);
    taken.push(target);
    shown++;
  }

  if (!islandSelection) return;
  if (!M.inView(islandSelection.anchor, camera)) {
    clearIslandSelection();
    return;
  }
  const emptyView = selected.length && !visibleRepresented;
  if (emptyView) $('map-empty').classList.remove('show');
  $('island-selection').textContent = emptyView
    ? `${islandSelection.name} · no selected addresses in view`
    : islandSelection.name;
}
