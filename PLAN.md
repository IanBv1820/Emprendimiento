# Plan de estudio: aprender a programar desde cero

**Meta:** que al final puedas construir y publicar una aplicación web simple para un emprendimiento, por ejemplo una tienda, un sistema de pedidos o una página con reservas.

**Ruta:** web (HTML, CSS, JavaScript y después Node.js). Elegí esta ruta porque ves resultados en el navegador desde el primer día, y con un solo lenguaje (JavaScript) cubres el frontend y el backend.

## Cómo usar este plan

- **Ritmo sugerido:** 3 sesiones por semana de 1,5 a 2 horas cada una. Son 36 sesiones, así que unas 12 semanas.
- **Cada sesión tiene un tema, lo que vas a aprender y una práctica.** La práctica no es opcional: ahí es donde realmente se aprende.
- **Guarda todo en este repo.** Crea una carpeta por sesión (`sesiones/01-...`, `sesiones/02-...`) y haz commit al terminar.
- **Marca la casilla** `[x]` cuando termines una sesión.
- **Si una sesión te cuesta, repítela.** Es mejor ir lento y entender que avanzar sin entender.
- **Recursos gratis recomendados:** [MDN Web Docs](https://developer.mozilla.org/es/) (la referencia oficial, en español), [javascript.info](https://es.javascript.info/) y [freeCodeCamp](https://www.freecodecamp.org/espanol/).

### Regla sobre la IA

Hasta el módulo 5 usa la IA como **profesor**, no como quien hace la tarea:

- ✅ "Explícame qué hace este error", "¿por qué mi bucle no termina?", "dame un ejercicio extra sobre arrays"
- ❌ "Hazme la página completa"

Si copias código que no entiendes, no estás aprendiendo. En el módulo 5 aprendes a usar agentes como Claude Code para trabajar más rápido, y ahí ya vas a poder revisar lo que escriben.

---

## Módulo 0: Preparación (2 sesiones)

- [ ] **Sesión 1: Qué es programar y cómo funciona la web**
  - Aprendes qué es un programa, qué pasa cuando abres una página (navegador → servidor → respuesta) y la diferencia entre frontend y backend.
  - Instala VS Code y Node.js, y aprende comandos básicos de la terminal (`cd`, `ls`, `mkdir`).
  - **Práctica:** crea una carpeta desde la terminal y ábrela en VS Code.

- [ ] **Sesión 2: Git y GitHub**
  - Aprendes qué es el control de versiones y los comandos `clone`, `add`, `commit`, `push` y `status`.
  - **Práctica:** clona este repo en tu computadora, crea `sesiones/01-intro/notas.md` con lo que aprendiste y súbelo con un commit.

## Módulo 1: HTML y CSS, la cara de la web (7 sesiones)

- [ ] **Sesión 3: Estructura HTML**
  - Etiquetas, `<head>` y `<body>`, títulos, párrafos y comentarios.
  - **Práctica:** una página "Sobre mí" con tu nombre y 3 párrafos.

- [ ] **Sesión 4: Enlaces, imágenes y listas**
  - `<a>`, `<img>`, `<ul>`, `<ol>`, rutas relativas y absolutas.
  - **Práctica:** agrega una foto, una lista de tus metas y enlaces a tus redes.

- [ ] **Sesión 5: Formularios**
  - `<form>`, `<input>`, `<select>`, `<textarea>`, `<button>` y la importancia de los `<label>`.
  - **Práctica:** un formulario de contacto para un negocio (nombre, correo, mensaje).

- [ ] **Sesión 6: CSS básico**
  - Selectores, colores, fuentes, tamaños y cómo conectar un `.css`.
  - **Práctica:** dale estilo a tu página "Sobre mí".

- [ ] **Sesión 7: El modelo de caja**
  - `margin`, `padding`, `border`, `width` y `box-sizing`, y cómo usar las DevTools del navegador para inspeccionar.
  - **Práctica:** arma tarjetas de producto (imagen, nombre, precio).

- [ ] **Sesión 8: Flexbox**
  - Alinear y distribuir elementos en filas y columnas.
  - **Práctica:** un menú de navegación y una fila de 3 tarjetas de producto.

- [ ] **Sesión 9: Diseño responsive + 🎯 Mini proyecto 1**
  - Media queries y cómo diseñar primero para celular.
  - **Práctica:** la **landing page de tu emprendimiento** (o uno inventado) con encabezado, productos/servicios, formulario de contacto y pie de página. Que se vea bien en el celular.

## Módulo 2: Fundamentos de JavaScript, la lógica (10 sesiones)

- [ ] **Sesión 10: Variables y tipos de datos**
  - `let`, `const`, números, textos, booleanos y `console.log`.
  - **Práctica:** guarda en variables el nombre, precio y stock de un producto e imprímelos.

- [ ] **Sesión 11: Operadores y condicionales**
  - Aritmética, comparaciones, `&&` y `||`, `if`/`else` y `switch`.
  - **Práctica:** si la compra supera 100, aplica 10% de descuento; si no hay stock, muestra "Agotado".

- [ ] **Sesión 12: Bucles**
  - `for` y `while`, y cómo evitar bucles infinitos.
  - **Práctica:** imprime una tabla de precios del 1 al 10 unidades.

- [ ] **Sesión 13: Funciones**
  - Parámetros, `return`, funciones flecha y por qué conviene dividir el problema en partes.
  - **Práctica:** las funciones `calcularIVA(precio)`, `aplicarDescuento(precio, porcentaje)` y `calcularTotal(...)`.

- [ ] **Sesión 14: Arrays**
  - Crear, leer, agregar y quitar elementos, y recorrerlos.
  - **Práctica:** un carrito de compras como array: agrega productos, quita uno y muestra el total.

- [ ] **Sesión 15: Objetos**
  - Propiedades y métodos, y arrays de objetos.
  - **Práctica:** un inventario como array de objetos `{ nombre, precio, stock }`.

- [ ] **Sesión 16: Métodos de arrays**
  - `map`, `filter`, `find`, `reduce` y `sort`.
  - **Práctica:** del inventario saca los productos con poco stock, el valor total y los productos ordenados por precio.

- [ ] **Sesión 17: Errores y depuración**
  - Leer mensajes de error, usar `console` y el debugger de las DevTools, y `try`/`catch`.
  - **Práctica:** te paso (o le pides a la IA) código con 5 errores y los encuentras tú.

- [ ] **Sesión 18: Repaso y ejercicios de lógica**
  - Resuelve 5 a 8 ejercicios cortos sin ayuda, en freeCodeCamp o en tu propia lista.
  - **Práctica:** anota cuáles te costaron y repasa esos temas.

- [ ] **Sesión 19: 🎯 Mini proyecto 2, calculadora de negocio**
  - Un programa en la consola que, con costo, precio de venta y unidades vendidas, calcule la ganancia, el margen y el punto de equilibrio.

## Módulo 3: JavaScript en el navegador, páginas interactivas (6 sesiones)

- [ ] **Sesión 20: El DOM**
  - `querySelector`, cambiar texto, estilos y clases, y crear elementos desde JS.
  - **Práctica:** dibuja las tarjetas de productos desde el array del inventario en lugar de escribirlas en HTML.

- [ ] **Sesión 21: Eventos**
  - `addEventListener`, `click`, `input` y `submit`.
  - **Práctica:** un botón "Agregar al carrito" que actualice un contador.

- [ ] **Sesión 22: Formularios y validación**
  - Leer valores, validar campos, mostrar errores y `preventDefault`.
  - **Práctica:** valida el formulario de contacto de tu landing page.

- [ ] **Sesión 23: Guardar datos en el navegador**
  - `localStorage` y `JSON.stringify`/`JSON.parse`.
  - **Práctica:** que el carrito no se borre al recargar la página.

- [ ] **Sesión 24: APIs, `fetch` y `async`/`await`**
  - Qué es una API, el formato JSON y cómo pedir datos de internet.
  - **Práctica:** muestra el tipo de cambio del dólar (o el clima) usando una API pública.

- [ ] **Sesión 25: 🎯 Mini proyecto 3, gestor de pedidos**
  - Una app donde registras pedidos (cliente, producto, cantidad, estado), los filtras por estado y se guardan en `localStorage`.

## Módulo 4: Backend y bases de datos (6 sesiones)

- [ ] **Sesión 26: Node.js y npm**
  - JavaScript fuera del navegador, `package.json` e instalar paquetes.
  - **Práctica:** corre tu calculadora de negocio (sesión 19) con Node.

- [ ] **Sesión 27: Tu primer servidor con Express**
  - Rutas, peticiones y respuestas, y los métodos `GET` y `POST`.
  - **Práctica:** un servidor que responda `/productos` con tu inventario en JSON.

- [ ] **Sesión 28: API REST**
  - CRUD (crear, leer, actualizar, borrar) y los códigos HTTP 200, 201, 400 y 404.
  - **Práctica:** una API completa de productos y pruébala con Thunder Client o Postman.

- [ ] **Sesión 29: Bases de datos y SQL**
  - Tablas, `SELECT`, `INSERT`, `UPDATE`, `DELETE` y `WHERE`, usando SQLite.
  - **Práctica:** guarda los productos en una base de datos en lugar de un array.

- [ ] **Sesión 30: Conectar frontend con backend**
  - Que tu página use `fetch` contra tu propia API, y qué es CORS.
  - **Práctica:** que el gestor de pedidos guarde los datos en el servidor en lugar de `localStorage`.

- [ ] **Sesión 31: Seguridad básica**
  - Variables de entorno (`.env`), por qué nunca se suben contraseñas a GitHub, validar datos en el servidor y `.gitignore`.
  - **Práctica:** revisa tu proyecto y corrige lo que haga falta.

## Módulo 5: Proyecto final y publicación (5 sesiones)

- [ ] **Sesión 32: Planificar el proyecto final (MVP)**
  - Elige una idea real de tu emprendimiento y define lo mínimo que debe hacer, las pantallas y los datos que guarda.
  - **Práctica:** escribe `proyecto-final/PLAN.md` con la lista de funciones y un boceto en papel.

- [ ] **Sesión 33: Usar IA para programar bien**
  - Cómo trabajar con agentes como Claude Code o Cursor: dar contexto claro, pedir cambios pequeños, revisar lo que hacen y escribir tests.
  - **Práctica:** construye la primera parte del proyecto final con ayuda de la IA y revisa cada cambio antes de aceptarlo.

- [ ] **Sesión 34: Construir el proyecto (parte 2)**
  - Completar las funciones principales.
  - **Práctica:** que el flujo principal funcione de principio a fin.

- [ ] **Sesión 35: Publicar en internet**
  - Deploy del frontend en GitHub Pages o Netlify y del backend en Render o Railway, con variables de entorno en producción.
  - **Práctica:** que tu proyecto tenga un link que puedas mandarle a alguien.

- [ ] **Sesión 36: Retrospectiva y próximos pasos**
  - Qué aprendiste, qué te costó y qué mejorarías del proyecto.
  - Posibles caminos: React (interfaces más grandes), TypeScript, Python (datos y automatización) o pagos en línea (Stripe o Mercado Pago).
  - **Práctica:** escribe un README bonito para tu proyecto final. Es tu portafolio.

---

## Registro de progreso

| Semana | Sesiones hechas | Lo que más me costó | Nota para mí |
|--------|-----------------|---------------------|--------------|
| 1      |                 |                     |              |
| 2      |                 |                     |              |
| 3      |                 |                     |              |
