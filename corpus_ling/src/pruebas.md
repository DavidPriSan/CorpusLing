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

<!-- Apariciones de cada palabra -->

```js
vl.markBar()
  .data(pruebas)
  .params(
    {name: "Filtro", bind: {input: "text"}}
  )
  .transform(
    vl.filter("datum.word == Filtro")
  )
  .width(800)
  .autosize({type: "pad", resize: "true", contains: "padding"})
  .encode(
    vl.y().fieldN('word').title('Palabra'),
    vl.x().fieldN('word').count().title('Apariciones')
  )
  .render()
```