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