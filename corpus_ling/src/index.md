---
theme: dashboard
toc: false
---

<style>

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: var(--sans-serif);
  margin: 4rem 0 8rem;
  text-wrap: balance;
  text-align: center;
}

.hero h1 {
  margin: 2rem 0;
  max-width: none;
  font-size: 14vw;
  font-weight: 900;
  line-height: 1;
  background: linear-gradient(30deg, var(--theme-foreground-focus), currentColor);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero h2 {
  margin: 0;
  max-width: 34em;
  font-size: 20px;
  font-style: initial;
  font-weight: 500;
  line-height: 1.5;
  color: var(--theme-foreground-muted);
}

@media (min-width: 640px) {
  .hero h1 {
    font-size: 90px;
  }
}

</style>

<div class="hero">
  <h1>CorpusLing</h1>
  <h2>TFG Grado en Ingeniería Informática</h2>
</div>

<!-- Carga de datos -->

```js
const freq = FileAttachment("./data/wordFrequency.tsv").tsv();
const coll = FileAttachment("./data/collocates.tsv").tsv();
```


<!-- Filtro -->

```js
const palabraInput = Inputs.text({label: "Palabra a buscar"});
const palabra = Generators.input(palabraInput);
```


<!-- Tipo de texto D3 -->

<div class="grid grid-cols-2">
  <div class="card" style="max-height: 60px; max-width: 400px;">
    ${palabraInput}
  </div>
  <div class="card" style="max-width: 520px;">
    <h1>Tipo de Texto</h1>
    ${display(tt_svg.node())}
  </div>
</div>

```js
// Dimensiones
var tt_margin = 50,
    tt_width = 500,
    tt_height = 500,
    tt_radius = Math.min(tt_width, tt_height) / 2 - tt_margin;

// Datos
var tt_filter = freq.filter((d) => d.lemma === palabra);
var tt_data = tt_filter.map(d => [
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
var tt_color = d3.scaleOrdinal()
  .domain(["Blog", "Web", "TVM", "Oral", "Ficción", "Revista", "Periódico", "Académico"])
  .range(["#eeba79", "#79ee7f", "#79adee", "#ee79e8", "#e8ee79", "#79eeba", "#7f79ee", "#ee79ae"]);

// Layout del gráfico
var tt_pie = d3.pie()
  .sort(null)
  .value(d => d.value);

var tt_arc = d3.arc()
  .innerRadius(0)
  .outerRadius(tt_radius);

var tt_labelRadius = tt_arc.outerRadius()() * 0.7;

// Arco para el texto
var tt_arcLabel = d3.arc()
  .innerRadius(tt_labelRadius)
  .outerRadius(tt_labelRadius);

// SVG
const tt_svg = d3.create('svg')
  .data(tt_data)
  .attr('width', tt_width)
  .attr('height', tt_height)
  .attr('viewBox', [-tt_width / 2, -tt_height / 2, tt_width, tt_height])
  .attr('style', 'font: 14px sans-serif;');

// Sectores
tt_svg.append('g')
    .attr('stroke', 'white')
  .selectAll()
  .data(d => tt_pie(d))
  .join('path')
    .attr('d', tt_arc)
    .attr('fill', d => tt_color(d.data.key))
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
```


<!-- Colocados D3 -->

<div class="grid grid-cols-2">
  <div class="card">
    <h1>Colocados (antes)</h1>
    ${display(c_svg.node())}
  </div>
  <div class="card">
    <h1>Colocados (después)</h1>
    ${display(c2_svg.node())}
  </div>
</div>

```js
// Dimensiones
var c_width = 870,
    c_height = 500,
    c_marginTop = 20,
    c_marginRight = 0,
    c_marginBottom = 50,
    c_marginLeft = 70;

// Datos
var c_data = coll.filter((d) => d.lemma === palabra);
c_data = c_data.filter(function(d,i){
  return i < 20;
});

// Escala X
var c_x = d3.scaleBand()
  .domain(d3.groupSort(c_data, ([d]) => -d.freq, (d) => d.coll))
  .range([c_marginLeft, c_width - c_marginRight])
  .padding(0.1);

// Escala Y
var c_y = d3.scaleLinear()
  .domain([0, d3.max(c_data, function(d) { return +d.freq; })])
  .range([c_height - c_marginBottom, c_marginTop]);

// SVG
const c_svg = d3.create('svg')
  .attr('width', c_width)
  .attr('height', c_height)
  .attr('viewbox', [0, 0, c_width, c_height]);

// Barras
c_svg.append('g')
  .attr('fill', 'steelblue')
  .selectAll()
  .data(c_data)
  .join('rect')
    .attr('x', (d) => c_x(d.coll))
    .attr('y', (d) => c_y(d.freq))
    .attr('height', (d) => (c_height - c_marginBottom) - c_y(d.freq))
    .attr('width', c_x.bandwidth());

// Eje X
c_svg.append('g')
  .attr('transform', `translate(0,${c_height - c_marginBottom})`)
  .call(d3.axisBottom(c_x).tickSizeOuter(0))
  .selectAll('text')
    .attr('transform', 'translate(-10,0)rotate(-45)')
    .style('text-anchor', 'end');

// Eje Y
c_svg.append('g')
  .attr('transform', `translate(${c_marginLeft},0)`)
  .call(d3.axisLeft(c_y))
  .call(g => g.select('.domain').remove())
  .call(g => g.append('text')
    .attr('x', -c_marginLeft)
    .attr('y', 10)
    .attr('fill', 'currentColor')
    .attr('text-anchor', 'start')
    .text('↑ Frecuencia'));
```

```js
// Dimensiones
var c_width = 870,
    c_height = 500,
    c_marginTop = 20,
    c_marginRight = 0,
    c_marginBottom = 50,
    c_marginLeft = 70;

// Datos
var c_data = coll.filter((d) => d.coll === palabra);
c_data = c_data.filter(function(d,i){
  return i < 20;
});

// Escala X
var c_x = d3.scaleBand()
  .domain(d3.groupSort(c_data, ([d]) => -d.freq, (d) => d.lemma))
  .range([c_marginLeft, c_width - c_marginRight])
  .padding(0.1);

// Escala Y
var c_y = d3.scaleLinear()
  .domain([0, d3.max(c_data, function(d) { return +d.freq; })])
  .range([c_height - c_marginBottom, c_marginTop]);

// SVG
const c2_svg = d3.create('svg')
  .attr('width', c_width)
  .attr('height', c_height)
  .attr('viewbox', [0, 0, c_width, c_height]);

// Barras
c2_svg.append('g')
  .attr('fill', 'steelblue')
  .selectAll()
  .data(c_data)
  .join('rect')
    .attr('x', (d) => c_x(d.lemma))
    .attr('y', (d) => c_y(d.freq))
    .attr('height', (d) => (c_height - c_marginBottom) - c_y(d.freq))
    .attr('width', c_x.bandwidth());

// Eje X
c2_svg.append('g')
  .attr('transform', `translate(0,${c_height - c_marginBottom})`)
  .call(d3.axisBottom(c_x).tickSizeOuter(0))
  .selectAll('text')
    .attr('transform', 'translate(-10,0)rotate(-45)')
    .style('text-anchor', 'end');

// Eje Y
c2_svg.append('g')
  .attr('transform', `translate(${c_marginLeft},0)`)
  .call(d3.axisLeft(c_y))
  .call(g => g.select('.domain').remove())
  .call(g => g.append('text')
    .attr('x', -c_marginLeft)
    .attr('y', 10)
    .attr('fill', 'currentColor')
    .attr('text-anchor', 'start')
    .text('↑ Frecuencia'));
```