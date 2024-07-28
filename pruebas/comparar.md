---
theme: dashboard
title: Comparar tipos
toc: false
---

<!-- Carga de datos -->

```js
const freq = FileAttachment("./data/wordFrequency.tsv").tsv();
```


<!-- Filtro -->

```js
const palabraInput = Inputs.text({label: "Palabra a buscar"});
const palabra = Generators.input(palabraInput);
```

<div class="card">
  ${palabraInput}
</div>


<!-- Tipo de texto D3 -->

<div class="card">
  <h1>Tipo de Texto</h1>
  <div class="tipo-texto"></div>
</div>

```js
// Dimensiones
const tt_margin = 50;
const tt_width = 450;
const tt_height = 450;
const tt_radius = Math.min(tt_width, tt_height) / 2 - tt_margin;

// Datos
const tt_filter = freq.filter((d) => d.lemma === palabra);
const tt_data = tt_filter.map(d => [
  { key: 'Blog', value: d.blog, percent: d3.format(",.1~f")((d.blog / d.freq) * 100) },
  { key: 'Web', value: d.web, percent: d3.format(",.1~f")((d.web / d.freq) * 100) },
  { key: 'TVM', value: d.TVM, percent: d3.format(",.1~f")((d.TVM / d.freq) * 100) },
  { key: 'Oral', value: d.spok, percent: d3.format(",.1~f")((d.spok / d.freq) * 100) },
  { key: 'Ficción', value: d.fic, percent: d3.format(",.1~f")((d.fic / d.freq) * 100) },
  { key: 'Revista', value: d.mag, percent: d3.format(",.1~f")((d.mag / d.freq) * 100) },
  { key: 'Periódico', value: d.news, percent: d3.format(",.1~f")((d.news / d.freq) * 100) },
  { key: 'Académico', value: d.acad, percent: d3.format(",.1~f")((d.acad / d.freq) * 100) },
]);

// Paleta de colores
const tt_color = d3.scaleOrdinal()
  .domain(["Blog", "Web", "TVM", "Oral", "Ficción", "Revista", "Periódico", "Académico"])
  .range(["#eeba79", "#79ee7f", "#79adee", "#ee79e8", "#e8ee79", "#79eeba", "#7f79ee", "#ee79ae"]);

// Layout del gráfico
const tt_pie = d3.pie()
  .sort(null)
  .value(d => d.value);

const tt_arc = d3.arc()
  .innerRadius(0)
  .outerRadius(tt_radius);

const tt_labelRadius = tt_arc.outerRadius()() * 0.7;

// Arco para el texto
const tt_arcLabel = d3.arc()
  .innerRadius(tt_labelRadius)
  .outerRadius(tt_labelRadius);

// SVG
const tt_svg = d3.selectAll('.tipo-texto')
  .data(tt_data)
  .append('svg')
    .attr('width', tt_width)
    .attr('height', tt_height)
  .append('g')
    .attr('transform', `translate(${tt_width /2},${tt_height / 2})`);

// Path
tt_svg.selectAll('path')
  .data(d => tt_pie(d))
  .join('path')
    .attr('d', tt_arc)
    .attr('fill', d => tt_color(d.data.key))
    .attr('stroke', 'white')
    .attr('stroke-width', '2px')
    .attr('opacity', 0.7)
  .append('title')
    .text(d => `${d.data.key}: ${d.data.value.toLocaleString("es")}`);

// Texto
tt_svg.append('g')
  .attr('text-anchor', 'middle')
  .selectAll()
  .data(d => tt_pie(d))
  .join('text')
    .attr('transform', d => `translate(${tt_arcLabel.centroid(d)})`)
    .call(text => text.filter(d => (d.endAngle - d.startAngle) > 0.25).append("tspan")
      .attr('y', '-0.4em')
      .attr('font-weight', 'bold')
      .text(d => d.data.key))
    .call(text => text.filter(d => (d.endAngle - d.startAngle) > 0.25).append("tspan")
      .attr('x', 0)
      .attr('y', '0.7em')
      .attr('fill-opacity', 0.7)
      .text(d => d.data.percent.toLocaleString("es") + "%"));

// Título
tt_svg.append('text')
  .attr('x', 0)
  .attr('y', -((tt_height / 2) - (tt_margin / 2)))
  .attr('text-anchor', 'middle')
  .style('font-size', '25px')
  .attr('font-weight', 'bold')
  .style('fill', 'white')
  .text(palabra);
```