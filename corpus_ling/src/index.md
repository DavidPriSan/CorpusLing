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

## Pruebas

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

<div class="card">
  ${palabraInput}
</div>


<!-- Frecuencia por tipo de texto -->

<div class="card"><h1>Tipo de texto</h1>
  ${resize((width) => Plot.plot({
    width,
    marginLeft: 50,
    marginBottom: 40,
    y: {grid: true, label: "Apariciones"},
    x: {label: "Tipo de texto", ticks: 8},
    marks: [
      Plot.barY(freq.filter((d) => d.lemma === palabra),
        {
            y: "acad",
            insetLeft: width*(1/17),
            insetRight: width*(15/17),
            fill: "steelblue"
        }
      ),
      Plot.barY(freq.filter((d) => d.lemma === palabra),
        {
            y: "blog",
            insetLeft: width*(3/17),
            insetRight: width*(13/17),
            fill: "steelblue"
        }
      ),
      Plot.barY(freq.filter((d) => d.lemma === palabra),
        {
            y: "fic",
            insetLeft: width*(5/17),
            insetRight: width*(11/17),
            fill: "steelblue"
        }
      ),
      Plot.barY(freq.filter((d) => d.lemma === palabra),
        {
            y: "spok",
            insetLeft: width*(7/17),
            insetRight: width*(9/17),
            fill: "steelblue"
        }
      ),
      Plot.barY(freq.filter((d) => d.lemma === palabra),
        {
            y: "news",
            insetLeft: width*(9/17),
            insetRight: width*(7/17),
            fill: "steelblue"
        }
      ),
      Plot.barY(freq.filter((d) => d.lemma === palabra),
        {
            y: "mag",
            insetLeft: width*(11/17),
            insetRight: width*(5/17),
            fill: "steelblue"
        }
      ),
      Plot.barY(freq.filter((d) => d.lemma === palabra),
        {
            y: "TVM",
            insetLeft: width*(13/17),
            insetRight: width*(3/17),
            fill: "steelblue"
        }
      ),
      Plot.barY(freq.filter((d) => d.lemma === palabra),
        {
            y: "web",
            insetLeft: width*(15/17),
            insetRight: width*(1/17),
            fill: "steelblue"
        }
      ),
      Plot.text([["Blog"], ["Web"], ["TVM"], ["Oral"], ["Ficción"], ["Revista"], ["Periódico"], ["Académico"]]),
      Plot.ruleY([0])
    ]
  }))}
</div>


<!-- Collocates -->

<div class="grid grid-cols-2">
  <div class="card"><h1>Colocados(antes)</h1>
    ${resize((width) => Plot.plot({
      width,
      marginBottom: 80,
      y: {grid: true, label: "Apariciones"},
      x: {label: null, tickRotate: -35},
      marks: [
        Plot.barY(coll.filter((d) => d.lemma === palabra),
          {
            y: "freq",
            x: "coll",
            sort: { x: "y", reverse: true, limit: 15 },
            fill: "steelblue"
          }
        ),
        Plot.ruleY([0])
      ]
    }))}
  </div>

  <div class="card"><h1>Colocados(después)</h1>
    ${resize((width) => Plot.plot({
      width,
      marginBottom: 80,
      y: {grid: true, label: "Apariciones"},
      x: {label: null, tickRotate: -35},
      marks: [
        Plot.barY(coll.filter((d) => d.coll === palabra),
          {
            y: "freq",
            x: "lemma",
            sort: { x: "y", reverse: true, limit: 15 },
            fill: "steelblue"
          }
        ),
        Plot.ruleY([0])
      ]
    }))}
  </div>
</div>


<!-- Tipo de texto D3 -->
<div class="card">
  <h1>Tipo de Texto</h1>
  <div class="tipo-texto"></div>
</div>

```js
// Dimensiones
const tt_margin = 50;
const tt_width = 500;
const tt_height = 500;
const tt_radius = Math.min(tt_width, tt_height) / 2 - tt_margin;

// Datos
const tt_filter = freq.filter((d) => d.lemma === palabra);
const tt_data = tt_filter.map(d => [
  { key: 'Blog', value: d.blog },
  { key: 'Web', value: d.web },
  { key: 'TVM', value: d.TVM },
  { key: 'Oral', value: d.spok },
  { key: 'Ficción', value: d.fic },
  { key: 'Revista', value: d.mag },
  { key: 'Periódico', value: d.news },
  { key: 'Académico', value: d.acad },
]);

// Paleta de colores
const tt_color = d3.scaleOrdinal()
  .domain(["Blog", "Web", "TVM", "Oral", "Ficción", "Revista", "Periódico", "Académico"])
  .range(["#eeba79", "#79ee7f", "#79adee", "#ee79e8", "#e8ee79", "#79eeba", "#7f79ee", "#ee79ae"]);

// Layout del gráfico
const tt_pie = d3.pie().value(d => d.value);

const tt_arc = d3.arc()
  .innerRadius(0)
  .outerRadius(tt_radius);

const tt_labelRadius = tt_arc.outerRadius()() * 0.8;

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
    .attr('stroke', 'black')
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
    .call(text => text.append("tspan")
      .attr('y', '-0.4em')
      .attr('font-weight', 'bold')
      .text(d => d.data.key))
    .call(text => text.filter(d => (d.endAngle - d.startAngle) > 0.25).append("tspan")
      .attr('x', 0)
      .attr('y', '0.7em')
      .attr('fill-opacity', 0.7)
      .text(d => d.data.value.toLocaleString("es")));

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