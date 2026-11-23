# Plan de estudio: Python para emprender

**Punto de partida:** ya manejas más o menos bucles y condicionales, y las funciones las tienes a un 6/10. No empezamos desde cero, pero sí afianzamos las bases antes de avanzar.

**Meta:** que al final puedas usar Python para tu emprendimiento: automatizar tareas, analizar tus ventas, generar reportes en Excel y publicar una aplicación web propia.

## Cómo usar este plan

- **Ritmo sugerido:** 3 sesiones por semana de 1,5 a 2 horas cada una. Son 32 sesiones, así que unas 11 semanas.
- **Cada sesión tiene un tema, lo que vas a aprender y una práctica.** La práctica no es opcional: ahí es donde realmente se aprende.
- **Guarda todo en este repo.** Crea una carpeta por sesión (`sesiones/01-diagnostico/`, `sesiones/02-git/`…) con tus archivos `.py` y haz commit al terminar.
- **Marca la casilla** `[x]` cuando termines una sesión.
- **Si una sesión te resulta fácil, avanza. Si te cuesta, repítela.**
- **Recursos gratis recomendados:** [documentación oficial de Python en español](https://docs.python.org/es/3/tutorial/), [Real Python](https://realpython.com/) (en inglés, muy claro) y [Exercism, track de Python](https://exercism.org/tracks/python) para practicar.

### Regla sobre la IA

Hasta el módulo 5 usa la IA como **profesor**, no como quien hace la tarea:

- ✅ "Explícame este error", "¿por qué mi función devuelve `None`?", "dame 3 ejercicios más de diccionarios"
- ❌ "Hazme el programa completo"

Si copias código que no entiendes, no estás aprendiendo. En el módulo 5 aprendes a trabajar con agentes como Claude Code, y ahí ya vas a poder revisar lo que escriben.

---

## Módulo 0: Diagnóstico y herramientas (2 sesiones)

- [ ] **Sesión 1: Diagnóstico + preparar tu computadora**
  - Instala Python 3.12 o más nuevo y VS Code con la extensión de Python. Aprende a correr un archivo desde la terminal: `python archivo.py`.
  - **Práctica, sin ayuda y midiendo el tiempo:**
    1. Una función `precio_final(precio, descuento=0, impuesto=0.18)` que devuelva el precio con el descuento y el impuesto aplicados.
    2. Con `ventas = [120, 45, 300, 80, 15]`, calcula el total, el promedio y cuántas ventas superan 100, **sin usar `sum()` ni `len()`**.
    3. Un bucle `while` que pida números hasta que escribas `fin` y al final muestre el mayor.
    4. Una función que reciba un texto y devuelva cuántas veces aparece cada palabra.
  - **Cómo leer el resultado:** si resuelves del 1 al 3 en menos de 15 minutos cada uno, haz las sesiones 3 y 4 rápido, como repaso. Si el 4 no te sale, no pasa nada: lo ves en la sesión 7.

- [ ] **Sesión 2: Git y GitHub**
  - Qué es el control de versiones y los comandos `clone`, `add`, `commit`, `push` y `status`.
  - **Práctica:** clona este repo, guarda tus ejercicios del diagnóstico en `sesiones/01-diagnostico/` y súbelos.

## Módulo 1: Afianzar las bases (6 sesiones)

- [ ] **Sesión 3: Bucles a fondo**
  - `for` con `range`, `enumerate` y `zip`; `while`; `break` y `continue`; bucles anidados.
  - **Práctica:** imprime una tabla de precios por cantidad (de 1 a 10 unidades de 3 productos) bien alineada.

- [ ] **Sesión 4: Funciones de 6 a 9/10**
  - Parámetros por defecto, argumentos con nombre, `*args` y `**kwargs`, devolver varios valores, alcance (`scope`) de las variables, docstrings y type hints básicos (`def f(x: int) -> float`).
  - La diferencia entre `print` y `return`, que es el error más común.
  - **Práctica:** las funciones `calcular_ganancia(costo, precio, unidades)`, `margen(costo, precio)` y `punto_de_equilibrio(costos_fijos, costo_unitario, precio)`, cada una con su docstring.

- [ ] **Sesión 5: Textos y f-strings**
  - Métodos de strings (`split`, `strip`, `lower`, `replace`, `startswith`), f-strings y formato de dinero: `f"{precio:,.2f}"`.
  - **Práctica:** genera un recibo de compra bien formateado en la consola.

- [ ] **Sesión 6: Listas y tuplas**
  - Slicing, ordenar, buscar y list comprehensions (`[p * 1.18 for p in precios]`).
  - **Práctica:** con una lista de precios, saca los 3 más caros, los que están bajo 50 y la lista con impuesto incluido, usando comprehensions.

- [ ] **Sesión 7: Diccionarios y sets**
  - Crear, leer y modificar; recorrer con `.items()`; `.get()`; diccionarios anidados; listas de diccionarios; sets para eliminar duplicados.
  - **Práctica:** un inventario como lista de diccionarios `{"nombre", "precio", "stock"}`. Busca productos, actualiza el stock y lista los que están por agotarse.

- [ ] **Sesión 8: 🎯 Mini proyecto 1, inventario en la consola**
  - Un programa con menú (`while` + `input`) para agregar, vender, buscar y listar productos, y ver el valor total del inventario. Todo organizado en funciones.

## Módulo 2: Python para trabajo real (8 sesiones)

- [ ] **Sesión 9: Manejo de errores**
  - Leer un traceback, `try`/`except`/`else`/`finally`, `raise` y validar lo que escribe el usuario.
  - **Práctica:** haz tu inventario a prueba de errores: que no se caiga si escribes letras donde va un número o vendes más de lo que hay.

- [ ] **Sesión 10: Archivos, CSV y JSON**
  - `open` con `with`, los módulos `csv` y `json`, y `pathlib`.
  - **Práctica:** que el inventario se guarde en un archivo JSON y no se pierda al cerrar el programa. Exporta las ventas a un CSV.

- [ ] **Sesión 11: Módulos y organización del código**
  - `import`, dividir el código en varios archivos, `if __name__ == "__main__":` y la librería estándar útil (`datetime`, `random`, `os`).
  - **Práctica:** separa el inventario en `modelos.py`, `almacenamiento.py` y `main.py`.

- [ ] **Sesión 12: Entornos virtuales y pip**
  - `python -m venv .venv`, `pip install`, `requirements.txt` y `.gitignore`.
  - **Práctica:** crea un entorno virtual para tus proyectos e instala tu primer paquete (`rich`, para que la consola se vea bonita).

- [ ] **Sesión 13: Programación orientada a objetos (1)**
  - Clases, `__init__`, atributos, métodos y `self`.
  - **Práctica:** las clases `Producto` y `Inventario`, con métodos `agregar`, `vender` y `valor_total`.

- [ ] **Sesión 14: Programación orientada a objetos (2)**
  - Herencia, `__str__`, `@dataclass` y cuándo vale la pena usar una clase (y cuándo no).
  - **Práctica:** una clase `Venta` que guarde fecha, productos y total, y la clase `ProductoPerecible` que herede de `Producto` y tenga fecha de vencimiento.

- [ ] **Sesión 15: Tests con pytest**
  - Por qué testear, cómo escribir y correr tests con `assert`, y casos borde.
  - **Práctica:** tests para `calcular_ganancia`, `vender` (incluido vender sin stock) y `valor_total`.

- [ ] **Sesión 16: 🎯 Mini proyecto 2, sistema de ventas**
  - Clases `Producto`, `Inventario` y `Venta`; guardado en JSON; un reporte del día (total vendido, producto estrella y stock bajo); y tests para la lógica principal.

## Módulo 3: Datos y automatización (6 sesiones)

> Aquí Python se vuelve un superpoder para emprender.

- [ ] **Sesión 17: pandas (1)**
  - `DataFrame`, leer CSV y Excel, ver columnas, filtrar y ordenar.
  - **Práctica:** carga un CSV de ventas (el tuyo o uno de ejemplo que generes) y responde preguntas: ¿cuál fue la venta más grande?, ¿qué pasó en marzo?

- [ ] **Sesión 18: pandas (2)**
  - `groupby`, totales por mes, producto o cliente, limpiar datos (vacíos, duplicados, formatos) y columnas calculadas.
  - **Práctica:** ventas por mes, top 5 de productos y ticket promedio por cliente.

- [ ] **Sesión 19: Gráficos con matplotlib**
  - Gráficos de líneas, barras y torta; títulos y etiquetas; guardarlos como imagen.
  - **Práctica:** un gráfico de las ventas por mes y otro de los productos más vendidos.

- [ ] **Sesión 20: Automatizar Excel**
  - `pandas.to_excel` y `openpyxl`: varias hojas, formato, anchos de columna y fórmulas.
  - **Práctica:** genera un Excel con una hoja de resumen y otra de detalle, listo para mandar.

- [ ] **Sesión 21: APIs con requests**
  - Qué es una API, el formato JSON, `requests.get` y las claves de API en un archivo `.env` (que **nunca** se sube a GitHub).
  - **Práctica:** consulta el tipo de cambio del dólar con una API pública y convierte tus precios.

- [ ] **Sesión 22: 🎯 Mini proyecto 3, reporte automático de ventas**
  - Un script que, con un CSV de ventas, genere automáticamente un Excel con el resumen y los gráficos. Una sola orden: `python reporte.py ventas.csv`.

## Módulo 4: Bases de datos y web (6 sesiones)

- [ ] **Sesión 23: SQL con SQLite**
  - Tablas, `CREATE`, `INSERT`, `SELECT`, `WHERE`, `UPDATE`, `DELETE` y un `JOIN` básico.
  - **Práctica:** diseña las tablas `productos`, `clientes` y `ventas`, y escribe consultas útiles.

- [ ] **Sesión 24: Python + base de datos**
  - El módulo `sqlite3`, consultas con parámetros (y por qué así se evita la inyección SQL).
  - **Práctica:** cambia el guardado de tu sistema de ventas de JSON a SQLite.

- [ ] **Sesión 25: Flask (1), tu primera web**
  - Rutas, plantillas Jinja y lo mínimo de HTML para mostrar datos.
  - **Práctica:** una página que muestre tu lista de productos sacada de la base de datos.

- [ ] **Sesión 26: Flask (2), formularios**
  - `GET` y `POST`, formularios, validación y redirecciones.
  - **Práctica:** páginas para agregar productos y registrar ventas desde el navegador.

- [ ] **Sesión 27: Seguridad básica**
  - Login simple con contraseñas hasheadas, sesiones, variables de entorno, validación en el servidor y qué nunca subir a GitHub.
  - **Práctica:** que solo tú puedas entrar al panel de ventas.

- [ ] **Sesión 28: Publicar en internet**
  - Deploy en Render o PythonAnywhere y variables de entorno en producción.
  - **Práctica:** que tu sistema de ventas tenga un link real que funcione desde tu celular.

## Módulo 5: Proyecto final (4 sesiones)

- [ ] **Sesión 29: Planificar el proyecto final (MVP)**
  - Elige un problema real de tu emprendimiento. Define lo mínimo que tiene que hacer, qué datos guarda y qué pantallas o reportes tiene.
  - **Práctica:** escribe `proyecto-final/PLAN.md` con la lista de funciones y las tablas de la base de datos.

- [ ] **Sesión 30: Programar con agentes de IA**
  - Cómo trabajar con Claude Code o Cursor: dar contexto claro, pedir cambios pequeños, revisar cada cambio y usar tus tests como red de seguridad.
  - **Práctica:** construye la primera parte del proyecto con ayuda de la IA y revisa cada cambio antes de aceptarlo.

- [ ] **Sesión 31: Construir y publicar**
  - Completar las funciones principales, escribir tests y hacer el deploy.
  - **Práctica:** que el proyecto final esté funcionando en internet.

- [ ] **Sesión 32: Retrospectiva y próximos pasos**
  - Qué aprendiste, qué te costó y qué mejorarías.
  - Posibles caminos: **FastAPI** (APIs modernas), **Django** (webs grandes), **bots de Telegram o WhatsApp** para atender clientes, **análisis de datos** más avanzado o **apps con IA** usando la API de Claude.
  - **Práctica:** escribe un buen README para tu proyecto final. Es tu portafolio.

---

## Registro de progreso

| Semana | Sesiones hechas | Lo que más me costó | Nota para mí |
|--------|-----------------|---------------------|--------------|
| 1      |                 |                     |              |
| 2      |                 |                     |              |
| 3      |                 |                     |              |
