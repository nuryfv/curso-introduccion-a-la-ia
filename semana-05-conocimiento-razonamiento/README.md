# Semana 5. Representación del conocimiento y razonamiento

Hasta ahora el conocimiento sobre cada problema estaba escondido dentro del código. Esta semana lo escribes de forma **explícita**, como hechos y reglas que un programa puede combinar y explicar: es el enfoque de la IA simbólica y de los sistemas expertos. También aprendes a razonar con conceptos **vagos**, como «un poco de frío» o «potencia media», con la lógica difusa. Esta semana empieza la **Actividad Evaluativa 3**, que compara este enfoque con el aprendizaje a partir de datos de la semana 6.

## Objetivos de aprendizaje

1. Usar la lógica proposicional para representar hechos y reglas, y decidir si una conclusión se deduce de ellos.
2. Describir la arquitectura de un sistema experto.
3. Aplicar el encadenamiento hacia adelante y hacia atrás, y elegir el más adecuado para un problema.
4. Representar conocimiento con redes semánticas y ontologías, con herencia y excepciones.
5. Definir conjuntos difusos y variables lingüísticas.
6. Construir un sistema de inferencia difusa de Mamdani y compararlo con un controlador nítido.

## Temas de la semana

- Lógica e IA simbólica
- Sistemas expertos: base de hechos, base de reglas y motor de inferencia
- Encadenamiento hacia adelante y hacia atrás
- Redes semánticas y ontologías
- Conjuntos difusos
- Inferencia difusa (método de Mamdani)

## Ruta de estudio

| Paso | Actividad | Tiempo estimado |
|:-:|---|:-:|
| 1 | Leer el [capítulo 5](capitulo/capitulo-05-conocimiento-razonamiento.md) y responder los recuadros «Para pensar» | 100 min |
| 2 | Ver al menos tres [videos complementarios](complementos/videos.md) | 45-60 min |
| 3 | Explorar Wikidata con las [herramientas](complementos/herramientas.md) | 15 min |
| 4 | Realizar la [práctica de la semana](practicas/) en Google Colab | 2 h 30 min |
| 5 | Resolver las preguntas de repaso del final del capítulo | 45 min |
| 6 | Responder el cuestionario de autoevaluación (enlace en el Equipo de Teams) | 20 min |
| 7 | Leer el enunciado de la [Actividad Evaluativa 3](../actividades-evaluativas/ae3-conocimiento-datos/), elegir el problema y **empezar a recolectar los datos** | 2 h |
| 8 | Explorar los [materiales adicionales](materiales-adicionales/) (opcional) | libre |
| 9 | Llevar tus dudas a la sesión sincrónica | 1 h |

## Lecturas base

- García Serrano, A. (2016). *Inteligencia artificial: Fundamentos, práctica y aplicaciones* (2.ª ed.), cap. 6.
- Russell, S. J., y Norvig, P. (2004). *Inteligencia artificial: Un enfoque moderno* (2.ª ed.), cap. 7 (lógica proposicional y encadenamiento), cap. 10 (redes semánticas) y cap. 14, sección sobre lógica difusa (consulta).

## Práctica

**Conocimiento y razonamiento en Python:** un cuaderno de Jupyter en el que comprobarás consecuencias lógicas con tablas de verdad, construirás un sistema experto que diagnostica fallas de conexión a internet con encadenamiento hacia adelante y hacia atrás, consultarás una red semántica con herencia y excepciones, y programarás un termostato difuso que compararás con uno de encendido y apagado. Ver [`practicas/README.md`](practicas/README.md).

## Sesión sincrónica

- **Fecha y hora:** *[por definir]*
- **Enlace:** Equipo de Microsoft Teams del curso
- **Agenda sugerida:** realimentación general de la Actividad Evaluativa 2 · encadenamiento hacia adelante y hacia atrás a mano (preguntas de repaso 4 y 5) · ajustes del termostato difuso (ejercicio 5) · revisión de los problemas y datos elegidos para la Actividad Evaluativa 3.

## Evaluación

Cuestionario de autoevaluación (formativo, 0 %), con retroalimentación automática por pregunta. La práctica no se califica, pero es la base de la parte A de la **Actividad Evaluativa 3**, que se entrega en la semana 6.
