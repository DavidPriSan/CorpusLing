---
theme: dashboard
title: N-gramas
toc: false
---

<!-- Carga de datos -->

```js
const ngrams = FileAttachment("./data/ngrams.json").json();
```

<!-- Tipo de texto D3 -->

<div class="card">
  <h1>Conjuntos más usados de 5 palabras que empiezan por 'M'</h1>
  ${display(ng_svg.node())}
</div>

```js
// Dimensiones
const ng_width = 950,
      ng_height = ng_width,
      ng_radius = ng_width / 6;

// Paleta de colores
const ng_color = d3.scaleOrdinal(d3.quantize(d3.interpolateRainbow, ngrams.children.length + 1));

// Layout
const ng_hierarchy = d3.hierarchy(ngrams)
    .sum(d => d.value)
    .sort((a, b) => b.value - a.value);
const ng_root = d3.partition()
    .size([2 * Math.PI, ng_hierarchy.height + 1])
  (ng_hierarchy);
ng_root.each(d => d.current = d);

// Generador de arcos
const ng_arc = d3.arc()
  .startAngle(d => d.x0)
  .endAngle(d => d.x1)
  .padAngle(d => Math.min((d.x1 - d.x0) / 2, 0.005))
  .padRadius(ng_radius * 1.5)
  .innerRadius(d => d.y0 * ng_radius)
  .outerRadius(d => Math.max(d.y0 * ng_radius, d.y1 * ng_radius - 1))

// SVG
const ng_svg = d3.create('svg')
  .attr('viewBox', [-ng_width / 2, -ng_height / 2, ng_width, ng_width])
  .style('font', '10px sans-serif');

// Arcos
const ng_path = ng_svg.append('g')
  .selectAll('path')
  .data(ng_root.descendants().slice(1))
  .join('path')
    .attr('fill', d => { while (d.depth > 1) d = d.parent; return ng_color(d.data.name); })
    .attr('fill-opacity', d => arcVisible(d.current) ? (d.children ? 0.6 : 0.4) : 0)
    .attr('pointer-events', d => arcVisible(d.current) ? "auto" : "none")

    .attr('d', d => ng_arc(d.current));

// Clickables si tienen hijos
ng_path.filter(d => d.children)
    .style('cursor', 'pointer')
    .on('click', clicked);

const ng_format = d3.format(",d");
ng_path.append('title')
    .text(d => `${d.ancestors().map(d => d.data.name).reverse().join("/")}\n${ng_format(d.value)}`);

const ng_label = ng_svg.append('g')
    .attr('pointer-events', 'none')
    .attr('text-anchor', 'middle')
    .style('user-select', 'none')
  .selectAll('text')
  .data(ng_root.descendants().slice(1))
  .join('text')
    .attr('dy', '0.35em')
    .attr('fill-opacity', d => +labelVisible(d.current))
    .attr('transform', d => labelTransform(d.current))
    .text(d => d.data.name);

const ng_parent = ng_svg.append('circle')
    .datum(ng_root)
    .attr('r', ng_radius)
    .attr('fill', 'none')
    .attr('pointer-events', 'all')
    .on('click', clicked);

// Zoom al clickar
function clicked(event, p) {
  ng_parent.datum(p.parent || ng_root);

  ng_root.each(d => d.target = {
    x0: Math.max(0, Math.min(1, (d.x0 - p.x0) / (p.x1 - p.x0))) * 2 * Math.PI,
    x1: Math.max(0, Math.min(1, (d.x1 - p.x0) / (p.x1 - p.x0))) * 2 * Math.PI,
    y0: Math.max(0, d.y0 - p.depth),
    y1: Math.max(0, d.y1 - p.depth)
  });

  const t = ng_svg.transition().duration(750);

  ng_path.transition(t)
      .tween("data", d => {
        const i = d3.interpolate(d.current, d.target);
        return t => d.current = i(t);
      })
    .filter(function(d) {
      return +this.getAttribute("fill-opacity") || arcVisible(d.target);
    })
      .attr("fill-opacity", d => arcVisible(d.target) ? (d.children ? 0.6 : 0.4) : 0)
      .attr("pointer-events", d => arcVisible(d.target) ? "auto" : "none") 

      .attrTween("d", d => () => ng_arc(d.current));

  ng_label.filter(function(d) {
      return +this.getAttribute("fill-opacity") || labelVisible(d.target);
    }).transition(t)
      .attr("fill-opacity", d => +labelVisible(d.target))
      .attrTween("transform", d => () => labelTransform(d.current));
}
  
function arcVisible(d) {
  return d.y1 <= 3 && d.y0 >= 1 && d.x1 > d.x0;
}

function labelVisible(d) {
  return d.y1 <= 3 && d.y0 >= 1 && (d.y1 - d.y0) * (d.x1 - d.x0) > 0.03;
}

function labelTransform(d) {
  const x = (d.x0 + d.x1) / 2 * 180 / Math.PI;
  const y = (d.y0 + d.y1) / 2 * ng_radius;
  return `rotate(${x - 90}) translate(${y},0) rotate(${x < 180 ? 0 : 180})`;
}
```