---
theme: dashboard
title: Pruebas
toc: false
---

# Pruebas

<!-- Carga de datos -->

```js
const freq = FileAttachment("./data/wordFrequency.tsv").tsv();
const coll = FileAttachment("./data/collocates.tsv").tsv();
const numbers = FileAttachment("./data/numbers.tsv").tsv();
```


<!-- CSV -->

```js
display(freq);
display(coll);
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

<div class="card"><h1>Texto</h1>
  ${resize((width) => Plot.plot({
    width,
    marginLeft: 50,
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