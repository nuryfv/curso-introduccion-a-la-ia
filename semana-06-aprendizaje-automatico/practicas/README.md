# Práctica · Semana 6: Aprendizaje automático y clasificador bayesiano ingenuo

**Tipo:** práctica autónoma, no calificable
**Tiempo estimado:** 2 h 30 min
**Archivo:** [`practica-06-aprendizaje-automatico.ipynb`](practica-06-aprendizaje-automatico.ipynb)
**Herramientas:** Google Colab o Jupyter; ver [`complementos/herramientas.md`](../complementos/herramientas.md)
**Relación con el capítulo:** secciones 6.1 a 6.6

## Propósito

Programar desde cero el clasificador bayesiano ingenuo y aplicarlo a problemas distintos:

| Parte | Problema | Qué practicas |
|---|---|---|
| 1 | Una prueba médica | Probabilidad condicional y teorema de Bayes, con simulación |
| 2 | ¿Se juega el partido? | Bayes ingenuo con atributos categóricos y suavizado de Laplace |
| 3 | Filtro de *spam* en español | Bolsa de palabras, logaritmos, entrenamiento y prueba, matriz de confusión |
| 4 | Filtro con datos reales | El corpus *SMS Spam Collection* (5.574 SMS) y comparación con scikit-learn |
| 5 | Identificar el idioma de un texto | Trigramas de caracteres |
| 6 | Agrupar clientes sin etiquetas | Aprendizaje no supervisado con *k*-medias |

La sección 4 descarga el corpus *SMS Spam Collection* del repositorio de la Universidad de California en Irvine; si no hay conexión, el resto del cuaderno funciona igual. Todas las celdas se probaron con Python 3 y usan librerías que Google Colab trae instaladas. Las cifras que cita el capítulo se obtuvieron con este cuaderno.

## Cómo abrir el cuaderno

**Opción 1. Google Colab (recomendada, no requiere instalación)**
1. Descarga el archivo `.ipynb` de esta carpeta.
2. Entra a https://colab.research.google.com con tu cuenta de Google.
3. Elige *Archivo → Subir cuaderno* y selecciona el archivo.

**Opción 2. Jupyter en tu computador**
Necesitas Python 3 con `numpy`, `matplotlib` y `scikit-learn` (ver la [guía de configuración del entorno](../../guias/configuracion-entorno.md)).

## Contenido

1. Probabilidad y teorema de Bayes. **Ejercicio 1:** repetir la prueba.
2. Bayes ingenuo paso a paso. **Ejercicio 2:** el problema de la probabilidad cero.
3. Filtro de *spam* en español. **Ejercicio 3:** poner a prueba el filtro.
4. El corpus *SMS Spam Collection*. **Ejercicio 4:** datos desbalanceados.
5. Identificar el idioma. **Ejercicio 5:** ¿dónde se confunde?
6. Aprendizaje no supervisado con *k*-medias. **Ejercicio 6:** ¿qué significan los grupos?
7. Tabla de cierre.

## Qué llevar a la sesión sincrónica

Tu cuaderno con las celdas ejecutadas, las respuestas de los ejercicios 1 a 6 y la tabla de cierre. Probaremos en vivo los mensajes «trampa» del ejercicio 3.

> Esta práctica no se califica, pero la clase `BayesIngenuoCategorico` es la base de la parte B de la [Actividad Evaluativa 3](../../actividades-evaluativas/ae3-conocimiento-datos/), que se entrega esta semana.
