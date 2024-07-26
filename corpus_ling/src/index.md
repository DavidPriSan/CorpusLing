---
theme: [glacier, alt, wide]
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

.scrollable-div {
  height: 350px;
  overflow-y: scroll;
}

</style>

<div class="hero">
  <h1>CorpusLing</h1>
  <h2>TFG Grado en Ingeniería Informática</h2>
</div>

<!-- Botones pasos -->

```js
const pasosInput = Inputs.button(
  [
    ["1: Carga de datos", (value) => 1],
    ["2: Verificación", (value) => 2],
    ["3: Visualización", (value) => 3]
  ],
  { value: 0 }
);
const pasos = Generators.input(pasosInput);
```

<div class="card">
  ${pasosInput}
</div>

<!-- Procesamiento pasos -->

```js
const paso1Div = document.getElementById("paso1");
const paso2Div = document.getElementById("paso2");
const paso3Div = document.getElementById("paso3");

if (pasos == 0) { // Sin seleccionar paso
  paso1Div.hidden = true;
  paso2Div.hidden = true;
  paso3Div.hidden = true;
} else if (pasos == 1) { // Paso 1 (Carga de datos)
  paso1Div.hidden = false;
  paso2Div.hidden = true;
  paso3Div.hidden = true;
} else if (pasos == 2) { // Paso 2 (Verificación)
  paso1Div.hidden = true;
  paso2Div.hidden = false;
  paso3Div.hidden = true;
} else if (pasos == 3) { // Paso 3 (Visualización)
  paso1Div.hidden = true;
  paso2Div.hidden = true;
  paso3Div.hidden = false;
}
```

<!-- Botones carga de datos -->

```js
// Imagenes
const TSVpng = FileAttachment("TSV.png").image({ width: 64 });
```

```js
// Botonera
const cargaInput = Inputs.button([[TSVpng, (value) => 1]], { value: 0 });
const carga = Generators.input(cargaInput);
```

<!-- Modo de carga -->

```js
// Input TSV
const archivoTSVInput = Inputs.file({
  label: "Archivo TSV",
  accept: ".tsv",
  required: true,
  width: 310,
});
const archivoTSV = Generators.input(archivoTSVInput);
```

<div id="paso1">
<div class="grid grid-cols-2">
  <div class="card"> <!-- Elegir modo -->
    <h1>Elige el modo de carga de datos</h1>
    <br>
    ${cargaInput}
    <br>
    <div id="carga"></div>
    <div id="TSV">
      ${archivoTSVInput}
    </div>
  </div>
  <div class="card" style="max-height: 350px;"> <!-- Visualización de datos -->
    <div id="muestraTSV" class="scrollable-div"></div>
  </div>
</div>
</div>

```js
const cargaDiv = document.getElementById("carga");
const TSVDiv = document.getElementById("TSV");
const muestraTSVDiv = document.getElementById("muestraTSV");

if (carga == 0) { // Sin seleccionar modo
  cargaDiv.innerHTML = "<p>Puedes elegir como quieres cargar tus datos pulsando los distintos botones de arriba.</p>";
  TSVDiv.hidden = true;
  muestraTSVDiv.hidden = true;
} else if (carga == 1) { // Examinar TSV
  cargaDiv.innerHTML = "<p>Examina el archivo TSV de tu equipo haciendo click en el botón de abajo (siendo la primera línea del mismo los encabezados de las columnas).</p><br>";
  TSVDiv.hidden = false;
  muestraTSVDiv.hidden = false;
}
```

```js
// Parseo TSV
const TSV = archivoTSV.tsv();
```

```js
muestraTSV.innerHTML = JSON.stringify(TSV);
const keys = Object.keys(TSV[0]);
```

<!-- Verificación -->

<div id="paso2">
<div class="grid grid-cols-3">
  <div class="card"> <!-- Texto -->
    <h1>Comprueba que tus datos se procesaron correctamente</h1>
    <br>
    
  </div>
  <div class="card grid-colspan-2" style="max-height: 350px;"> <!-- Tabla -->
    ${selectorVfInput}
    <div id="tablaVf" class="scrollable-div"></div>
  </div>
</div>
</div>

```js
// Tabla verificación TSV
/*

  HACER LO DE NUMEROS EN UN COLOR Y TEXTO EN OTRO?

*/
const container = document.getElementById("tablaVf");

let table = document.createElement("table");
let thead = document.createElement("thead");
let tr = document.createElement("tr");

// Encabezados
keys.forEach((item) => {
  let th = document.createElement("th");
  th.innerText = item;
  tr.appendChild(th);
});
thead.appendChild(tr);
table.append(tr);

// Datos
TSV.forEach((item) => {
  let tr = document.createElement("tr");
  let vals = Object.values(item);

  vals.forEach((elem) => {
    let td = document.createElement("td");
    td.innerText = elem;
    tr.appendChild(td);
  });
  table.appendChild(tr);
});
container.appendChild(table);
```

<!-- Botones verificación -->

```js
// Selector
/*

  NO FUNCA

*/
const selectorVfInput = Inputs.select(keys, {label: "Ordenar por"});
const selectorVf = Generators.input(selectorVfInput);
```

<!-- Visualización -->

<div id="paso3">
<div class="grid grid-cols-3">
  <div class="card"> <!-- Texto -->
    <h1>Elige el tipo de gráfico</h1>
    <br>
    ${graphInput}
  </div>
  <div class="card grid-colspan-2" style="max-height: 700px;"> <!-- Gráfico -->
    <div id="graphBarras" style="overflow-y: scroll">
      ${selectorVsInput}
      ${limitVsInput}
      ${display(c_svg.node())}
    </div>
    <div id="graphSector">
      ${selectorVsInput}
      ${limitVsInput}
      ${display(tt_svg.node())}
    </div>
  </div>
</div>
</div>

<!-- Botones visualización -->

```js
// Imagenes

```

```js
// Botonera gráficos
const graphInput = Inputs.button(
  [
    ["Gráfico de barras", (value) => 1],
    ["Diagrama de sectores", (value) => 2]
  ],
  { value: 0 }
);
const graph = Generators.input(graphInput);
```

<!-- Elección gráfico -->

```js
const graphBarrasDiv = document.getElementById("graphBarras");
const graphSectorDiv = document.getElementById("graphSector");

if (graph == 0) { // Sin seleccionar gráfico
  graphBarrasDiv.hidden = true;
  graphSectorDiv.hidden = true;
} else if (graph == 1) { // Barras
  graphBarrasDiv.hidden = false;
  graphSectorDiv.hidden = true;
} else if (graph == 2) { // Sectores
  graphBarrasDiv.hidden = true;
  graphSectorDiv.hidden = false;
}
```

```js
// Selector de columna
const selectorVsInput = Inputs.select(keys, {label: "Seleccionar columna"});
const selectorVs = Generators.input(selectorVsInput);

// Limitador de datos
const limits = [];
var nlims = 25;
for(var i = 0; i < nlims; i++){
  limits[i] = parseInt(TSV.length * ((i + 1) / nlims), 10);
}
const limitVsInput = Inputs.select(limits, {label: "Límite de elementos"});
const limitVs = Generators.input(limitVsInput);
```

<!-- Gráfico de barras -->

```js
// Datos
var c_data = TSV;
c_data = c_data.filter(function(d,i){
  return i < limitVs;
});

// Elige la primera key que no es un número
var c_key = Object.keys(c_data[0]).find(c_key => c_data[0][c_key] === Object.values(c_data[0]).find((e) => isNaN(e)));

// Dimensiones
var c_width = [...new Set(c_data.map(item => item[c_key]))].length * 30,
    c_height = 600,
    c_marginTop = 20,
    c_marginRight = 0,
    c_marginBottom = 70,
    c_marginLeft = 70;

// Escala X
var c_x = d3.scaleBand()
  .domain(d3.groupSort(c_data, ([d]) => -d[c_key], (d) => d[c_key]))
  .range([c_marginLeft, c_width - c_marginRight])
  .padding(0.1);

// Escala Y
var c_y = d3.scaleLinear()
  .domain([0, d3.max(c_data, function(d) { return +d[selectorVs]; })])
  .range([c_height - c_marginBottom, c_marginTop]);

var c_yAxis = d3.axisLeft(c_y)
  .ticks(10)
  .tickSize(0);

// SVG
const c_svg = d3.create('svg')
  .attr('width', c_width)
  .attr('height', c_height)
  .attr('viewbox', [0, 0, c_width, c_height]);

// Malla
c_svg.selectAll('line.horizontal-grid')
  .data(c_y.ticks(10))
  .enter()
  .append('line')
  .attr('class', 'horizontal-grid')
  .attr('x1', c_marginLeft)
  .attr('y1', (d) => { return c_y(d); })
  .attr('x2', c_width)
  .attr('y2', (d) => { return c_y(d); })
  .style('stroke', 'gray')
  .style('stroke-width', 0.5)
  .style('stroke-dasharray', '3 3');

// Barras
c_svg.append('g')
  .attr('fill', 'steelblue')
  .selectAll()
  .data(c_data)
  .join('rect')
    .attr('x', (d) => c_x(d[c_key]))
    .attr('y', (d) => c_y(d[selectorVs]))
    .attr('height', (d) => (c_height - c_marginBottom) - c_y(d[selectorVs]))
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
  .call(c_yAxis)
  .call(g => g.select('.domain').remove())
  .call(g => g.append('text')
    .attr('x', -c_marginLeft)
    .attr('y', 10)
    .attr('fill', 'currentColor')
    .attr('text-anchor', 'start')
    .text('↑ ' + selectorVs));
```

<!-- Diagrama de sectores -->

```js
// Dimensiones
var tt_margin = 50,
    tt_width = 500,
    tt_height = 500,
    tt_radius = Math.min(tt_width, tt_height) / 2 - tt_margin;

// Datos
var tt_data = TSV;
/*var tt_filter = freq.filter((d) => d.lemma === palabra);
var tt_data = tt_filter.map(d => [
  { key: 'Blog', value: d.blog, percent: d3.format(",.1~f")((d.blog / d.freq) * 100) },
  { key: 'Web', value: d.web, percent: d3.format(",.1~f")((d.web / d.freq) * 100) },
  { key: 'TVM', value: d.TVM, percent: d3.format(",.1~f")((d.TVM / d.freq) * 100) },
  { key: 'Oral', value: d.spok, percent: d3.format(",.1~f")((d.spok / d.freq) * 100) },
  { key: 'Ficción', value: d.fic, percent: d3.format(",.1~f")((d.fic / d.freq) * 100) },
  { key: 'Revista', value: d.mag, percent: d3.format(",.1~f")((d.mag / d.freq) * 100) },
  { key: 'Periódico', value: d.news, percent: d3.format(",.1~f")((d.news / d.freq) * 100) },
  { key: 'Académico', value: d.acad, percent: d3.format(",.1~f")((d.acad / d.freq) * 100) },
]);*/

var tt_key = Object.keys(tt_data[0]).find(tt_key => tt_data[0][tt_key] === Object.values(tt_data[0]).find((e) => isNaN(e)));

// Paleta de colores
var tt_color = d3.scaleOrdinal()
  .domain(["Blog", "Web", "TVM", "Oral", "Ficción", "Revista", "Periódico", "Académico"])
  .range(["#eeba79", "#79ee7f", "#79adee", "#ee79e8", "#e8ee79", "#79eeba", "#7f79ee", "#ee79ae"]);

// Layout del gráfico
var tt_pie = d3.pie()
  .sort(null)
  .value(d => d[selectorVs]);

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
  .selectAll('g')
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
    .attr('fill', d => tt_color(d[tt_key]))
    .attr('stroke-width', '2px')
    .attr('opacity', 0.7)
  .append('title')
    .text(d => `${d[tt_key]}: ${d[selectorVs].toLocaleString("es")}`);

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
      .text(d => d[tt_key]))
    .call(text => text.filter(d => (d.endAngle - d.startAngle) > 0.25).append("tspan")
      .attr('x', 0)
      .attr('y', '0.7em')
      .attr('fill-opacity', 0.7)
      .text(d => d[selectorVs].toLocaleString("es") + "%"));
```

```js
tt_svg
```