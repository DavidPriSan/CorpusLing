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
const ArchivoLocalpng = FileAttachment("ArchivoLocal.png").image({ width: 64 });
const DatosMuestrapng = FileAttachment("DatosMuestra.png").image({ width: 64 });
```

```js
// Botonera
const cargaInput = Inputs.button(
  [
    [ArchivoLocalpng, (value) => 1],
    [DatosMuestrapng, (value) => 2]
  ], 
  { value: 0 }
);
const carga = Generators.input(cargaInput);
```

<!-- Modo de carga -->

```js
// Input archivo local
const archivoLocalInput = Inputs.file({
  label: "Selecciona tu archivo local",
  accept: ".tsv,.csv,.json",
  width: 310,
});
const archivoLocal = Generators.input(archivoLocalInput);

// Selector datos de muestra
const selectorDMInput = Inputs.select(["", "Ngrams (COCA)", "Collocates (COCA)", "Word Frequency (COCA)", "Ngrams (Modificado)"], {label: "Selecciona un conjunto de datos", value: ""});
const selectorDM = Generators.input(selectorDMInput);
```

```js
// Datos de muestra
const coca_ngrams = FileAttachment("./data/coca_ngrams.tsv").tsv();
const collocates = FileAttachment("./data/collocates.tsv").tsv();
const ngrams = FileAttachment("./data/ngrams.json").json();
const wordFrequency = FileAttachment("./data/wordFrequency.tsv").tsv();
```

<div id="paso1">
<div class="grid grid-cols-2">
  <div class="card"> <!-- Elegir modo -->
    <h1>Elige el modo de carga de datos</h1>
    <br>
    ${cargaInput}
    <br>
    <div id="carga"></div>
    <div id="aLocal">
      ${archivoLocalInput}
    </div>
    <div id="datosMuestra">
      ${selectorDMInput}
    </div>
  </div>
  <div class="card" style="max-height: 350px;"> <!-- Visualización de datos -->
    <div id="muestraJson" class="scrollable-div"></div>
  </div>
</div>
</div>

```js
const cargaDiv = document.getElementById("carga");
const aLocalDiv = document.getElementById("aLocal");
const datosMuestraDiv = document.getElementById("datosMuestra");
const muestraJsonDiv = document.getElementById("muestraJson");

if (carga == 0) { // Sin seleccionar modo
  cargaDiv.innerHTML = "<p>Puedes elegir como quieres cargar tus datos pulsando los distintos botones de arriba.</p>";
  aLocalDiv.hidden = true;
  muestraJsonDiv.hidden = true;
  datosMuestraDiv.hidden = true;
} else if (carga == 1) { // Examinar Archivo
  cargaDiv.innerHTML = "<p>Examina el archivo de tu equipo haciendo click en el botón de abajo, el archivo puede ser TSV, CSV(siendo la primera línea del mismo los encabezados de las columnas en ambos casos) o JSON.</p><br>";
  aLocalDiv.hidden = false;
  muestraJsonDiv.hidden = false;
  datosMuestraDiv.hidden = true;
} else if (carga == 2) { // Datos de muestra
  cargaDiv.innerHTML = "<p>Desde CorpusLing ofrecemos varios archivos de muestra para probar el funcionamiento de la página y las distintas posibilidades que ofrecemos.</p><p>Estos conjuntos son muestras del corpus COCA ofrecidos por <a href=\"https://www.english-corpora.org/\">English Corpora</a></p><a href=\"https://www.wordfrequency.info/\">Word Frequency</a><br><a href=\"https://www.ngrams.info/\">N-Grams</a><br><a href=\"https://www.collocates.info/\">Collocates</a><br><br>";
  aLocalDiv.hidden = true;
  muestraJsonDiv.hidden = false;
  datosMuestraDiv.hidden = false;
}
```

```js
console.log("1");
console.log(archivoLocal);
```

```js
console.log("2");
console.log(archivoLocalInput.value);
```

```js
// Parseo de archivo
var arch = [{}];
var arch1 = [{}];
var arch2 = [{}];

// Muestra
if(selectorDMInput.value != "") {
  if(selectorDM == "Ngrams (COCA)") {
    arch2 = coca_ngrams;
  } else if(selectorDM == "Collocates (COCA)") {
    arch2 = collocates;
  } else if(selectorDM == "Word Frequency (COCA)") {
    arch2 = wordFrequency;
  } else if(selectorDM == "Ngrams (Modificado)") {
    arch2 = ngrams;
  }
}
 // Local
if(archivoLocalInput.value != undefined) {
  console.log("3");
  console.log(archivoLocalInput.value);
  if(archivoLocal.name.split('.')[1] == 'tsv') {
    arch1 = archivoLocal.tsv();
  } else if(archivoLocal.name.split('.')[1] == 'csv') {
    arch1 = archivoLocal.csv( {typed: true} );
  } else if(archivoLocal.name.split('.')[1] == 'json') {
    arch1 = archivoLocal.json();
  }
}

if(carga == 1) {
  arch = arch1;
} else if(carga == 2) {
  arch = arch2;
}

const archivo = arch;
```

```js
// Muestra archivo (formato json)
if(JSON.stringify(archivo) != "[{}]") {
  muestraJsonDiv.innerHTML = JSON.stringify(archivo);
} else {
  muestraJsonDiv.innerHTML = "";
}

// Keys
const keys = Object.keys(archivo[0]);
```

```js
// Tipos de las keys
const keysTypes = [];
keys.forEach((item, i) => {
  if(isNaN(archivo[0][item])) { // Texto
    keysTypes[i] = 'text';
  } else { // Número
    keysTypes[i] = 'number';
  }
});
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

// Encabezados
keys.forEach((item, i) => {
  let th = document.createElement('th');
  th.innerText = item;

  // Color
  if(keysTypes[i] == 'text') {
    th.style.color = 'seagreen';
  } else if(keysTypes[i] == 'number') {
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
    selectorColInput.value = keysTypes[i];
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
        //keys[keys.indexOf(item)] = new_item;
        keysTypes[i] = selectorColInput.value;

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
        keysTypes[i] = selectorColInput.value;

        // Modificar celda
        th.innerText = orig_text;
        th.style.cssText = 'padding: 5px';
      }

      // Color
      if(keysTypes[i] == 'text') { // Texto
        th.style.color = 'seagreen';
      } else if(keysTypes[i] == 'number') { // Número
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
if ((keysTypes[keys.indexOf(selectorVf)] === 'text') && (selectorAD === 'Ascendente')) {
  archivo.sort((a,b) => (a[selectorVf] > b[selectorVf]) ? 1 : ((b[selectorVf] > a[selectorVf]) ? -1 : 0));
} else if ((keysTypes[keys.indexOf(selectorVf)] === 'text') && (selectorAD === 'Descendente')) {
  archivo.sort((a,b) => (a[selectorVf] < b[selectorVf]) ? 1 : ((b[selectorVf] < a[selectorVf]) ? -1 : 0));
} else if ((keysTypes[keys.indexOf(selectorVf)] === 'number') && (selectorAD === 'Ascendente')){
  archivo.sort((a,b) => a[selectorVf] - b[selectorVf]);
} else if ((keysTypes[keys.indexOf(selectorVf)] === 'number') && (selectorAD === 'Descendente')){
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
    if(isNaN(elem) && (keysTypes[i] === 'text')) { // Texto
      td.style.color = 'seagreen';
    } else if (!isNaN(elem) && (keysTypes[i] === 'number')){ // Número
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
        if(isNaN(curr_text) && (keysTypes[i] === 'text')) { // Texto
          td.style.color = 'seagreen';
        } else if (!isNaN(curr_text) && (keysTypes[i] === 'number')){ // Número
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
    <div class="card grid-colspan-2" style="max-height: 1400px;"> <!-- Gráfico -->
      <div id="graphButtons">
        ${selectorIdInput}
        ${selectorVsInput}
        ${limitVsInput}
      </div>
      <div id="graphButtonsLimits">
        ${ordenarVsInput}
      </div>
      <div id="graphBarras" style="overflow-y: scroll">
      </div>
      <div id="graphSector">
      </div>
      <div id="hexbinButtons">
        ${selectorRadioInput}
      </div>
      <div id="graphHexbin">
      </div>
      <div id="sunburstButtons">
        ${limitSbInput}
      </div>
      <div id="graphSunburst">
      </div>
      <div id="graphIcicle" style="overflow-y: hidden">
      </div>
      <div id="graphTree" style="max-height: 1200px; overflow-y: scroll">
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
    ["Hexbin", (value) => 3],
    ["Zoomable sunburst", (value) => 4],
    ["Zoomable Icicle", (value) => 5],
    ["Collapsible Tree", (value) => 6]
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
const graphButtonsLimitsDiv = document.getElementById("graphButtonsLimits");
const sunburstButtonsDiv = document.getElementById("sunburstButtons");
const graphHexbinDiv = document.getElementById("graphHexbin");
const hexbinButtonsDiv = document.getElementById("hexbinButtons");
const graphIcicleDiv = document.getElementById("graphIcicle");
const graphTreeDiv = document.getElementById("graphTree");

if (graph == 0) { // Sin seleccionar gráfico
  graphBarrasDiv.hidden = true;
  graphSectorDiv.hidden = true;
  graphSunburstDiv.hidden = true;
  graphButtonsDiv.hidden = true;
  graphButtonsLimitsDiv.hidden = true;
  sunburstButtonsDiv.hidden = true;
  graphHexbinDiv.hidden = true;
  hexbinButtonsDiv.hidden = true;
  graphIcicleDiv.hidden = true;
  graphTreeDiv.hidden = true;
} else if (graph == 1) { // Barras
  graphBarrasDiv.hidden = false;
  graphSectorDiv.hidden = true;
  graphSunburstDiv.hidden = true;
  graphButtonsDiv.hidden = false;
  graphButtonsLimitsDiv.hidden = false;
  sunburstButtonsDiv.hidden = true;
  graphHexbinDiv.hidden = true;
  hexbinButtonsDiv.hidden = true;
  graphIcicleDiv.hidden = true;
  graphTreeDiv.hidden = true;
} else if (graph == 2) { // Sectores
  graphBarrasDiv.hidden = true;
  graphSectorDiv.hidden = false;
  graphSunburstDiv.hidden = true;
  graphButtonsDiv.hidden = false;
  graphButtonsLimitsDiv.hidden = false;
  sunburstButtonsDiv.hidden = true;
  graphHexbinDiv.hidden = true;
  hexbinButtonsDiv.hidden = true;
  graphIcicleDiv.hidden = true;
  graphTreeDiv.hidden = true;
} else if (graph == 3) { // Hexbin
  graphBarrasDiv.hidden = true;
  graphSectorDiv.hidden = true;
  graphSunburstDiv.hidden = true;
  graphButtonsDiv.hidden = false;
  graphButtonsLimitsDiv.hidden = true;
  sunburstButtonsDiv.hidden = true;
  graphHexbinDiv.hidden = false;
  hexbinButtonsDiv.hidden = false;
  graphIcicleDiv.hidden = true;
  graphTreeDiv.hidden = true;
} else if (graph == 4) { // Zoomable Sunburst
  graphBarrasDiv.hidden = true;
  graphSectorDiv.hidden = true;
  graphSunburstDiv.hidden = false;
  graphButtonsDiv.hidden = true;
  graphButtonsLimitsDiv.hidden = true;
  sunburstButtonsDiv.hidden = false;
  hexbinButtonsDiv.hidden = true;
  graphIcicleDiv.hidden = true;
  graphTreeDiv.hidden = true;
} else if (graph == 5) { // Zoomable Icicle
  graphBarrasDiv.hidden = true;
  graphSectorDiv.hidden = true;
  graphSunburstDiv.hidden = true;
  graphButtonsDiv.hidden = true;
  graphButtonsLimitsDiv.hidden = true;
  sunburstButtonsDiv.hidden = false;
  hexbinButtonsDiv.hidden = true;
  graphIcicleDiv.hidden = false;
  graphTreeDiv.hidden = true;
}  else if (graph == 6) { // Collapsible Tree
  graphBarrasDiv.hidden = true;
  graphSectorDiv.hidden = true;
  graphSunburstDiv.hidden = true;
  graphButtonsDiv.hidden = true;
  graphButtonsLimitsDiv.hidden = true;
  sunburstButtonsDiv.hidden = false;
  hexbinButtonsDiv.hidden = true;
  graphIcicleDiv.hidden = true;
  graphTreeDiv.hidden = false;
}
```

<!-- Botones -->

```js
// Keys divididas por tipo
const keysText = [];
const keysNumber = [];

keys.forEach((item, i) => {
  if(keysTypes[i] == "text") {
    keysText.push(item);
  } else if(keysTypes[i] == "number") {
    keysNumber.push(item);
  }
});

// Selector de identificador
const selectorIdInput = Inputs.select(keysText, {label: "Selecciona identificador"});
const selectorId = Generators.input(selectorIdInput);

// Selector de columna
const selectorVsInput = Inputs.select(keysNumber, {label: "Selecciona columna"});
const selectorVs = Generators.input(selectorVsInput);

// Limitador de datos
const limitVsInput = Inputs.range([1, archivo.length], {step: 1, label: "Límite de elementos", value: (archivo.length / 10)});
const limitVs = Generators.input(limitVsInput);

// Limitador Sunburst
const limitSbInput = Inputs.range([1, 50], {step: 1, label: "Límite de elementos", value: 5});
const limitSb = Generators.input(limitSbInput);

// Ordenar por id/dato
const ordenarVsInput = Inputs.select(["Identificador", "Valor"], {label: "Ordenar por"});
const ordenarVs = Generators.input(ordenarVsInput);

// Selector Radio
const selectorRadioInput = Inputs.range([2, 20], {step: 1, label: "Radio"});
const selectorRadio = Generators.input(selectorRadioInput);
```

<!-- Gráfico de barras -->

```js
if(keysText.length === 0 || keysNumber.length === 0) {
  graphBarrasDiv.innerHTML = "<div class=\"caution\">Los datos son incompatibles con este gráfico, por favor seleccione otro tipo de gráfico.</div>";
  graphInput[0].disabled = true;
} else {
  graphBarrasDiv.innerHTML = "";
  graphInput[0].disabled = false;

  // Datos
  const c_data = archivo.filter(function(d,i){
    return i < limitVs;
  });

  // Elige la key
  const c_key = selectorId;

  // Agrupar por identificador
  const c_grouped = [];
  c_data.forEach((item) => {
    var groupedO = c_grouped.find(o => { return o[c_key] == item[c_key]});
    if (groupedO != undefined) {
      keysNumber.forEach((key) => {
        let num = Number(groupedO[key]) + Number(item[key])
        groupedO[key] = num.toString();
      });
    } else {
      c_grouped.push(structuredClone(item));
    }
  });

  // Dimensiones
  const c_width = Math.max(200, [...new Set(c_grouped.map(item => item[c_key]))].length * 30),
        c_height = 600,
        c_marginTop = 20,
        c_marginRight = 0,
        c_marginBottom = 70,
        c_marginLeft = 70;

  // Escala X
  const c_x = d3.scaleBand();

  if(ordenarVs == "Identificador") { // Ordenado por id
    c_x.domain(d3.groupSort(c_grouped, ([d]) => -d[c_key], (d) => d[c_key]))
      .range([c_marginLeft, c_width - c_marginRight])
      .padding(0.1);
  } else if(ordenarVs == "Valor") { // Ordenado por valor
    c_x.domain(d3.groupSort(c_grouped, ([d]) => -d[selectorVs], (d) => d[c_key]))
      .range([c_marginLeft, c_width - c_marginRight])
      .padding(0.1);
  }  

  // Escala Y
  const c_y = d3.scaleLinear()
    .domain([0, d3.max(c_grouped, function(d) { return +d[selectorVs]; })])
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
    .data(c_grouped)
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
}
```

<!-- Diagrama de sectores -->

```js
if(keysText.length === 0 || keysNumber.length === 0) {
  graphSectorDiv.innerHTML = "<div class=\"caution\">Los datos son incompatibles con este gráfico, por favor seleccione otro tipo de gráfico.</div>";
  graphInput[1].disabled = true;
} else {
  graphSectorDiv.innerHTML = "";
  graphInput[1].disabled = false;

  // Dimensiones
  const tt_margin = 20,
      tt_width = 900,
      tt_height = 900,
      tt_radius = Math.min(tt_width, tt_height) / 2 - tt_margin;

  // Datos
  const tt_data = archivo.filter(function(d,i){
    return i < limitVs;
  });

  // Key para identificar elementos
  const tt_key = selectorId;

  // Agrupar por identificador
  const tt_grouped = [];
  tt_data.forEach((item) => {
    var groupedO = tt_grouped.find(o => { return o[tt_key] == item[tt_key]});
    if (groupedO != undefined) {
      keysNumber.forEach((key) => {
        let num = Number(groupedO[key]) + Number(item[key])
        groupedO[key] = num.toString();
      });
    } else {
      tt_grouped.push(structuredClone(item));
    }
  });

  // Ordenar conjunto
  if(ordenarVs == "Identificador") { // Por id
    tt_grouped.sort((a, b) => d3.ascending(a[tt_key], b[tt_key]));
  } else if(ordenarVs == "Valor") { // Por valor
    tt_grouped.sort(function(a, b) { return (b[selectorVs] - a[selectorVs]); });
  }

  // Paleta de colores
  const tt_color = d3.scaleOrdinal(d3.quantize(d3.interpolateRainbow, [...new Set(tt_grouped.map(item => item[selectorVs]))].length + 1));

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
    .data(tt_pie(tt_grouped))
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
      let label = tt_grouped.find(x => x[selectorVs] === (i.value).toString())[tt_key] + ': ' + i.value;
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
}
```
<!-- Hexbin -->

```js
import * as d3hexbin from "d3-hexbin";

if(keysText.length === 0 || keysNumber.length === 0) {
  graphHexbinDiv.innerHTML = "<div class=\"caution\">Los datos son incompatibles con este gráfico, por favor seleccione otro tipo de gráfico.</div>";
  graphInput[2].disabled = true;
} else {
  graphHexbinDiv.innerHTML = "";
  graphInput[2].disabled = false;

  // Dimensiones
  const hb_width = 650;
  const hb_height = hb_width;
  const hb_marginTop = 20;
  const hb_marginRight = 20;
  const hb_marginBottom = 30;
  const hb_marginLeft = 40;

  // Datos
  const hb_data = archivo.filter(function(d,i){
    return i < limitVs;
  });

  // Escala X
  const hb_x = d3.scaleBand()
    .domain(d3.groupSort(hb_data, ([d]) => -d[selectorId], (d) => d[selectorId]))
    .range([hb_marginLeft, hb_width - hb_marginRight]);

  // Escala Y
  const hb_y = d3.scaleLinear()
    .domain([0, d3.max(hb_data, function(d) { return +d[selectorVs]; })])
    .rangeRound([hb_height - hb_marginBottom, hb_marginTop]);

  // Clasificación de datos
  const hb_hexbin = d3hexbin.hexbin()
    .x(d => hb_x(d[selectorId]))
    .y(d => hb_y(d[selectorVs]))
    .radius(selectorRadio)
    .extent([[hb_marginLeft, hb_marginTop], [hb_width - hb_marginRight, hb_height - hb_marginBottom]]);

  const hb_bins = hb_hexbin(hb_data);

  // Escala de color
  const hb_color = d3.scaleSequential(d3.interpolateBuPu)
    .domain([0, d3.max(hb_bins, d => d.length) / 2]);

  // Borra gráfico anterior (si existe)
  let hexbinAnt = document.getElementById('hexbin');
  if (hexbinAnt != null) {
    hexbinAnt.remove();
  }

  // SVG
  const hb_svg = d3.select('#graphHexbin').append('svg')
    .attr('id', 'hexbin')
    .attr('viewBox', [0, 0, hb_width, hb_height]);

  // Eje X
  hb_svg.append('g')
      .attr('transform', `translate(0, ${hb_height - 10})`)
      .call(d3.axisBottom(hb_x).tickSizeOuter(0))
      .call(g => g.select('.domain').remove())
      .call(g => g.append('text')
          .attr('x', hb_width - hb_marginRight)
          .attr('y', -4)
          .attr('fill', 'currentColor')
          .attr('font-weight', 'bold')
          .attr('text-anchor', 'end')
          .text(selectorId));

  // Eje Y
  hb_svg.append('g')
      .attr('transform', `translate(${hb_marginLeft}, 0)`)
      .call(d3.axisLeft(hb_y).ticks(null, '.1s'))
      .call(g => g.select('.domain').remove())
      .call(g => g.append('text')
          .attr('x', 4)
          .attr('y', hb_marginTop)
          .attr('dy', '.75em')
          .attr('fill', 'currentColor')
          .attr('font-weight', 'bold')
          .attr('text-anchor', 'start')
          .text(selectorVs));

  // Hexágonos
  hb_svg.append('g')
      .attr('fill', '#ddd')
      .attr('stroke', 'black')
    .selectAll('path')
    .data(hb_bins)
    .enter().append('path')
      .attr('transform', d => `translate(${d.x},${d.y})`)
      .attr('d', hb_hexbin.hexagon())
      .attr('fill', bin => hb_color(bin.length));
}
```

<!-- Zoomable sunburst -->

```js
if( archivo[0].children === undefined ) {
  graphSunburstDiv.innerHTML = "<div class=\"caution\">Los datos son incompatibles con este gráfico, por favor seleccione otro tipo de gráfico.</div>";
  graphInput[3].disabled = true;
} else{
  graphInput[3].disabled = false;
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

<!-- Zoomable Icicle -->

```js
if( archivo[0].children === undefined ) {
  graphIcicleDiv.innerHTML = "<div class=\"caution\">Los datos son incompatibles con este gráfico, por favor seleccione otro tipo de gráfico.</div>";
  graphInput[4].disabled = true;
} else{
  graphInput[4].disabled = false;
  graphIcicleDiv.innerHTML = "";

  // Datos
  var tempArchivo = structuredClone(archivo);
  var ic_data = limitData(tempArchivo[0], limitSb);

  // Dimensiones
  const ic_width = 928;
  const ic_height = 1200;

  // Escala de colores
  const ic_color = d3.scaleOrdinal(d3.quantize(d3.interpolateRainbow, ic_data.children.length + 1));

  // Layout
  const ic_hierarchy = d3.hierarchy(ic_data)
      .sum(d => d.value)
      .sort((a, b) => b.height - a.height || b.value - a.value);
  const ic_root = d3.partition()
      .size([ic_height, (ic_hierarchy.height + 1) * ic_width / 3])
    (ic_hierarchy);

  // Borra gráfico anterior (si existe)
  let icicleAnt = document.getElementById('icicle');
  if (icicleAnt != null) {
    icicleAnt.remove();
  }

  // SVG
  const ic_svg = d3.select('#graphIcicle').append('svg')
      .attr('id', 'icicle')
      .attr('viewBox', [0, 0, ic_width, ic_height])
      .attr('width', ic_width)
      .attr('height', ic_height)
      .attr('style', 'max-width: 100%; height: auto; font: 10px sans-serif;');

  // Celdas
  const ic_cell = ic_svg.selectAll('g')
    .data(ic_root.descendants())
    .join('g')
      .attr('transform', d => `translate(${d.y0},${d.x0})`);

  const ic_rect = ic_cell.append('rect')
      .attr('width', d => d.y1 - d.y0 - 1)
      .attr('height', d => rectHeight(d))
      .attr('fill-opacity', 0.6)
      .attr('fill', d => {
        if (!d.depth) return '#ccc';
        while (d.depth > 1) d = d.parent;
        return ic_color(d.data.name);
      })
      .style('cursor', 'pointer')
      .on('click', clicked);

  // Label
  const ic_text = ic_cell.append('text')
      .style('user-select', 'none')
      .attr('pointer-events', 'none')
      .attr('x', 4)
      .attr('y', 13)
      .attr('fill-opacity', d => +labelVisible(d));

  ic_text.append('tspan')
      .text(d => d.data.name);

  const ic_format = d3.format(',d');
  const ic_tspan = ic_text.append('tspan')
      .attr('fill-opacity', d => labelVisible(d) * 0.7)
      .text(d => ` ${ic_format(d.value)}`);

  ic_cell.append('title')
      .text(d => `${d.ancestors().map(d => d.data.name).reverse().join('/')}\n${ic_format(d.value)}`);

  // Cambiar el focus al clickar
  let focus = ic_root;
  function clicked(event, p) {
    focus = focus === p ? p = p.parent : p;

    ic_root.each(d => d.target = {
      x0: (d.x0 - p.x0) / (p.x1 - p.x0) * ic_height,
      x1: (d.x1 - p.x0) / (p.x1 - p.x0) * ic_height,
      y0: d.y0 - p.y0,
      y1: d.y1 - p.y0
    });

    const t = ic_cell.transition().duration(750)
        .attr('transform', d => `translate(${d.target.y0},${d.target.x0})`);

    ic_rect.transition(t).attr('height', d => rectHeight(d.target));
    ic_text.transition(t).attr('fill-opacity', d => +labelVisible(d.target));
    ic_tspan.transition(t).attr('fill-opacity', d => labelVisible(d.target) * 0.7);
  }
  
  // Altura de las celdas
  function rectHeight(d) {
    return d.x1 - d.x0 - Math.min(1, (d.x1 - d.x0) / 2);
  }

  // Determina si debe mostrarse la label
  function labelVisible(d) {
    return d.y1 <= width && d.y0 >= 0 && d.x1 - d.x0 > 16;
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

<!-- Collapsible Tree -->

```js
if( archivo[0].children === undefined ) {
  graphTreeDiv.innerHTML = "<div class=\"caution\">Los datos son incompatibles con este gráfico, por favor seleccione otro tipo de gráfico.</div>";
  graphInput[5].disabled = true;
} else{
  graphInput[5].disabled = false;
  graphTreeDiv.innerHTML = "";

  // Datos
  var tempArchivo = structuredClone(archivo);
  var ct_data = limitData(tempArchivo[0], limitSb);

  // Dimensiones
  const ct_width = 928;
  const ct_marginTop = 10;
  const ct_marginRight = 10;
  const ct_marginBottom = 10;
  const ct_marginLeft = 40;

  // Raíz (líneas separadas por dx y columnas por dy, como si la raíz estuviera abajo)
  const ct_root = d3.hierarchy(ct_data);
  const ct_dx = 10;
  const ct_dy = (ct_width - ct_marginRight - ct_marginLeft) / (1 + ct_root.height);

  // Layout
  const ct_tree = d3.tree().nodeSize([ct_dx, ct_dy]);
  const ct_diagonal = d3.linkHorizontal().x(d => d.y).y(d => d.x);

  // Borra gráfico anterior (si existe)
  let treeAnt = document.getElementById('tree');
  if (treeAnt != null) {
    treeAnt.remove();
  }

  // SVG
  const ct_svg = d3.select('#graphTree').append('svg')
      .attr('id', 'tree')
      .attr('width', ct_width)
      .attr('height', ct_dx)
      .attr('viewBox', [-ct_marginLeft, -ct_marginTop, ct_width, ct_dx])
      .attr('style', 'max-width: 100%; height: auto; font: 10px sans-serif; user-select: none;');

  const ct_gLink = ct_svg.append('g')
      .attr('fill', 'none')
      .attr('stroke', '#555')
      .attr('stroke-opacity', 0.4)
      .attr('stroke-width', 1.5);

  const ct_gNode = ct_svg.append('g')
      .attr('cursor', 'pointer')
      .attr('pointer-events', 'all');

  // Actualizar el árbol
  function update(event, source) {
    const duration = event?.altKey ? 2500 : 250; // Ralentiza transición
    const nodes = ct_root.descendants().reverse();
    const links = ct_root.links();

    // Layout
    ct_tree(ct_root);

    let left = ct_root;
    let right = ct_root;
    ct_root.eachBefore(node => {
      if (node.x < left.x) left = node;
      if (node.x > right.x) right = node;
    });

    const height = right.x - left.x + ct_marginTop + ct_marginBottom;

    const transition = ct_svg.transition()
        .duration(duration)
        .attr('height', height)
        .attr('viewBox', [-ct_marginLeft, left.x - ct_marginTop, ct_width, height])
        .tween('resize', window.ResizeObserver ? null : () => () => ct_svg.dispatch('toggle'));

    // Actualiza nodos
    const node = ct_gNode.selectAll('g')
      .data(nodes, d => d.id);

    // Nodos nuevos
    const nodeEnter = node.enter().append('g')
        .attr('transform', d => `translate(${source.y0},${source.x0})`)
        .attr('fill-opacity', 0)
        .attr('stroke-opacity', 0)
        .on('click', (event, d) => {
          d.children = d.children ? null : d._children;
          update(event, d);
        });

    nodeEnter.append('circle')
        .attr('r', 2.5)
        .attr('fill', d => d._children ? '#555' : '#999')
        .attr('stroke-width', 10);

    nodeEnter.append('text')
        .attr('dy', '0.31em')
        .attr('x', d => d._children ? -6 : 6)
        .attr('text-anchor', d => d._children ? 'end' : 'start')
        .text(d => d.data.name)
        .attr('stroke-linejoin', 'round')
        .attr('stroke-width', 3)
        .attr('stroke', 'white')
        .attr('paint-order', 'stroke');

    // Cambia nodos nuevos de posición
    const nodeUpdate = node.merge(nodeEnter).transition(transition)
        .attr('transform', d => `translate(${d.y},${d.x})`)
        .attr('fill-opacity', 1)
        .attr('stroke-opacity', 1);

    // Mueve nodos existentes a la posición del padre
    const nodeExit = node.exit().transition(transition).remove()
        .attr('transform', d => `translate(${source.y},${source.x})`)
        .attr('fill-opacity', 0)
        .attr('stroke-opacity', 0);

    // Actualiza enlaces
    const link = ct_gLink.selectAll('path')
      .data(links, d => d.target.id);

    // Añade los nuevos enlaces
    const linkEnter = link.enter().append('path')
        .attr('d', d => {
          const o = {x: source.x0, y: source.y0};
          return ct_diagonal({source: o, target: o});
        });

    // Posición de enlaces
    link.merge(linkEnter).transition(transition)
        .attr('d', ct_diagonal);

    // Posición de nodos
    link.exit().transition(transition).remove()
        .attr('d', d => {
          const o = {x: source.x, y: source.y};
          return ct_diagonal({source: o, target: o});
        });

    // Posiciones antiguas par transición
    ct_root.eachBefore(d => {
      d.x0 = d.x;
      d.y0 = d.y;
    });
  }

  // Configuración inicial
  ct_root.x0 = ct_dy / 2;
  ct_root.y0 = 0;
  ct_root.descendants().forEach((d, i) => {
    d.id = i;
    d._children = d.children;
    if (d.depth && d.data.name.length !== 4) d.children = null;
  });

  update(null, ct_root);

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