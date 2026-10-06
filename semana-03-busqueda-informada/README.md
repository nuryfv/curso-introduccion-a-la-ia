# Semana 3. Búsqueda informada, búsqueda local y metaheurísticas

Esta semana le das a la búsqueda **información sobre el problema**. Primero estudias las heurísticas y el algoritmo A\*, que encuentran el camino óptimo explorando mucho menos que las búsquedas ciegas de la semana 2. Después cambias de enfoque: cuando el espacio es tan grande que ni A\* sirve y lo que importa es la configuración final, partes de una solución completa y la mejoras poco a poco con búsqueda local y metaheurísticas inspiradas en la física y en la evolución.

## Objetivos de aprendizaje

1. Explicar qué es una función heurística y comprobar si es admisible y consistente.
2. Aplicar la búsqueda con vuelta atrás a problemas con restricciones.
3. Aplicar la búsqueda voraz y el algoritmo A\*, y explicar por qué A\* es óptimo con una heurística admisible.
4. Describir algoritmos constructivos voraces como el de Dijkstra y el de ahorros de Clarke y Wright.
5. Aplicar *hill climbing*, temple simulado, búsqueda tabú y algoritmos genéticos a un problema de optimización.
6. Elegir una técnica según el tipo de problema, la calidad de solución requerida y los recursos disponibles.

## Temas de la semana

- Funciones heurísticas
- Búsqueda con vuelta atrás (*backtracking*)
- Búsqueda voraz primero el mejor y algoritmo A\*
- Algoritmos constructivos voraces (Dijkstra, Clarke y Wright)
- *Hill climbing*
- Temple simulado (*simulated annealing*)
- Búsqueda tabú
- Algoritmos genéticos

## Ruta de estudio

| Paso | Actividad | Tiempo estimado |
|:-:|---|:-:|
| 1 | Leer el [capítulo 3](capitulo/capitulo-03-busqueda-informada.md) y responder los recuadros «Para pensar» | 110 min |
| 2 | Ver al menos tres [videos complementarios](complementos/videos.md) | 45-60 min |
| 3 | Explorar PathFinding.js y el visualizador del TSP de las [herramientas](complementos/herramientas.md) | 30 min |
| 4 | Realizar la [práctica de la semana](practicas/) en Google Colab | 2 h 30 min |
| 5 | Resolver las preguntas de repaso del final del capítulo | 45 min |
| 6 | Responder el cuestionario de autoevaluación (enlace en el Equipo de Teams) | 20 min |
| 7 | Explorar los [materiales adicionales](materiales-adicionales/) (opcional) | libre |
| 8 | Leer el enunciado de la [Actividad Evaluativa 2](../actividades-evaluativas/ae2-optimizacion-juegos/) y empezar la parte A | 2 h |
| 9 | Llevar tus dudas a la sesión sincrónica | 1 h |

## Lecturas base

- García Serrano, A. (2016). *Inteligencia artificial: Fundamentos, práctica y aplicaciones* (2.ª ed.), cap. 4.
- Russell, S. J., y Norvig, P. (2004). *Inteligencia artificial: Un enfoque moderno* (2.ª ed.), cap. 4 y cap. 5, secciones sobre vuelta atrás (consulta).

## Práctica

**Búsqueda informada y metaheurísticas en Python:** un cuaderno de Jupyter en el que resolverás las rutas de la semana 2 con A\* y la distancia en línea recta, compararás dos heurísticas en el 8-puzle, aplicarás la vuelta atrás a las *N* reinas y atacarás un viajante de comercio por 24 capitales de Colombia con *hill climbing*, temple simulado, búsqueda tabú y un algoritmo genético. Ver [`practicas/README.md`](practicas/README.md).

## Sesión sincrónica

- **Fecha y hora:** *[por definir]*
- **Enlace:** Equipo de Microsoft Teams del curso
- **Agenda sugerida:** realimentación general de la Actividad Evaluativa 1 · A\* a mano de Sevilla a Barcelona (pregunta de repaso 3) · discusión de los ejercicios 1 y 7 de la práctica · presentación del enunciado de la Actividad Evaluativa 2.

## Evaluación

Cuestionario de autoevaluación (formativo, 0 %), con retroalimentación automática por pregunta. La práctica no se califica, pero es la base de la parte A de la **Actividad Evaluativa 2**, que se entrega en la semana 4.
