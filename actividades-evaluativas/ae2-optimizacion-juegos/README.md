# Actividad Evaluativa 2. Optimización y juegos

- **Semanas que abarca:** 3 y 4
- **Entrega:** semana 4 (25 de octubre de 2026), en la tarea del Equipo de Teams
- **Valor:** 25 % de la nota final
- **Modalidad:** individual
- **Tiempo estimado:** 10 a 12 horas

## Descripción

La actividad tiene dos partes. En la **parte A** comparas experimentalmente técnicas de búsqueda informada y de búsqueda local sobre dos problemas de rutas **generados para ti**: nadie más tiene tus mismas instancias. En la **parte B** construyes un agente que juega un juego de dos jugadores con minimax, poda alfa-beta y una función de evaluación diseñada por ti. Todo se documenta en un **informe técnico**.

## Resultados de aprendizaje que se evalúan

1. Aplica y compara búsqueda voraz, A\* y coste uniforme, y diseña heurísticas admisibles (capítulo 3, secciones 3.1 a 3.3).
2. Aplica y ajusta metaheurísticas a un problema de optimización, y compara sus resultados con rigor (capítulo 3, secciones 3.4 a 3.9).
3. Implementa un agente de juego con minimax y poda alfa-beta, y evalúa el efecto de la profundidad, la poda y la función de evaluación (capítulo 4).

---

## Tus instancias personales

Descarga [`recursos/ae2_instancias.py`](recursos/ae2_instancias.py) y súbelo a Colab junto a tu cuaderno (o déjalo en la misma carpeta si trabajas en tu computador). Tu **semilla** son los **últimos 6 dígitos de tu documento de identidad**:

```python
from ae2_instancias import mapa_rutas, consultas_rutas, instancia_tsp, dibujar_mapa

SEMILLA = 123456                       # ← los últimos 6 dígitos de TU documento
mapa = mapa_rutas(SEMILLA)             # 60 poblaciones unidas por vías (parte A.1)
consultas = consultas_rutas(SEMILLA)   # tres pares (origen, destino): cercano, medio y lejano
puntos = instancia_tsp(SEMILLA)        # 80 puntos; el 0 es el depósito (parte A.2)
dibujar_mapa(mapa)
```

Escribe tu semilla en la primera celda del cuaderno y en el informe. Un trabajo con instancias que no corresponden a tu semilla se califica sobre la mitad de la nota.

---

## Parte A. Búsqueda informada y metaheurísticas (45 %)

### A.1 Rutas con búsqueda informada

En el mapa de tu semilla, las vías tienen una longitud en kilómetros y cada población tiene coordenadas (*x*, *y*).

1. Implementa **coste uniforme, búsqueda voraz y A\***. Puedes partir de la función `primero_el_mejor` de la [práctica de la semana 3](../../semana-03-busqueda-informada/practicas/), indicando lo que reutilizaste.
2. Usa **al menos dos heurísticas** para A\*: la distancia euclídea y otra que propongas tú. Justifica en el informe si cada heurística es **admisible** y **consistente**. Puedes proponer también una heurística no admisible, si explicas qué ganas y qué pierdes con ella.
3. Resuelve las **tres consultas** de tu semilla con cada combinación de algoritmo y heurística, y registra: la ruta, su longitud, los nodos expandidos y el tiempo.
4. Dibuja en el mapa la ruta de A\* de la consulta lejana.

### A.2 Recorrido de reparto con metaheurísticas

Un vehículo sale del depósito (el punto 0), visita los 80 puntos de tu instancia y vuelve al depósito. Se busca el recorrido más corto con distancias euclídeas: es un viajante de comercio (TSP).

1. Construye una solución inicial con un **algoritmo constructivo voraz** (vecino más cercano u otro).
2. Implementa **al menos tres** de estas técnicas: *hill climbing* con reinicios aleatorios, temple simulado, búsqueda tabú y algoritmo genético.
3. Ejecuta cada técnica estocástica con **al menos 10 semillas** distintas y reporta el mejor resultado, la media, la desviación estándar y el tiempo promedio.
4. Presenta una **gráfica de convergencia** que compare las técnicas (longitud frente a iteraciones o tiempo).
5. Haz un **estudio de parámetros** de una de las técnicas: varía al menos un parámetro (temperatura inicial y enfriamiento, permanencia tabú, tamaño de la población o tasa de mutación) en al menos cuatro valores y muestra su efecto en una tabla o gráfica.
6. Dibuja el mejor recorrido que encontraste.

### A.3 Análisis

En el informe, responde con base en tus datos:

1. ¿Cuántos nodos ahorró A\* frente a coste uniforme en cada consulta? ¿Por qué el ahorro cambia de una consulta a otra?
2. ¿La búsqueda voraz encontró la ruta óptima en tus tres consultas? Si falló, explica por qué con la ruta concreta.
3. ¿Cuál de tus heurísticas fue mejor? Relaciónalo con la dominancia (sección 3.1.3).
4. ¿Qué técnica dio el mejor recorrido? ¿Y la mejor relación entre calidad y tiempo? ¿Coincide con lo que observaste en la práctica de la semana 3?
5. ¿Qué aprendiste del estudio de parámetros?

---

## Parte B. Agente de juego con minimax y poda alfa-beta (40 %)

### B.1 Elige un juego

Elige **uno** de estos juegos. No se aceptan el tres en raya ni el Conecta 4 clásico, porque ya están resueltos en la práctica.

| Juego | Reglas resumidas |
|---|---|
| **Reversi (Othello) en tablero de 6 × 6** | Cada jugada debe encerrar en línea recta fichas del rival, que cambian de color. Si un jugador no puede jugar, pasa. Gana quien tenga más fichas al final. |
| **Mancala (variante Kalah) con 4 semillas por hoyo** | Seis hoyos por jugador y un almacén. Se siembran las semillas una a una en sentido antihorario; si la última cae en tu almacén repites turno, y si cae en un hoyo propio vacío capturas las del hoyo de enfrente. |
| **Hex en tablero de 5 × 5 o 6 × 6** | Cada jugador intenta unir con una cadena de fichas sus dos lados opuestos del tablero rómbico. No hay empates. |
| **Puntos y cajas en una cuadrícula de 3 × 3 cajas** | Por turnos se traza un segmento entre dos puntos vecinos; quien cierra una caja la gana y repite turno. Gana quien cierre más cajas. |
| **Conecta 3 en un tablero de 5 × 4** | Como Conecta 4, pero gana quien alinee tres fichas en un tablero de 5 columnas por 4 filas. |
| **Juego propio** | Un juego de dos jugadores, determinista y de información perfecta. **Debe aprobarlo la docente** antes del miércoles de la semana 4, por el chat del curso en Teams. |

### B.2 Implementa el agente

1. Implementa las **reglas** del juego: estado, movimientos legales, resultado de un movimiento, test terminal y utilidad (tabla 4.2).
2. Implementa **minimax** (o negamax) y **minimax con poda alfa-beta**, con un **límite de profundidad**.
3. Diseña una **función de evaluación** con **al menos tres rasgos** del juego y justifica sus pesos.
4. Implementa una **ordenación de movimientos** para mejorar la poda.
5. Incluye un modo para que una persona juegue contra el agente (por consola, con `input()`, es suficiente).

### B.3 Experimenta

1. **Poda.** Para profundidades de 1 a la máxima que tu computador permita en menos de un minuto, mide los nodos visitados por minimax, por alfa-beta sin ordenación y por alfa-beta con ordenación. Comprueba que los tres devuelven el mismo valor.
2. **Torneos.** Enfrenta, en al menos **20 partidas** cada uno (alternando quién empieza):
   - tu agente contra un jugador aleatorio;
   - tu agente con profundidad *p* contra tu agente con profundidad *p* − 2;
   - tu agente con tu función de evaluación contra el mismo agente con una evaluación más simple (por ejemplo, solo la diferencia de fichas o de puntos), a la misma profundidad.

### B.4 Análisis

En el informe, responde:

1. ¿Qué porcentaje de nodos ahorró la poda a cada profundidad? ¿Cuánto ayudó la ordenación? Compara con lo que predice la sección 4.5.3.
2. ¿Qué rasgos de tu función de evaluación resultaron más importantes? ¿Cómo lo sabes?
3. ¿Observaste el efecto horizonte en alguna partida? Descríbelo.
4. ¿Qué cambiarías para que tu agente jugara mejor con el mismo tiempo de cómputo?

---

## Parte C. Informe técnico (15 %)

Redacta un informe técnico de **8 a 12 páginas** siguiendo la [plantilla de informe](../../recursos/plantillas/plantilla-informe.md), con estas secciones como mínimo: introducción, descripción de los problemas y del juego, métodos (algoritmos, heurísticas, función de evaluación y parámetros), resultados (tablas y gráficas numeradas), análisis (respuestas de A.3 y B.4), conclusiones, referencias en APA y declaración de uso de IA.

---

## Entregables

En tu repositorio de entregas, dentro de la carpeta `ae2/`:

| Archivo | Contenido |
|---|---|
| `README.md` | Tu nombre, tu semilla, el juego elegido y una lista de los archivos de la carpeta. |
| `ae2-rutas.ipynb` | El cuaderno de la parte A, **ejecutado**. |
| `ae2-juego.ipynb` (o archivos `.py`) | El código de la parte B, con instrucciones para jugar contra el agente. Si usas archivos `.py`, incluye un cuaderno ejecutado con los experimentos. |
| `ae2_instancias.py` | El generador de instancias, sin modificar. |
| `informe.pdf` | El informe técnico de la parte C. |

En la tarea de Teams entrega **el enlace a tu repositorio** y **el informe en PDF**. Revisa la [guía de entregas](../../guias/entregas-en-teams.md).

## Uso de herramientas de IA generativa

Puedes usar asistentes de IA para resolver dudas, depurar código o revisar la redacción, con dos condiciones:

1. Incluye al final del informe una sección **«Declaración de uso de IA»** que diga qué herramienta usaste, para qué y en qué partes. Si no usaste ninguna, decláralo también.
2. Debes poder explicar cualquier parte de tu código y de tu análisis. La docente puede pedirte que lo hagas en la sesión sincrónica.

Puedes reutilizar el código de las prácticas de las semanas 3 y 4, indicando qué tomaste y qué cambiaste. No se permite usar librerías que implementen los algoritmos de búsqueda o de juegos (por ejemplo, el solucionador de rutas de OR-Tools o `easyAI`): debes implementarlos tú.

## Evaluación

Ver la [rúbrica](rubrica.md).

## Preguntas frecuentes

**Mi documento termina en ceros (por ejemplo, 000123). ¿Qué semilla uso?** El número que forman esos seis dígitos: 123.

**¿Puedo usar más poblaciones o más puntos?** Sí, como experimento adicional, pero los resultados principales deben ser los de tus instancias con los valores por omisión.

**El algoritmo genético tarda mucho con 80 puntos.** Reduce la población o el número de generaciones, y explica en el informe el compromiso entre calidad y tiempo. Eso forma parte del análisis.

**Mi juego tiene empates y mi función de utilidad solo usa +1 y −1.** Añade el 0 para el empate. Si tu juego reparte puntos (como Mancala o Puntos y cajas), puedes usar la diferencia de puntos como utilidad.
