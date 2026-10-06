# Práctica · Semana 3: Búsqueda informada, búsqueda local y metaheurísticas

**Tipo:** práctica autónoma, no calificable
**Tiempo estimado:** 2 h 30 min
**Archivo:** [`practica-03-busqueda-informada.ipynb`](practica-03-busqueda-informada.ipynb)
**Herramientas:** Google Colab o Jupyter; ver [`complementos/herramientas.md`](../complementos/herramientas.md)
**Relación con el capítulo:** secciones 3.1 a 3.9

## Propósito

Comprobar cuánto trabajo ahorra una buena heurística y comparar experimentalmente las técnicas de optimización del capítulo:

| Parte | Problema | Técnicas |
|---|---|---|
| I. Búsqueda de caminos | Rutas por carretera de la semana 2, con la distancia en línea recta como heurística | Coste uniforme, voraz y A\*; heurísticas no admisibles |
| I. Búsqueda de caminos | 8-puzle | A\* con *h*₁ (fichas mal colocadas) y *h*₂ (Manhattan); factor de ramificación efectivo |
| I. Búsqueda de caminos | *N* reinas | Vuelta atrás frente a fuerza bruta |
| II. Optimización | Viajante de comercio por 24 capitales de Colombia y por 100 puntos aleatorios | Vecino más cercano, *hill climbing* 2-opt, temple simulado, búsqueda tabú y algoritmo genético |

Todas las celdas se probaron con Python 3 y solo usan librerías que Google Colab trae instaladas (`matplotlib`). Las cifras que cita el capítulo se obtuvieron con este cuaderno.

## Cómo abrir el cuaderno

**Opción 1. Google Colab (recomendada, no requiere instalación)**
1. Descarga el archivo `.ipynb` de esta carpeta.
2. Entra a https://colab.research.google.com con tu cuenta de Google.
3. Elige *Archivo → Subir cuaderno* y selecciona el archivo.

**Opción 2. Jupyter en tu computador**
Si ya tienes Python 3 y Jupyter instalados, abre el archivo con `jupyter notebook` o desde Visual Studio Code.

## Contenido

1. El mapa de carreteras con coordenadas y la heurística de línea recta.
2. Una sola función para coste uniforme, voraz y A\*. **Ejercicios 1 y 2:** cuánto ahorra la heurística y qué pasa si exagera.
3. El 8-puzle con dos heurísticas. **Ejercicio 3:** factor de ramificación efectivo y dominancia.
4. Las *N* reinas con vuelta atrás. **Ejercicio 4:** cuánto poda la vuelta atrás.
5. El viajante de comercio por Colombia.
6. El vecino más cercano.
7. *Hill climbing* con 2-opt. **Ejercicio 5:** óptimos locales y reinicios.
8. Temple simulado. **Ejercicio 6:** el efecto de la temperatura.
9. Búsqueda tabú.
10. Algoritmo genético con cruce de orden.
11. Comparación final. **Ejercicio 7:** qué método elegir y cómo ajustar sus parámetros.
12. Tabla de cierre.

## Qué llevar a la sesión sincrónica

Tu cuaderno con las celdas ejecutadas, las respuestas de los ejercicios 1 a 7 y la tabla de cierre. Discutiremos en grupo los ejercicios 1 y 7.

> Esta práctica no se califica, pero es la base de la primera parte de la [Actividad Evaluativa 2](../../actividades-evaluativas/ae2-optimizacion-juegos/), que se entrega la próxima semana.
