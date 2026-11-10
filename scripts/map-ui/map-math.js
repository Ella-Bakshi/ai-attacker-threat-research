(function(root){
  'use strict';
  const W=1200,H=600,MAX_ZOOM=48;
  const baseWidth=aspect=>Math.max(W,H*aspect);
  function clampCamera(camera,aspect){
    const base=baseWidth(aspect),w=Math.max(base/MAX_ZOOM,Math.min(base*1.2,camera.w)),h=w/aspect;
    return {w,h,x:w>=W?(W-w)/2:Math.max(0,Math.min(W-w,camera.x)),y:h>=H?(H-h)/2:Math.max(0,Math.min(H-h,camera.y))};
  }
  function worldCamera(aspect){const w=baseWidth(aspect);return {x:(W-w)/2,y:(H-w/aspect)/2,w,h:w/aspect};}
  function bounds(points){if(!points.length)return null;return {minX:Math.min(...points.map(p=>p.x)),maxX:Math.max(...points.map(p=>p.x)),minY:Math.min(...points.map(p=>p.y)),maxY:Math.max(...points.map(p=>p.y))};}
  function fitCamera(points,aspect){const b=bounds(points);if(!b)return worldCamera(aspect);const w=Math.max(30,(b.maxX-b.minX)*1.3,(b.maxY-b.minY)*aspect*1.3),h=w/aspect;return clampCamera({x:(b.minX+b.maxX-w)/2,y:(b.minY+b.maxY-h)/2,w,h},aspect);}
  function zoomCamera(camera,factor,anchor,fx,fy,aspect){const w=Math.max(baseWidth(aspect)/MAX_ZOOM,Math.min(baseWidth(aspect)*1.2,camera.w*factor));return clampCamera({x:anchor.x-fx*w,y:anchor.y-fy*w/aspect,w,h:w/aspect},aspect);}
  function panCamera(camera,dx,dy,width,height,aspect){return clampCamera({x:camera.x-dx/width*camera.w,y:camera.y-dy/height*camera.h,w:camera.w,h:camera.h},aspect);}
  function inView(point,camera){return point.x>=camera.x&&point.x<=camera.x+camera.w&&point.y>=camera.y&&point.y<=camera.y+camera.h;}
  const api=Object.freeze({W,H,MAX_ZOOM,baseWidth,clampCamera,worldCamera,bounds,fitCamera,zoomCamera,panCamera,inView});
  root.AtlasMath=api;if(typeof module!=='undefined'&&module.exports)module.exports=api;
})(typeof globalThis!=='undefined'?globalThis:this);
