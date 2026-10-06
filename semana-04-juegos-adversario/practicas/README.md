# Práctica · Semana 4: Juegos y decisiones con adversario

**Tipo:** práctica autónoma, no calificable
**Tiempo estimado:** 2 h 30 min
**Archivo:** [`practica-04-juegos-adversario.ipynb`](practica-04-juegos-adversario.ipynb)
**Herramientas:** Google Colab o Jupyter; ver [`complementos/herramientas.md`](../complementos/herramientas.md)
**Relación con el capítulo:** secciones 4.1 a 4.6

## Propósito

Construir agentes que juegan contra un adversario y medir cuánto trabajo ahorran la poda y una buena función de evaluación:

| Parte | Juego | Técnicas |
|---|---|---|
| 1 a 4 | Tres en raya | Minimax, negamax, poda alfa-beta y ordenación de movimientos; torneo contra un jugador aleatorio; partida contra ti |
| 5 y 6 | Conecta 4 | Alfa-beta con profundidad limitada, función de evaluación y torneo entre agentes |
| 7 | Un juego con moneda | Expectiminimax y la escala de la función de evaluación |

Todas las celdas se probaron con Python 3 y no necesitan librerías externas. Las cifras que cita el capítulo se obtuvieron con este cuaderno.

## Cómo abrir el cuaderno

**Opción 1. Google Colab (recomendada, no requiere instalación)**
1. Descarga el archivo `.ipynb` de esta carpeta.
2. Entra a https://colab.research.google.com con tu cuenta de Google.
3. Elige *Archivo → Subir cuaderno* y selecciona el archivo.

**Opción 2. Jupyter en tu computador**
Si ya tienes Python 3 y Jupyter instalados, abre el archivo con `jupyter notebook` o desde Visual Studio Code.

## Contenido

1. El tres en raya como problema de búsqueda.
2. Minimax. **Ejercicio 1:** leer el árbol.
3. Negamax.
4. Poda alfa-beta. **Ejercicio 2:** el orden de los movimientos. Torneo contra un jugador aleatorio y partida contra la IA.
5. Conecta 4 con profundidad limitada y función de evaluación. **Ejercicio 3:** el costo de mirar más lejos.
6. Torneo de Conecta 4. **Ejercicio 4:** diseña tu función de evaluación.
7. Expectiminimax. **Ejercicio 5:** la escala de la evaluación.
8. Tabla de cierre.

## Qué llevar a la sesión sincrónica

Tu cuaderno con las celdas ejecutadas, las respuestas de los ejercicios 1 a 5 y la tabla de cierre. Haremos un pequeño torneo con las funciones de evaluación del ejercicio 4.

> Esta práctica no se califica, pero el agente de Conecta 4 es el punto de partida de la parte B de la [Actividad Evaluativa 2](../../actividades-evaluativas/ae2-optimizacion-juegos/), que se entrega esta semana.
