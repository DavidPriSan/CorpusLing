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

if (pasos == 0) { // Sin seleccionar paso
  paso1Div.hidden = true;
  paso2Div.hidden = true;
} else if (pasos == 1) { // Paso 1 (Carga de datos)
  paso1Div.hidden = false;
  paso2Div.hidden = true;
} else if (pasos == 2) { // Paso 2 (Verificación)
  paso1Div.hidden = true;
  paso2Div.hidden = false;
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
    ${selectorInput}
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

keys.forEach((item) => {
  let th = document.createElement("th");
  th.innerText = item;
  tr.appendChild(th);
});
thead.appendChild(tr);
table.append(tr);

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
const selectorInput = Inputs.select(keys, {label: "Ordenar por"});
const selector = Generators.input(selectorInput);
```

```js

```