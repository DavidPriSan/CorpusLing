---
theme: dashboard
title: Pruebas
toc: false
---

# Pruebas

<!-- Carga de datos -->

```js
const pruebas = FileAttachment("./data/pruebas.json").json();
```

<!-- Json -->

```js
display(pruebas);
```

<!-- Filtro del usuario -->

<input id="filtro" type="text"/>

<!-- Apariciones de cada palabra -->

```js
const input = document.getElementById("filtro");

vl.markBar()
  .data(pruebas)
  .params(
    vl.param('f').bind(input.value)
  )
  .transform(
    vl.filter("slice(datum.word, 0, 2) == f")
  )
  .width(600)
  .encode(
    vl.y().fieldN('word').title('Palabra'),
    vl.x().fieldN('word').count().title('Apariciones')
  )
  .render()
```