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
function eachWord(data, {width}) {
  vl.markBar().data(data).encode(
    vl.x().fieldQ("word"),
    vl.y().fieldN("count")
  )
}
```

<div class="grid grid-cols-1">
  <div class="card">
    ${resize((width) => eachWord(pruebas, {width}))}
  </div>
</div>
