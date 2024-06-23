---
theme: dashboard
title: Pruebas
toc: false
---

# Pruebas

<!-- Carga de datos -->

```js
const bigramas = FileAttachment("./data/bigramas.json").json();
const paises = ['España', 'México', 'Colombia', 'Argentina', 'Perú', 'Venezuela', 'Chile', 'Guatemala', 'Ecuador', 'Bolivia', 'Cuba'];
```


<!-- Json -->

```js
display(bigramas);
```


<!-- Filtro -->

```js
const palabraInput = Inputs.text({label: "Palabra a buscar"});
const palabra = Generators.input(palabraInput);
```

<div class="card">
  ${palabraInput}
</div>


<!-- Bigramas totales -->

<div class="card"><h1>Bigramas</h1>
  ${resize((width) => Plot.plot({
    width,
    marginBottom: 80,
    y: {grid: true, label: "Apariciones"},
    x: {label: null, tickRotate: -30},
    marks: [
      Plot.barY(bigramas.filter((d) => d.word === palabra),
        Plot.groupX(
          {
            y: "count"
          },
          {
            x: "bigram",
            sort: { x: "y", reverse: true, limit: 20 },
            fill: "steelblue"
          }
        )
      ),
      Plot.ruleY([0])
    ]
  }))}
</div>


<!-- Heatmap por país -->

<div class="card"><h1>Países</h1>
  ${resize((width) => Plot.plot({
    width,
    marginLeft: 120,
    y: {label: "País"},
    x: {label: "Año"},
    color: {legend: true, zero: true, label: "Apariciones"},
    marks: [
      Plot.cell(bigramas.filter((d) => d.word === palabra),
        Plot.group(
          {fill: "count"},
          {x: "year", y: "country", inset: 0.5}
        )
      )
    ]
  }))}
</div>


<!-- Selector país -->

```js
const paisInput = Inputs.select([null].concat(paises), {label: "País"});
const pais = Generators.input(paisInput);
```

<div class="card">
  ${paisInput}
</div>


<!-- Estadísticas del país -->

<div class="grid grid-cols-2">
  <div class="card">
    <h1>Bigramas</h1>
    ${resize((width) => Plot.plot({
      width,
      marginBottom: 80,
      y: {grid: true, label: "Apariciones"},
      x: {label: null, tickRotate: -30},
      marks: [
        Plot.barY(bigramas.filter((d) => d.word === palabra && d.country === pais),
          Plot.groupX(
            {
              y: "count"
            },
            {
              x: "bigram",
              sort: { x: "y", reverse: true, limit: 10 },
              fill: "steelblue"
            }
          )
        ),
        Plot.ruleY([0])
      ]
    }))}
  </div>
  <div class="card">
    <h1>Evolución en el tiempo</h1>
    ${resize((width) => Plot.plot({
      width,
      marginBottom: 80,
      y: {grid: true, label: "Apariciones"},
      x: {label: "Año"},
      marks: [
        Plot.areaY(bigramas.filter((d) => d.word === palabra && d.country === pais),
          Plot.binX(
            {
              y: "count"
            },
            {
              x: "year",
              sort: { x: "y", reverse: true, limit: 10 },
              fillOpacity: 0.2
            }
          )
        ),
        Plot.lineY(bigramas.filter((d) => d.word === palabra && d.country === pais),
          Plot.binX(
            {
              y: "count"
            },
            {
              x: "year",
              sort: { x: "y", reverse: true, limit: 10 }
            }
          )
        ),
        Plot.ruleY([0])
      ]
    }))}
  </div>
</div>