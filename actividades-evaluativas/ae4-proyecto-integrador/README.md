# Actividad Evaluativa 4. Proyecto integrador

- **Semanas que abarca:** 7 y 8
- **Entrega:** semana 8 (18 de noviembre de 2026), en la tarea del Equipo de Teams
- **Valor:** 25 % de la nota final
- **Modalidad:** individual
- **Tiempo estimado:** 14 a 16 horas

## Descripción

Construyes un **prototipo de IA** que resuelve un problema real, basado en una **red neuronal** que programas en Python o en un **modelo que entrenas con una herramienta** como Teachable Machine. Lo evalúas con rigor, analizas su **impacto ético y social** con los marcos de la semana 8 y lo presentas en un **video**. Es la actividad que integra el curso: el «saber» (cómo funciona), el «hacer» (construirlo y evaluarlo) y el «ser» (analizar críticamente sus consecuencias).

## Resultados de aprendizaje que se evalúan

1. Construye y evalúa un prototipo basado en redes neuronales o en un modelo entrenado con una herramienta especializada (capítulo 7).
2. Analiza de forma crítica y ética las posibilidades, limitaciones e impactos de su prototipo, con marcos de referencia reconocidos (capítulo 8).
3. Comunica de forma clara y honesta lo que su sistema hace, lo que no hace y sus riesgos.

## Calendario sugerido

| Cuándo | Qué |
|---|---|
| Semana 7, a más tardar el viernes | **Registrar la propuesta** en la tarea «Propuesta AE4» del Equipo de Teams (ver parte A). |
| Semana 7 | Recolectar o conseguir los datos y entrenar una primera versión. |
| Semana 8 | Evaluar, hacer el análisis ético, grabar el video y entregar. |

---

## Parte A. Propuesta (requisito, sin nota)

Antes de construir, registra en Teams una propuesta de media página con:

1. **Problema y usuarios:** ¿qué problema real resuelves y para quién?
2. **Enfoque:** opción 1 o 2 de la parte B, y qué tipo de datos (imágenes, sonidos, posturas, texto o datos tabulares).
3. **Datos:** de dónde saldrán, cuántos ejemplos esperas y con qué licencia o permiso.
4. **Primer riesgo que ves:** una frase.

La docente responderá con aprobación o ajustes. **No se califica un proyecto sin propuesta registrada.**

Algunas ideas, para inspirarte:

| Idea | Tipo de datos | Riesgo a analizar |
|---|---|---|
| Clasificar residuos (plástico, papel, orgánico, vidrio) para una caneca inteligente | Imágenes | ¿Funciona con distintas luces y con objetos aplastados o sucios? |
| Reconocer sonidos de alerta (timbre, alarma, llanto de bebé) para personas sordas | Sonidos | ¿Qué pasa con un falso negativo? ¿Quién usaría el sistema y cómo se probó con ellas? |
| Detectar una mala postura frente al computador durante el teletrabajo | Posturas | Privacidad de la cámara en casa; distintos cuerpos y sillas. |
| Reconocer algunas señas básicas de la Lengua de Señas Colombiana | Imágenes o posturas | Representatividad de las personas usuarias; participación de la comunidad sorda en el diseño. |
| Clasificar solicitudes ciudadanas (PQRS) por dependencia, con datos públicos | Texto | Errores que retrasan respuestas a ciudadanos; lenguaje de distintas regiones. |
| Clasificar el estado de madurez de una fruta | Imágenes | Variedades, luz, cámaras de distinta calidad. |

Evita los problemas de **riesgo inaceptable** del Reglamento europeo de IA (sección 8.3.2) y los que exigirían datos sensibles de otras personas (salud, rasgos biométricos de identificación, menores de edad). Si tu idea está en una zona gris, coméntala en la propuesta.

---

## Parte B. Prototipo (35 %)

Elige **una** opción:

**Opción 1. Red neuronal en Python**

- Entrena una red neuronal (perceptrón multicapa o red convolucional) con `scikit-learn`, Keras/TensorFlow o PyTorch, o con tu propia implementación de la práctica de la semana 7.
- Usa un conjunto de datos **propio** o **público con licencia que permita su uso** (cítalo).
- Separa datos de **entrenamiento**, **validación** y **prueba**. Ajusta los hiperparámetros con la validación y reporta el resultado final **solo una vez** con la prueba.
- Prueba al menos **tres configuraciones** (por ejemplo, número de capas o neuronas, tasa de aprendizaje o épocas) y justifica la elegida.

**Opción 2. Modelo entrenado con una herramienta**

- Entrena un modelo de imagen, sonido o postura en **Teachable Machine** (u otra herramienta equivalente aprobada en la propuesta), con **al menos 3 clases** y **al menos 80 ejemplos por clase recolectados por ti**, con variedad de condiciones.
- Reserva un **conjunto de prueba propio**: al menos **20 ejemplos nuevos por clase**, capturados otro día o en otras condiciones, que el modelo no haya visto.
- Prueba al menos **dos versiones** del modelo (por ejemplo, con más datos, más variedad o distintos parámetros avanzados de entrenamiento) y compara sus resultados.
- Integra el modelo en una **demostración mínima**: una página web con el código que exporta la herramienta, o el enlace compartible del modelo con instrucciones de uso.

**En ambas opciones**, el prototipo debe tener una forma de **usarse** (una celda de Colab que recibe una entrada nueva, una página web o el enlace del modelo) y debe mostrar al usuario su **nivel de confianza** en cada predicción.

## Parte C. Evaluación del prototipo (15 %)

1. **Métricas:** matriz de confusión, exactitud, y precisión y exhaustividad por clase, sobre el conjunto de prueba.
2. **Línea base:** compara con una solución simple sin redes neuronales (por ejemplo, predecir siempre la clase más frecuente, el clasificador bayesiano de la semana 6 o una regla). ¿Cuánto aporta realmente la red?
3. **Análisis de errores:** muestra al menos **cinco errores** del modelo y explica por qué crees que ocurrieron.
4. **Pruebas de robustez:** evalúa el modelo en al menos **dos condiciones distintas** de las de entrenamiento (otra luz, otro fondo, otra persona, ruido de fondo, otro estilo de redacción) y reporta cómo cambia el rendimiento.

## Parte D. Análisis ético y de impacto (25 %)

Usa las dos plantillas de [`recursos/`](recursos/):

1. **Ficha de modelo** (*model card*, sección 8.2.4): propósito y usos previstos, usos **no** previstos, datos, evaluación, limitaciones conocidas y recomendaciones.
2. **Evaluación de impacto**, que responda con argumentos y referencias:
   - **Personas afectadas:** quiénes se benefician, quiénes podrían salir perjudicadas y si participaron en el diseño.
   - **Privacidad:** qué datos personales trata el sistema y cómo cumpliría la Ley 1581 de 2012.
   - **Sesgos y equidad:** ¿funciona igual para todas las personas o condiciones? Usa tus pruebas de robustez como evidencia.
   - **Nivel de riesgo** según el Reglamento europeo de IA y obligaciones que tendría.
   - **Principios de la UNESCO** más relevantes para tu caso y cómo los atiendes.
   - **Impacto en el trabajo y en el ambiente:** ¿reemplaza o apoya alguna tarea humana? ¿Cuánto cómputo necesita?
   - **Medidas** concretas de mitigación, siguiendo la tabla 8.4.
   - **Conclusión honesta:** ¿debería usarse tu prototipo en el mundo real? ¿Con qué condiciones?

## Parte E. Video de presentación (15 %)

Graba un video de **5 a 7 minutos** con esta estructura:

1. **El problema y para quién** (1 min).
2. **Demostración en vivo** del prototipo, incluido al menos **un caso en que falla** (2 min).
3. **Cómo funciona y cómo se evaluó**, con los resultados principales (1 a 2 min).
4. **Riesgos y medidas** de la evaluación de impacto (1 a 2 min).
5. **Conclusión:** qué aprendiste y qué harías distinto (30 s).

Debe escucharse tu voz y verse la pantalla. Súbelo a Microsoft Stream o a YouTube como **no listado** y comparte el enlace. No incluyas datos personales de otras personas sin su autorización.

## Parte F. Informe y repositorio (10 %)

Redacta un informe de **8 a 12 páginas** siguiendo la [plantilla de informe](../../recursos/plantillas/plantilla-informe.md), que incluya las partes B, C y D, las referencias en APA y la declaración de uso de IA. La ficha de modelo y la evaluación de impacto pueden ir como anexos.

## Entregables

En tu repositorio de entregas, dentro de la carpeta `ae4/`:

| Archivo | Contenido |
|---|---|
| `README.md` | Tu nombre, el problema, la opción elegida, **cómo usar el prototipo** y el enlace al video. |
| `ae4.ipynb` (opción 1) o carpeta `demo/` (opción 2) | El código o la demostración, **ejecutado** y con instrucciones. |
| `evaluacion/` | Las métricas, la matriz de confusión y las evidencias de las pruebas de robustez (por ejemplo, capturas). |
| `ficha-modelo.md` | La ficha de modelo. |
| `evaluacion-impacto.md` | La evaluación de impacto. |
| `informe.pdf` | El informe. |

No subas al repositorio imágenes, audios o videos en los que se pueda identificar a otras personas. Si tus datos de entrenamiento pesan mucho, sube solo una muestra y explica dónde están los demás.

En la tarea de Teams entrega **el enlace a tu repositorio**, **el informe en PDF** y **el enlace al video**. Revisa la [guía de entregas](../../guias/entregas-en-teams.md).

## Uso de herramientas de IA generativa

Puedes usar asistentes de IA para resolver dudas, depurar código o revisar la redacción, con tres condiciones:

1. Incluye en el informe una sección **«Declaración de uso de IA»** que diga qué herramienta usaste, para qué y en qué partes. Si no usaste ninguna, decláralo también.
2. **El análisis ético debe ser tuyo**, apoyado en tus datos y tus pruebas. Un texto genérico que podría aplicarse a cualquier proyecto se califica como insuficiente.
3. Debes poder explicar cualquier parte de tu trabajo. La docente puede pedirte que lo hagas en la sesión de cierre.

## Evaluación

Ver la [rúbrica](rubrica.md).

## Preguntas frecuentes

**¿Puedo reutilizar el problema de la Actividad Evaluativa 3?** Sí, si ahora lo resuelves con una red neuronal y comparas con tu clasificador bayesiano como línea base. Indícalo en la propuesta.

**Mi modelo de Teachable Machine acierta el 100 % en la vista previa. ¿Ya está?** No. La vista previa usa condiciones parecidas a las del entrenamiento. Lo que se evalúa es el rendimiento con tu conjunto de prueba propio y en las pruebas de robustez.

**¿Puedo usar un modelo preentrenado o la API de un modelo de lenguaje?** Puedes usar aprendizaje por transferencia (como hace Teachable Machine). Si quieres construir el prototipo alrededor de la API de un modelo de lenguaje, plantéalo en la propuesta: deberás evaluarlo con un conjunto de prueba propio y analizar con especial cuidado la privacidad de los datos que envías y las alucinaciones.
