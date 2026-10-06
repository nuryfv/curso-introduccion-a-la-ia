# Práctica · Semana 5: Representación del conocimiento y razonamiento

**Tipo:** práctica autónoma, no calificable
**Tiempo estimado:** 2 h 30 min
**Archivo:** [`practica-05-conocimiento-razonamiento.ipynb`](practica-05-conocimiento-razonamiento.ipynb)
**Herramientas:** Google Colab o Jupyter; ver [`complementos/herramientas.md`](../complementos/herramientas.md)
**Relación con el capítulo:** secciones 5.1 a 5.6

## Propósito

Escribir conocimiento de forma explícita y razonar con él:

| Parte | Qué construyes | Técnicas |
|---|---|---|
| 1 | Un verificador de consecuencia lógica | Lógica proposicional y tablas de verdad |
| 2 a 4 | Un sistema experto que diagnostica fallas de conexión a internet | Base de hechos y de reglas, encadenamiento hacia adelante y hacia atrás, explicación |
| 5 | Una red semántica de animales | Herencia, excepciones y tripletas |
| 6 y 7 | Un termostato difuso | Inferencia de Mamdani y simulación frente a un termostato de encendido y apagado |

Todas las celdas se probaron con Python 3 y solo usan `numpy` y `matplotlib`. Las cifras que cita el capítulo se obtuvieron con este cuaderno.

## Cómo abrir el cuaderno

**Opción 1. Google Colab (recomendada, no requiere instalación)**
1. Descarga el archivo `.ipynb` de esta carpeta.
2. Entra a https://colab.research.google.com con tu cuenta de Google.
3. Elige *Archivo → Subir cuaderno* y selecciona el archivo.

**Opción 2. Jupyter en tu computador**
Si ya tienes Python 3 y Jupyter instalados, abre el archivo con `jupyter notebook` o desde Visual Studio Code.

## Contenido

1. Lógica proposicional. **Ejercicio 1:** una falacia frecuente.
2. Un sistema experto: base de hechos y base de reglas.
3. Encadenamiento hacia adelante con explicación. **Ejercicio 2:** probar y ampliar el sistema experto.
4. Encadenamiento hacia atrás. **Ejercicio 3:** adelante contra atrás.
5. Red semántica con herencia y excepciones. **Ejercicio 4:** ampliar la red y explorar Wikidata.
6. Termostato difuso: funciones de pertenencia, reglas, inferencia de Mamdani paso a paso y superficie de control.
7. Simulación frente a un termostato nítido. **Ejercicio 5:** ajustar el controlador difuso.
8. Tabla de cierre.

## Qué llevar a la sesión sincrónica

Tu cuaderno con las celdas ejecutadas, las respuestas de los ejercicios 1 a 5 y la tabla de cierre. Compartiremos las reglas nuevas del ejercicio 2 y los ajustes del termostato del ejercicio 5.

> Esta práctica no se califica, pero es la base de la parte A de la [Actividad Evaluativa 3](../../actividades-evaluativas/ae3-conocimiento-datos/), que se entrega en la semana 6. Empieza ya a recolectar tus datos.
