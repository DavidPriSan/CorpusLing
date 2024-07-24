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

<div class="grid grid-cols-2">
  <div class="card">
    <h1>Elige el modo de carga de datos</h1>
    <br>
    ${cargaInput}
    <br>
    <div id="carga"></div>
    <div id="TSV">
      ${archivoTSVInput}
    </div>
  </div>
  <div id="muestraTSV" class="card" style="max-height: 350px;">
    ${Inputs.table(archivoTSV.tsv())}
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
```