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

</style>

<div class="hero">
  <h1>CorpusLing</h1>
  <h2>TFG Grado en Ingeniería Informática</h2>
</div>


<!-- Botones pasos -->

```js
const pasosInput = Inputs.button([
  ["Paso 1: Carga de datos", value => 1],
  ["Paso 2: Verificación", value => 2]
], {value: 0});
const pasos = Generators.input(pasosInput);
```

<div class="card">
  ${pasosInput}
</div>

<!-- Procesamiento pasos -->

```js
const paso1Div = document.getElementById('paso1');
const paso2Div = document.getElementById('paso2');

if (pasos == 0) {
  paso1Div.hidden = true;
  paso2Div.hidden = true;
} else if (pasos == 1) {
  paso1Div.hidden = false;
  paso2Div.hidden = true;
}  else if (pasos == 2) {
  paso1Div.hidden = true;
  paso2Div.hidden = false;
}
```


<!-- Botones carga de datos -->

```js
const TSVpng = FileAttachment("TSV.png").image({width: 64});
```

```js
const cargaInput = Inputs.button([
  [TSVpng, value => 1]
], {value: 0});
const carga = Generators.input(cargaInput);
```

<!-- Modo de carga -->

```js
const archivoTSVInput = Inputs.file({label: "Archivo TSV", accept: ".tsv", required: true, width: 310});
const archivoTSV = Generators.input(archivoTSVInput);
```

<div id="paso1">
<div class="grid grid-cols-2">
  <div class="card">
    <h1>Elige el modo de carga de datos</h1>
    <br>
    ${cargaInput}
    <br>
    <div id="carga"></div>
    <div id="TSV">
      <input type="file" id="archivoTSV" name="archivoTSV" accept=".tsv">
      ${archivoTSVInput}
    </div>
  </div>
  <div id="muestraTSV" class="card" style="max-height: 350px;">
    
  </div>
</div>
</div>


<!-- Examinar TSV -->

```js
const cargaDiv = document.getElementById('carga');
const TSVDiv = document.getElementById('TSV');
const muestraTSVDiv = document.getElementById('muestraTSV');

if (carga == 0) {
  cargaDiv.innerHTML = '<p>Puedes elegir como quieres cargar tus datos pulsando los distintos botones de arriba.</p>';
  TSVDiv.hidden = true;
  muestraTSVDiv.hidden = true;
} else if (carga == 1) {
  cargaDiv.innerHTML = '<p>Examina el archivo TSV de tu equipo haciendo click en el botón de abajo (siendo la primera línea del mismo los encabezados de las columnas).</p><br>';
  TSVDiv.hidden = false;
  muestraTSVDiv.hidden = false;
}

function handle_tsv(evt) {
  let fl_files = evt.target.files;
  let fl_file = fl_files[0];

  let reader = new FileReader();

  let muestra_tsv = (e) => {
    document.getElementById('muestraTSV').innerHTML = e.target.result;
  }

  let on_reader_load  = (fl) => {
    return muestra_tsv;
  }

  reader.onload = on_reader_load(fl_file);
  reader.readAsText(fl_file);
}

document.getElementById('archivoTSV').addEventListener('change', handle_tsv, false);
```


<!-- Botones verificación -->

```js

```

<!-- Verificación -->

```js

```

<div id="paso2">
<div class="grid grid-cols-3">
  <div class="card">
    <h1>Elige el modo de carga de datos</h1>
  </div>
  <div id="tabla" class="card grid-colspan-2" style="max-height: 350px;">
  </div>
</div>
</div>