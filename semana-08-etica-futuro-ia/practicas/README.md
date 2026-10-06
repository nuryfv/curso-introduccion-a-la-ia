# Práctica · Semana 8: Análisis de casos y Moral Machine

**Tipo:** práctica autónoma, no calificable
**Tiempo estimado:** 2 horas (más 45 minutos si haces la parte C opcional)
**Herramientas:** Moral Machine y Google Colab; ver [`complementos/herramientas.md`](../complementos/herramientas.md)
**Relación con el capítulo:** secciones 8.1 a 8.7

## Propósito

Aplicar los conceptos y marcos del capítulo a casos reales, enfrentarte a dilemas morales que hoy deben resolver quienes diseñan sistemas de IA y, si quieres, auditar con datos el sesgo de un modelo.

| Parte | Qué haces | Tiempo |
|---|---|:-:|
| A | Analizar un caso real de impacto de la IA con una ficha estructurada | 60 min |
| B | Juzgar escenarios en Moral Machine y reflexionar sobre tus resultados | 60 min |
| C (opcional) | Auditar el sesgo de un modelo de selección de personal en Python | 45 min |

Crea un archivo `practica-semana-08.md` (o un documento de texto) para registrar tus respuestas. Llévalo a la sesión de cierre.

---

## Parte A. Análisis de un caso (60 min)

Elige **un** caso:

1. Uno de los cuatro casos de la tabla 8.2 del capítulo (reconocimiento facial, COMPAS, selección de personal o salud).
2. El caso Cambridge Analytica (sección 8.5.1).
3. Un caso de la **AI Incident Database** (https://incidentdatabase.ai), una base de datos pública de incidentes reales causados por sistemas de IA. Busca uno ocurrido en América Latina o en un sector que te interese.

Completa esta ficha, consultando al menos **una fuente primaria** (el estudio, la noticia original o el informe):

| Campo | Tu análisis |
|---|---|
| **Hechos** | ¿Qué sistema era, quién lo usaba, para qué y qué ocurrió? |
| **Personas afectadas** | ¿Quiénes salieron perjudicadas? ¿Quiénes se beneficiaban del sistema? |
| **Origen técnico del problema** | ¿Datos (qué tipo de sesgo, sección 8.2.1), modelo, interfaz o uso? Relaciónalo con lo que aprendiste en las semanas 6 y 7. |
| **Principios afectados** | ¿Qué principios de la Recomendación de la UNESCO (tabla 8.3) se vulneraron? |
| **Nivel de riesgo** | ¿En qué nivel del Reglamento europeo de IA (figura 8.1) estaría el sistema? ¿Qué obligaciones tendría? |
| **¿Qué habría cambiado?** | Tres prácticas concretas de la tabla 8.4 que habrían evitado o reducido el daño. |
| **Tu postura** | ¿Debería existir este sistema? ¿Con qué condiciones? Argumenta en un párrafo. |
| **Fuentes** | Referencias en APA. |

## Parte B. Moral Machine (60 min)

**Moral Machine** es una plataforma del MIT que presenta dilemas en los que un vehículo autónomo sin frenos debe elegir entre dos males. Con las respuestas de millones de personas en 233 países y territorios, sus autores estudiaron cómo cambian las preferencias morales entre culturas (Awad et al., 2018).

1. Entra a https://www.moralmachine.net/hl/es y pulsa **Comenzar a juzgar**. Responde los 13 escenarios. Antes de cada respuesta, lee con calma la descripción de las personas y los animales de cada lado.
2. Al terminar, revisa tu página de **resultados**: tus preferencias en cada dimensión (salvar a más vidas, proteger a los pasajeros, respetar las normas, intervenir o no, género, edad, especie, estatus social, condición física) comparadas con el promedio de los demás participantes.
3. Responde:
   - ¿Qué resultado te sorprendió? ¿Refleja lo que piensas o hubo dimensiones en las que decidiste casi al azar?
   - ¿Debería un vehículo autónomo decidir según la **mayoría** de las respuestas de las personas? ¿Qué problemas tendría hacerlo?
   - Algunas dimensiones (género, estatus social, condición física) chocan con el principio de **no discriminación**. ¿Debería prohibirse que un sistema use esa información? Relaciónalo con la sección 8.2.
   - Russell y Norvig (2004, cap. 26) señalan que, cuando un sistema de IA causa un daño, no está claro quién es el responsable. En un accidente de un vehículo autónomo, ¿quién debería responder: el fabricante, quien programó el sistema, la persona propietaria o nadie?
4. Opcional: en la sección **Diseñar** de la plataforma, crea un escenario propio que represente un dilema que te parezca difícil, y explica por qué.

## Parte C (opcional). Auditoría de sesgo en Python (45 min)

Abre en Google Colab el cuaderno [`practica-08-auditoria-sesgo.ipynb`](practica-08-auditoria-sesgo.ipynb). Con datos **sintéticos**, entrenarás el clasificador bayesiano de la semana 6 con un historial de contratación sesgado y medirás, con la razón de impacto y la tasa de selección de candidaturas con mérito, qué pasa cuando eliminas el atributo sensible. Responde las preguntas del ejercicio final. Las cifras que cita la sección 8.2.2 del capítulo se obtuvieron con este cuaderno.

---

## Para la sesión de cierre

Lleva tu ficha de la parte A y tus respuestas de la parte B. Compararemos los resultados de Moral Machine del grupo y discutiremos los casos analizados.

> Esta práctica no se califica, pero la ficha de la parte A es un buen modelo para el análisis ético y de impacto de la [Actividad Evaluativa 4](../../actividades-evaluativas/ae4-proyecto-integrador/).
