# Semana 4. Juegos y decisiones con adversario

Hasta ahora el agente estaba solo frente al problema. Esta semana aparece un **adversario** que también juega y que quiere lo contrario que tú. Estudias cómo decidir suponiendo que el rival juega perfecto (minimax), cómo ahorrar la mayor parte del trabajo sin cambiar la decisión (poda alfa-beta) y qué hacer cuando el juego es tan grande que hay que cortar la búsqueda y estimar quién va ganando (funciones de evaluación). Cierras la semana entregando la **Actividad Evaluativa 2**.

## Objetivos de aprendizaje

1. Clasificar un juego según el número de jugadores, la información, el azar y la suma de sus resultados.
2. Representar un juego como un árbol de juego con estado inicial, movimientos, test terminal y utilidad.
3. Calcular el valor minimax de un árbol y escribir el algoritmo en su forma negamax.
4. Aplicar la poda alfa-beta y explicar cómo influye el orden de los movimientos.
5. Diseñar una función de evaluación y reconocer el efecto horizonte.
6. Extender minimax a juegos con más jugadores y con azar (expectiminimax).

## Temas de la semana

- IA y juegos: juegos de suma cero y de información perfecta
- Árboles de juego
- Algoritmo minimax y negamax
- Funciones de evaluación
- Poda alfa-beta
- Juegos con más jugadores y juegos con azar

## Ruta de estudio

| Paso | Actividad | Tiempo estimado |
|:-:|---|:-:|
| 1 | Leer el [capítulo 4](capitulo/capitulo-04-juegos-adversario.md) y responder los recuadros «Para pensar» | 90 min |
| 2 | Ver al menos dos [videos complementarios](complementos/videos.md) | 30-60 min |
| 3 | Practicar la poda a mano con *Alpha-Beta Pruning Practice* de las [herramientas](complementos/herramientas.md) | 20 min |
| 4 | Realizar la [práctica de la semana](practicas/) en Google Colab | 2 h 30 min |
| 5 | Resolver las preguntas de repaso del final del capítulo | 45 min |
| 6 | Explorar los [materiales adicionales](materiales-adicionales/) (opcional) | libre |
| 7 | Llevar tus dudas a la sesión sincrónica | 1 h |
| 8 | Terminar y entregar la [Actividad Evaluativa 2](../actividades-evaluativas/ae2-optimizacion-juegos/) | según el enunciado |

## Lecturas base

- García Serrano, A. (2016). *Inteligencia artificial: Fundamentos, práctica y aplicaciones* (2.ª ed.), cap. 5.
- Russell, S. J., y Norvig, P. (2004). *Inteligencia artificial: Un enfoque moderno* (2.ª ed.), cap. 6 (consulta).

## Práctica

**Juegos con adversario en Python:** un cuaderno de Jupyter en el que programarás minimax, negamax y alfa-beta para el tres en raya, medirás cuántos nodos ahorra la poda, jugarás contra tu agente, construirás un jugador de Conecta 4 con profundidad limitada y función de evaluación, y comprobarás por qué el azar cambia las reglas. Ver [`practicas/README.md`](practicas/README.md).

## Sesión sincrónica

- **Fecha y hora:** *[por definir]*
- **Enlace:** Equipo de Microsoft Teams del curso
- **Agenda sugerida:** poda alfa-beta a mano sobre un árbol nuevo · torneo de Conecta 4 con las funciones de evaluación del ejercicio 4 · dudas finales de la Actividad Evaluativa 2.

## Evaluación

Entrega de la **Actividad Evaluativa 2** (25 %), que abarca las semanas 3 y 4, en la tarea del Equipo de Teams. La práctica de esta semana no se califica, pero es la base de la parte B de la actividad.
