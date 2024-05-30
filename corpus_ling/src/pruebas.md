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

<!-- Apariciones de cada palabra -->

```js
vl.markBar()
  .data(pruebas)
  .params(
    {name: "Filtro", bind: {input: "text"}}
  )
  .transform(
    vl.filter("slice(datum.word, 0, 2) == Filtro")
  )
  .width(800)
  .encode(
    vl.y().fieldN('word').title('Palabra'),
    vl.x().fieldN('word').count().title('Apariciones')
  )
  .render()
```