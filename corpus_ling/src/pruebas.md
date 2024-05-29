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

<!-- Apariciones de cada palabra -->

```js
display(pruebas);
```

```js
vl.markBar()
  .params(
    vl.param('Apariciones').value(100).bind(vl.slider(0,5000,50))
  )
  .data(pruebas)
  .transform(
    vl.filter('datum.word.count() < Apariciones')
  )
  .width(600)
  .height(32000)
  .encode(
    vl.y().fieldN("word"),
    vl.x().count()
  )
  .render()
```