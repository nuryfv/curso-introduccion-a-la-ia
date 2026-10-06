# Actividad Evaluativa 1. Línea de tiempo de la IA y modelado de un problema de búsqueda

- **Semanas que abarca:** 1 y 2
- **Entrega:** semana 2 (11 de octubre de 2026), en la tarea del Equipo de Teams
- **Valor:** 25 % de la nota final
- **Modalidad:** individual
- **Tiempo estimado:** 6 a 8 horas

## Descripción

La actividad tiene dos partes que corresponden a las dos primeras semanas del curso. En la **parte A** construyes una línea de tiempo comentada de la IA, apoyada en fuentes verificables, que te obliga a ir más allá de la tabla 1.3.9 del capítulo 1. En la **parte B** eliges un problema, lo formulas como un problema de búsqueda en un espacio de estados y comparas experimentalmente cuatro algoritmos de búsqueda no informada.

## Resultados de aprendizaje que se evalúan

1. Reconstruye los hitos principales de la historia de la IA y los relaciona con los enfoques y técnicas del curso (capítulo 1).
2. Formula un problema con sus cuatro componentes y describe su espacio de estados (capítulo 2, secciones 2.1 a 2.4).
3. Implementa y compara BFS, DFS, profundidad iterativa y coste uniforme según su completitud, optimalidad y complejidad (capítulo 2, secciones 2.5 a 2.8).

---

## Parte A. Línea de tiempo comentada de la IA (30 %)

### A.1 Construye la línea de tiempo

Elabora una línea de tiempo con **al menos 15 hitos** entre 1943 y 2026 que cumpla estas condiciones:

- Al menos **5 hitos que no aparezcan** en la tabla de la sección 1.3.9 del capítulo 1. Algunas ideas: ELIZA, Shakey, MYCIN, el Informe Lighthill, el sistema DENDRAL, TD-Gammon, el coche autónomo de la DARPA Grand Challenge, Siri, AlphaFold, Stable Diffusion, el Reglamento europeo de IA o un hito de la IA en Colombia o en América Latina.
- Al menos **2 hitos de 2023 en adelante**.
- Que se vean los **periodos de entusiasmo y los «inviernos»** de la IA (sección 1.3).

Para cada hito registra:

| Campo | Descripción |
|---|---|
| Año | Año del hito (o rango de años). |
| Hito | Qué ocurrió, en una o dos líneas. |
| Enfoque o técnica | Simbólico (lógica, reglas, búsqueda), conexionista (redes neuronales), probabilístico, aprendizaje por refuerzo, etc. |
| Semana del curso | La semana del curso en la que se estudia la técnica relacionada (1 a 8). |
| Fuente | Una referencia verificable en formato APA: el artículo original, la página institucional o un libro. **No se aceptan como única fuente Wikipedia, blogs anónimos ni respuestas de un chatbot.** |

El formato es libre: una tabla en Markdown, un diagrama `timeline` de Mermaid, una herramienta en línea como Canva o TimelineJS, o un PDF. Si usas una herramienta externa, incluye en el repositorio una exportación en PDF o PNG, además del enlace.

### A.2 Análisis (500 a 800 palabras)

Responde en prosa, citando tus fuentes:

1. **Ciclos.** Identifica en tu línea de tiempo al menos dos periodos de gran entusiasmo y uno de desencanto. ¿Qué promesas no se cumplieron y por qué? ¿Ves señales de un ciclo parecido hoy?
2. **Enfoques.** ¿Cómo ha cambiado el peso de los enfoques simbólico y conexionista a lo largo del tiempo? Apóyate en al menos tres hitos concretos.
3. **De un hito a hoy.** Elige un hito anterior al año 2000 y explica cómo sus ideas siguen presentes en algún sistema que uses hoy, describiéndolo como un agente con el esquema REAS (sección 1.6.3).

---

## Parte B. Modelado y búsqueda no informada (70 %)

### B.1 Elige un problema

Elige **uno** de estos problemas o propón uno propio:

| Problema | Descripción breve |
|---|---|
| **8-puzle** | Tablero 3 × 3 con 8 fichas y un hueco; se deslizan fichas hasta llegar a una configuración objetivo (Russell y Norvig, 2004, cap. 3). |
| **Jarras de agua** | Dos o tres jarras de capacidades distintas; llenar, vaciar o trasvasar hasta obtener una cantidad exacta. Asigna costos distintos a las acciones (por ejemplo, litros de agua usados). |
| **Misioneros y caníbales** | Tres misioneros y tres caníbales cruzan un río en una barca de dos plazas sin que los caníbales superen nunca a los misioneros en una orilla (Russell y Norvig, 2004, cap. 3). |
| **Laberinto en cuadrícula** | Una cuadrícula de al menos 10 × 10 con obstáculos y casillas de distinto costo (por ejemplo, barro = 3, camino = 1). |
| **Rutas en tu región** | Un grafo de al menos 12 municipios o lugares de tu región unidos por vías, con su distancia o tiempo de viaje. Indica de dónde obtuviste los datos. |
| **Problema propio** | Cualquier otro problema con estados discretos y acciones bien definidas. **Debe aprobarlo la docente** antes del miércoles de la semana 2, por el chat del curso en Teams. |

Condición: el problema debe permitir comparar **BFS y coste uniforme con resultados distintos**. Si todas las acciones de tu problema cuestan lo mismo, añade una variante con costos diferentes y justifícala.

### B.2 Modela el problema

En el informe, incluye:

1. **El agente:** descríbelo con el esquema REAS y clasifica su entorno según las propiedades de la sección 1.6.4.
2. **Modelo, objetivo y función de evaluación** (sección 2.1.2).
3. **Formulación** con los cuatro componentes (sección 2.3.1), escrita de manera que otra persona pueda implementarla: cómo se representa un estado, cuál es el estado inicial, qué acciones hay y cuándo es aplicable cada una, cuál es el test objetivo y cómo se calcula el costo.
4. **Abstracción:** qué detalles del problema real dejaste fuera y por qué tu modelo sigue siendo válido (sección 2.3.2).
5. **Tamaño del espacio de estados:** una estimación justificada del número de estados y del factor de ramificación.
6. **Diagrama** de al menos dos niveles del árbol o grafo de estados a partir del estado inicial, señalando los estados repetidos. Puede ser un diagrama de Mermaid, una imagen o una foto legible de un dibujo a mano.

### B.3 Implementa y compara

En un cuaderno de Jupyter (`.ipynb`):

1. Implementa tu problema en Python y los cuatro algoritmos: **BFS, DFS, profundidad iterativa y coste uniforme**. Puedes partir del código de la [práctica de la semana 2](../../semana-02-busqueda-no-informada/practicas/), indicando qué tomaste y qué cambiaste. Hay un cuaderno base con la estructura sugerida en [`recursos/`](recursos/).
2. Ejecuta los cuatro algoritmos sobre **al menos tres instancias** de dificultad creciente (fácil, media y difícil).
3. Para cada ejecución, mide: si encontró solución, la longitud de la solución (número de acciones), su costo, los **nodos expandidos**, el **tamaño máximo de la frontera** y el tiempo de ejecución.
4. Presenta los resultados en una tabla y en al menos una gráfica.

### B.4 Analiza los resultados

En el informe, responde con base en tus datos y en el capítulo 2:

1. ¿Qué algoritmo encontró la solución óptima en cada instancia? ¿Coincide con lo que predice la tabla 2.12?
2. ¿Cómo crecieron los nodos expandidos y el tamaño de la frontera al aumentar la dificultad? Relaciónalo con *b*, *d* y *m*.
3. ¿En qué instancia BFS y coste uniforme dieron soluciones distintas? Explica por qué.
4. ¿Hubo alguna instancia en la que un algoritmo no terminara en un tiempo razonable o se quedara sin memoria? ¿Qué harías para resolverla? (Puedes anticipar ideas de la semana 3.)
5. Si tuvieras que resolver tu problema en un producto de software real, ¿qué algoritmo elegirías y por qué?

---

## Entregables

En tu repositorio de entregas (ver la [plantilla](../../recursos/plantillas/repositorio-estudiante/)), dentro de la carpeta `ae1/`:

| Archivo | Contenido |
|---|---|
| `README.md` | Tu nombre, el problema elegido y una lista de los archivos de la carpeta. |
| `linea-de-tiempo.md` (o `.pdf` / `.png`) | La línea de tiempo de la parte A.1. |
| `ae1-busqueda.ipynb` | El cuaderno con el código de la parte B **ejecutado**: las salidas deben verse sin tener que volver a ejecutarlo. |
| `informe.md` o `informe.pdf` | El informe con el análisis de la parte A.2 y las secciones B.2 y B.4, según la [plantilla de informe](../../recursos/plantillas/plantilla-informe.md). Extensión máxima: 8 páginas, sin contar la línea de tiempo. |

En la tarea de Teams entrega **el enlace a tu repositorio** y **el informe en PDF**. Revisa la [guía de entregas](../../guias/entregas-en-teams.md).

## Uso de herramientas de IA generativa

Puedes usar asistentes de IA para resolver dudas, depurar código o revisar la redacción, con dos condiciones:

1. Incluye al final del informe una sección **«Declaración de uso de IA»** que diga qué herramienta usaste, para qué y en qué partes. Si no usaste ninguna, decláralo también.
2. Debes poder explicar cualquier parte de tu código y de tu análisis. La docente puede pedirte que lo hagas en la sesión sincrónica.

Las fuentes de la línea de tiempo deben ser verificables: un hito con una referencia inventada o que no dice lo que se le atribuye se califica como si no tuviera fuente.

## Evaluación

Ver la [rúbrica](rubrica.md).

## Preguntas frecuentes

**¿Puedo usar el 8-puzle aunque está en el libro?** Sí. Lo que se evalúa es tu formulación, tus experimentos y tu análisis.

**¿Puedo usar librerías como `networkx` o `aima-python` para los algoritmos?** Para representar el grafo, sí. Los cuatro algoritmos de búsqueda debes implementarlos tú (puedes adaptar los de la práctica de la semana 2).

**DFS no termina en mi instancia difícil. ¿Está mal?** No necesariamente. Pon un límite de tiempo o de nodos expandidos, registra que no terminó y explica por qué en el análisis: ese es un resultado valioso.
