---
theme: [air, alt, wide]
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

div.tooltip-donut {
  position: absolute;
  text-align: center;
  padding: .5rem;
  background: #FFFFFF;
  color: #313639;
  border: 1px solid #313639;
  border-radius: 8px;
  pointer-events: none;
  font-size: 1.3rem;
}

table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
  padding: 5px;
}

table {
  margin-left: auto;
  margin-right: auto;
}

th {
  background-color: gainsboro;
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
const cargaInput = Inputs.button(
  [
    [TSVpng, (value) => 1]
  ], 
  { value: 0 }
);
const carga = Generators.input(cargaInput);
```

<!-- Modo de carga -->

```js
// Input TSV
const archivoTSVInput = Inputs.file({
  label: "Archivo TSV",
  accept: ".tsv,.csv,.json",
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
  cargaDiv.innerHTML = "<p>Examina el archivo de tu equipo haciendo click en el botón de abajo, el archivo puede ser TSV, CSV(siendo la primera línea del mismo los encabezados de las columnas en ambos casos) o JSON.</p><br>";
  TSVDiv.hidden = false;
  muestraTSVDiv.hidden = false;
}
```

```js
// Parseo TSV
var arch;
if (archivoTSV.name.split('.')[1] == 'tsv'){
  var arch = archivoTSV.tsv();
} else if (archivoTSV.name.split('.')[1] == 'csv'){
  var arch = archivoTSV.csv( {typed: true} );
} else if (archivoTSV.name.split('.')[1] == 'json'){
  var arch = archivoTSV.json();
}
const archivo = arch;
```

```js
muestraTSV.innerHTML = JSON.stringify(archivo);
const keys = Object.keys(archivo[0]);
```

<!-- Verificación -->

<div id="paso2">
<div class="grid grid-cols-3">
  <div class="card" style="max-height: 100px;"> <!-- Título -->
    <h1>Comprueba que tus datos se ven bien</h1>
  </div>
  <div class="card" style="max-height: 100px;"> <!-- Botones -->
    ${selectorVfInput}
  </div>
  <div class="card" style="max-height: 100px;">
    ${selectorADInput}
  </div>
</div>
<div class="grid grid-cols-3">
  <div id="textoVf" class="card" style="max-height: 400px;"> <!-- Texto -->
    <p>
      Comprueba que tus datos se han procesado correctamente. En la tabla de la derecha puedes ver los 
      <span style="color: royalblue">números</span> 
      de color azul y el 
      <span style="color: seagreen">texto</span> 
      en verde. Una 
      <span style="color: darkred; background-color: lightpink">celda</span> 
      de color rojo indica que hay un dato que no se corresponde con la columna o que hay un problema con el conjunto de datos.
    </p>
    <p>
      Puedes editar el contenido de las celdas haciendo click en cada una de ellas, realiza todos los cambios que consideres antes de avanzar a la parte de visualización.
    </p>
  </div>
  <div id="editColVf" class="card" style="max-height: 400px;" hidden> <!-- Editar columna -->
    <h2>Editar columna</h2>
    <br>
    ${selectorColInput}
    <br>
    ${nombreColInput}
  </div>
  <div class="card grid-colspan-2" style="max-height: 400px;"> <!-- Tabla -->
    <div id="tablaVf" class="scrollable-div"></div>
  </div>
</div>
</div>

<!-- Tabla -->

```js
// Tabla verificación
const container = document.getElementById('tablaVf');
const textoVf = document.getElementById('textoVf');
const editColVf = document.getElementById('editColVf');

// Borra tabla anterior (si existe)
let tablaAnt = document.getElementById('tablaVer');
if (tablaAnt != null) {
  tablaAnt.remove();
}

let table = document.createElement('table');
table.setAttribute('id', 'tablaVer');
let thead = document.createElement('thead');
let tr = document.createElement('tr');
var headerTypes = [];

// Encabezados
keys.forEach((item, i) => {
  let th = document.createElement('th');
  th.innerText = item;
  // Color
  if(isNaN(archivo[0][item])) { // Texto
    headerTypes[i] = 'text';
    th.style.color = 'seagreen';
  } else { // Número
    headerTypes[i] = 'number';
    th.style.color = 'royalblue';
  }

  // Editar columna
  /*th.onclick = function() {
    // Checkea si ya está clickada
    if (this.hasAttribute('data-clicked')) {
      return;
    }

    this.setAttribute('data-clicked', 'yes');
    this.setAttribute('data-text', this.innerText);
    textoVf.hidden = true;
    editColVf.hidden = false;
    selectorColInput.value = headerTypes[i];
    nombreColInput.placeholder = this.innerText;
    nombreColInput.value = this.innerText;

    // Input
    var input = document.createElement('input');
    input.setAttribute('type', 'button');
    input.value = 'Confirmar';
    input.style.width = '100px';
    input.style.height = '50px';
    input.style.border = '5px';
    input.style.fontFamily = 'inherit';
    input.style.fontSize = 'inherit';
    input.style.textAlign = 'inherit';

    input.onclick = function() {
      var orig_text = th.getAttribute('data-text');
      var curr_text = nombreColInput.value;

      if (orig_text != curr_text) { // Hay cambios
        th.removeAttribute('data-clicked');
        th.removeAttribute('data-text');

        // Modificar key
        var new_item = structuredClone(item);
        new_item = curr_text;
        keys[keys.indexOf(item)] = new_item;
        headerTypes[i] = selectorColInput.value;

        // Modificar key en cada objeto
        archivo.forEach( (obj) => {
          delete Object.assign(obj, {[curr_text]: obj[orig_text] })[orig_text];
        });

        // Modificar celda
        th.innerText = curr_text;
        item = new_item;
        th.style.cssText = 'padding: 5px';
      } else { // No hay cambios
        th.removeAttribute('data-clicked');
        th.removeAttribute('data-text');

        // Modificar key
        headerTypes[i] = selectorColInput.value;

        // Modificar celda
        th.innerText = orig_text;
        th.style.cssText = 'padding: 5px';
      }

      // Color
      if(headerTypes[i] == 'text') { // Texto
        th.style.color = 'seagreen';
      } else if(headerTypes[i] == 'number') { // Número
        th.style.color = 'royalblue';
      }

      textoVf.hidden = false;
      editColVf.hidden = true;
      editColVf.removeChild(input);
    }

    editColVf.append(input);
    editColVf.lastElementChild.select();
  }*/

  tr.appendChild(th);
});
thead.appendChild(tr);
table.append(tr);

// Ordenar conjunto
if ((headerTypes[keys.indexOf(selectorVf)] === 'text') && (selectorAD === 'Ascendente')) {
  archivo.sort((a,b) => (a[selectorVf] > b[selectorVf]) ? 1 : ((b[selectorVf] > a[selectorVf]) ? -1 : 0));
} else if ((headerTypes[keys.indexOf(selectorVf)] === 'text') && (selectorAD === 'Descendente')) {
  archivo.sort((a,b) => (a[selectorVf] < b[selectorVf]) ? 1 : ((b[selectorVf] < a[selectorVf]) ? -1 : 0));
} else if ((headerTypes[keys.indexOf(selectorVf)] === 'number') && (selectorAD === 'Ascendente')){
  archivo.sort((a,b) => a[selectorVf] - b[selectorVf]);
} else if ((headerTypes[keys.indexOf(selectorVf)] === 'number') && (selectorAD === 'Descendente')){
  archivo.sort((a,b) => b[selectorVf] - a[selectorVf]);
}

// Datos
archivo.forEach((item) => {
  let tr = document.createElement('tr');
  let vals = Object.values(item);

  vals.forEach((elem, i) => {
    let td = document.createElement('td');
    td.innerText = elem;
    // Color
    if(isNaN(elem) && (headerTypes[i] === 'text')) { // Texto
      td.style.color = 'seagreen';
    } else if (!isNaN(elem) && (headerTypes[i] === 'number')){ // Número
      td.style.color = 'royalblue';
    } else { // Error
      td.style.color = 'darkred';
      td.style.backgroundColor = 'lightpink';
    }

    // Celda editable
    td.onclick = function() {
      // Checkea si ya está clickada
      if (this.hasAttribute('data-clicked')) {
        return;
      }

      this.setAttribute('data-clicked', 'yes');
      this.setAttribute('data-text', this.innerText);

      // Input
      var input = document.createElement('input');
      input.setAttribute('type', 'text');
      input.value = this.innerText;
      input.style.width = (this.offsetWidth - 5) + 'px';
      input.style.height = (this.offsetHeight - 5) + 'px';
      input.style.border = '0px';
      input.style.fontFamily = 'inherit';
      input.style.fontSize = 'inherit';
      input.style.textAlign = 'inherit';
      input.style.backgroundColor = 'LightGoldenRodYellow';

      input.onblur = function() {
        var orig_text = td.getAttribute('data-text');
        var curr_text = this.value;

        if (orig_text != curr_text) { // Hay cambios
          td.removeAttribute('data-clicked');
          td.removeAttribute('data-text');

          // Modificar objeto
          var new_item = structuredClone(item);
          new_item[keys[i]] = curr_text;
          archivo[archivo.indexOf(item)] = new_item;

          // Modificar celda
          td.innerText = curr_text;
          item = new_item;
          td.style.cssText = 'padding: 5px';
        } else { // No hay cambios
          td.removeAttribute('data-clicked');
          td.removeAttribute('data-text');

          // Modificar celda
          td.innerText = orig_text;
          td.style.cssText = 'padding: 5px';
        }

        // Color
        if(isNaN(curr_text) && (headerTypes[i] === 'text')) { // Texto
          td.style.color = 'seagreen';
        } else if (!isNaN(curr_text) && (headerTypes[i] === 'number')){ // Número
          td.style.color = 'royalblue';
        } else { // Error
          td.style.color = 'darkred';
          td.style.backgroundColor = 'lightpink';
        }
      }

      // Guardar cambios con tecla Enter
      input.onkeypress = function(e) {
        if (e.keyCode == 13) {
          this.blur();
        }
      }

      this.innerText = '';
      this.style.cssText = 'padding: 0px 0px';
      this.append(input);
      this.firstElementChild.select();
    }

    tr.appendChild(td);
  });
  table.appendChild(tr);
});
container.appendChild(table);
```

<!-- Botones verificación -->

```js
// Selector columna
const selectorVfInput = Inputs.select(keys, {label: "Ordenar por"});
const selectorVf = Generators.input(selectorVfInput);

// Selector asc/desc
const selectorADInput = Inputs.select(["Ascendente", "Descendente"]);
const selectorAD = Generators.input(selectorADInput);

// Selector tipo columna
const selectorColInput = Inputs.select(["number", "text"], {label: "Tipo"});
const selectorCol = Generators.input(selectorColInput);

// Input columna
const nombreColInput = Inputs.text({
  label: "Nombre"
});
const nombreCol = Generators.input(nombreColInput);
```

<!-- Visualización -->

<div id="paso3">
  <div class="grid grid-cols-3">
    <div class="card"> <!-- Texto -->
      <h1>Elige el tipo de gráfico</h1>
      <br>
      ${graphInput}
    </div>
    <div class="card grid-colspan-2" style="max-height: 1200px;"> <!-- Gráfico -->
      <div id="graphButtons">
        ${selectorVsInput}
        ${limitVsInput}
      </div>
      <div id="graphBarras" style="overflow-y: scroll">
      </div>
      <div id="graphSector">
      </div>
      <div id="sunburstButtons">
        ${limitSbInput}
      </div>
      <div id="graphSunburst">
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
    ["Diagrama de sectores", (value) => 2],
    ["Zoomable sunburst", (value) => 3]
  ],
  { value: 0 }
);
const graph = Generators.input(graphInput);
```

<!-- Elección gráfico -->

```js
const graphBarrasDiv = document.getElementById("graphBarras");
const graphSectorDiv = document.getElementById("graphSector");
const graphSunburstDiv = document.getElementById("graphSunburst");
const graphButtonsDiv = document.getElementById("graphButtons");
const sunburstButtonsDiv = document.getElementById("sunburstButtons");

if (graph == 0) { // Sin seleccionar gráfico
  graphBarrasDiv.hidden = true;
  graphSectorDiv.hidden = true;
  graphSunburstDiv.hidden = true;
  graphButtonsDiv.hidden = true;
  sunburstButtonsDiv.hidden = true;
} else if (graph == 1) { // Barras
  graphBarrasDiv.hidden = false;
  graphSectorDiv.hidden = true;
  graphSunburstDiv.hidden = true;
  graphButtonsDiv.hidden = false;
  sunburstButtonsDiv.hidden = true;
} else if (graph == 2) { // Sectores
  graphBarrasDiv.hidden = true;
  graphSectorDiv.hidden = false;
  graphSunburstDiv.hidden = true;
  graphButtonsDiv.hidden = false;
  sunburstButtonsDiv.hidden = true;
}  else if (graph == 3) { // Zoomable Sunburst
  graphBarrasDiv.hidden = true;
  graphSectorDiv.hidden = true;
  graphSunburstDiv.hidden = false;
  graphButtonsDiv.hidden = true;
  sunburstButtonsDiv.hidden = false;
}
```

```js
// Selector de columna
const selectorVsInput = Inputs.select(keys, {label: "Seleccionar columna"});
const selectorVs = Generators.input(selectorVsInput);

// Limitador de datos
const limitVsInput = Inputs.range([1, archivo.length], {step: 1, label: "Límite de elementos"});
const limitVs = Generators.input(limitVsInput);

// Limitador Sunburst
const limitSbInput = Inputs.range([1, 50], {step: 1, label: "Límite de elementos"});
const limitSb = Generators.input(limitSbInput);
```

<!-- Gráfico de barras -->

```js
// Datos
const c_data = archivo.filter(function(d,i){
  return i < limitVs;
});

// Elige la primera key que no es un número
const c_key = Object.keys(c_data[0]).find(c_key => c_data[0][c_key] === Object.values(c_data[0]).find((e) => isNaN(e)));

// Dimensiones
const c_width = Math.max(200, [...new Set(c_data.map(item => item[c_key]))].length * 30),
      c_height = 600,
      c_marginTop = 20,
      c_marginRight = 0,
      c_marginBottom = 70,
      c_marginLeft = 70;

// Escala X
const c_x = d3.scaleBand()
  .domain(d3.groupSort(c_data, ([d]) => -d[c_key], (d) => d[c_key]))
  .range([c_marginLeft, c_width - c_marginRight])
  .padding(0.1);

// Escala Y
const c_y = d3.scaleLinear()
  .domain([0, d3.max(c_data, function(d) { return +d[selectorVs]; })])
  .range([c_height - c_marginBottom, c_marginTop]);

const c_yAxis = d3.axisLeft(c_y)
  .ticks(10)
  .tickSize(0);

// Borra gráfico anterior (si existe)
let barrasAnt = document.getElementById('barras');
if (barrasAnt != null) {
  barrasAnt.remove();
}

// SVG
const c_svg = d3.select('#graphBarras').append('svg')
  .attr('id', 'barras')
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
const tt_margin = 20,
    tt_width = 900,
    tt_height = 900,
    tt_radius = Math.min(tt_width, tt_height) / 2 - tt_margin;

// Datos
const tt_data = archivo.filter(function(d,i){
  return i < limitVs;
});

// Key para identificar elementos (primera no numérica)
const tt_key = Object.keys(tt_data[0]).find(tt_key => tt_data[0][tt_key] === Object.values(tt_data[0]).find((e) => isNaN(e)));

// Paleta de colores
const tt_color = d3.scaleOrdinal(d3.quantize(d3.interpolateRainbow, [...new Set(tt_data.map(item => item[selectorVs]))].length + 1));

// Layout del gráfico
const tt_pie = d3.pie()
  .sort(null)
  .value(d => d[selectorVs]);

// Generador de arcos
const tt_arc = d3.arc()
  .innerRadius(0)
  .outerRadius(tt_radius * 0.8);

// Arcos para el ratón
const tt_hoverArc = d3.arc()
  .innerRadius(0)
  .outerRadius(tt_radius);

// Borra gráfico anterior (si existe)
let sectorAnt = document.getElementById('sector');
if (sectorAnt != null) {
  sectorAnt.remove();
}

// SVG
const tt_svg = d3.select('#graphSector').append('svg')
  .attr('id', 'sector')
  .attr('width', tt_width)
  .attr('height', tt_height)
  .attr('style', 'font: 14px sans-serif;')
  .attr('viewBox', [-tt_width / 2, -tt_height / 2, tt_width, tt_height]);

// Tooltip
var tt_hoverDiv = d3.select('#graphSector').append('div')
  .attr('class', 'tooltip-donut')
  .style('opacity', 0);

// Sectores
const tt_g = tt_svg.selectAll('.arc')
  .data(tt_pie(tt_data))
  .enter().append('g')
  .attr('class', 'arc');

tt_g.append('path')
  .attr('d', tt_arc)
  .attr('class', 'arc')
  .style('fill', (d, i) => tt_color(i))
  .style('fill-opacity', 0.8)
  .style('stroke', 'black')
  .style('stroke-width', 1)
  .on('mouseover', function (d, i) { // Ratón encima del sector
    // Resaltar sector
    d3.select(this)
      .style('fill-opacity', 1)
      .transition().duration(500)
      .attr('d', tt_hoverArc);
    // Mostrar tooltip
    tt_hoverDiv.transition()
      .duration(50)
      .style('opacity', 1);
    // Texto
    let label = tt_data.find(x => x[selectorVs] === (i.value).toString())[tt_key] + ': ' + i.value;
    tt_hoverDiv.html(label)
      // Coordenadas
      .style('left', (d3.pointer(d)[0] + document.getElementById('graphSector').getBoundingClientRect().x) + 150 + 'px')
      .style('top', (d3.pointer(d)[1] + document.getElementById('graphSector').getBoundingClientRect().x) + 175 + 'px');
  })
  .on('mouseout', function (d, i) { // Ratón sale del sector
    // Volver sector a la normalidad
    d3.select(this)
      .style('fill-opacity', 0.8)
      .transition().duration(500)
      .attr('d', tt_arc);
    // Ocultar tooltip
    tt_hoverDiv.transition()
      .duration(50)
      .style('opacity', 0);
  });
```

<!-- Zoomable sunburst -->

```js
if( archivo[0].children === undefined ) {
  graphSunburstDiv.innerHTML = "<p>Los datos son incompatibles con este gráfico, por favor seleccione otro tipo de gráfico.</p>";
} else{
  graphSunburstDiv.innerHTML = "";

  // Datos
  var tempArchivo = structuredClone(archivo);
  var sb_data = limitData(tempArchivo[0], limitSb);

  // Dimensiones
  const ng_width = 950,
        ng_height = ng_width,
        ng_radius = ng_width / 6;

  // Paleta de colores
  const ng_color = d3.scaleOrdinal(d3.quantize(d3.interpolateRainbow, sb_data.children.length + 1));

  // Layout
  const ng_hierarchy = d3.hierarchy(sb_data)
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

  // Borra gráfico anterior (si existe)
  let sunburstAnt = document.getElementById('sunburst');
  if (sunburstAnt != null) {
    sunburstAnt.remove();
  }

  // SVG
  const ng_svg = d3.select('#graphSunburst').append('svg')
    .attr('id', 'sunburst')
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

  // Title
  const ng_format = d3.format(",d");
  ng_path.append('title')
      .text(d => `${d.ancestors().map(d => d.data.name).reverse().join("/")}\n${ng_format(d.value)}`);

  // Label
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

  // Para eventos del ratón
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

  // Posición labels
  function labelTransform(d) {
    const x = (d.x0 + d.x1) / 2 * 180 / Math.PI;
    const y = (d.y0 + d.y1) / 2 * ng_radius;
    return `rotate(${x - 90}) translate(${y},0) rotate(${x < 180 ? 0 : 180})`;
  }

  // Limitar hijos
  function limitData(d, i) {
    if (d.hasOwnProperty('children')) {
      if(d.children.length > i) {
        d.children = d.children.slice(0, i);
      }
      d.children.forEach((e) => limitData(e, i));
      return d;
    }
    return d;
  }
}
```