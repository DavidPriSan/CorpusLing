---
theme: dashboard
title: Pruebas
toc: false
---

# Pruebas

<!-- Carga de datos -->

```js
const bigramas = FileAttachment("./data/bigramas.json").json();
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

<div class="card" style="display: flex; flex-direction: column; gap: 1rem;">
  ${palabraInput}
</div>

<!-- Apariciones de bigramas -->

<div class="card" style="display: flex; flex-direction: column; gap: 1rem;"><h1>Bigramas</h1>
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

<!-- Apariciones por país -->

<div class="card" style="display: flex; flex-direction: column; gap: 1rem;"><h1>Países</h1>
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