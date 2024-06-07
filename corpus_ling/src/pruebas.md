---
theme: dashboard
title: Pruebas
toc: false
---

# Pruebas

<!-- Carga de datos -->

```js
const pruebas = FileAttachment("./data/pruebas.json").json();
const bigramas = FileAttachment("./data/bigramas.json").json();
```

<!-- Json -->

```js
display(pruebas);
display(bigramas);
```

<!-- Filtro -->

```js
const palabraInput = Inputs.text({label: "Palabra a buscar"});
const palabra = Generators.input(palabraInput);
```

<!-- Apariciones de cada palabra -->

<div class="card" style="display: flex; flex-direction: column; gap: 1rem;">
  ${palabraInput}
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
