# Actividad Evaluativa 3. Del conocimiento experto a los datos

- **Semanas que abarca:** 5 y 6
- **Entrega:** semana 6 (8 de noviembre de 2026), en la tarea del Equipo de Teams
- **Valor:** 25 % de la nota final
- **Modalidad:** individual
- **Tiempo estimado:** 10 a 12 horas, más el tiempo de recolección de datos

## Descripción

Vas a resolver **el mismo problema de clasificación de dos maneras**: con un sistema que razona con **conocimiento experto** (reglas o lógica difusa, semana 5) y con un clasificador que **aprende de datos** (Bayes ingenuo, semana 6). Los datos los recolectas tú. Al final comparas los dos enfoques con los mismos datos de prueba y reflexionas sobre cuándo conviene cada uno.

## Resultados de aprendizaje que se evalúan

1. Construye un sistema basado en reglas con encadenamiento hacia adelante o un sistema de inferencia difusa de Mamdani (capítulo 5).
2. Recolecta y documenta un conjunto de datos de forma ética, y entrena y evalúa un clasificador bayesiano ingenuo (capítulo 6).
3. Compara críticamente un enfoque basado en conocimiento con uno basado en datos, considerando su rendimiento, su explicabilidad y su costo de desarrollo.

## Calendario sugerido

| Cuándo | Qué |
|---|---|
| Semana 5, primeros días | Elegir el problema y diseñar el formulario o la planilla de recolección. |
| Semana 5 | Recolectar los datos y escribir las reglas **antes** de mirar los datos de prueba. |
| Semana 6 | Implementar Bayes ingenuo, comparar y redactar el informe. |

---

## Parte A. El problema y los datos (15 %)

### A.1 Elige un problema de clasificación

Elige un problema de tu vida académica, laboral o cotidiana que cumpla estas condiciones:

- Se quiere predecir una **clase** con 2 a 4 valores posibles.
- Hay **al menos 4 atributos** categóricos o que se puedan discretizar en rangos (por ejemplo, «menos de 6 horas», «6 a 8 horas», «más de 8 horas»).
- **Tienes una idea propia** de cómo se decide, o puedes entrevistar a alguien que la tenga: la necesitarás para escribir las reglas.

Algunas ideas:

| Problema | Clase | Atributos posibles |
|---|---|---|
| ¿Llegaré tarde a clase o al trabajo? | a tiempo / tarde | día de la semana, hora de salida, clima, medio de transporte, ¿hubo evento en la ciudad? |
| ¿Mi código pasará las pruebas al primer intento? | sí / no | tamaño del cambio, horas de sueño, tipo de tarea, hora del día, ¿escribí pruebas antes? |
| Prioridad de un ticket de soporte de tu trabajo (anonimizado) | baja / media / alta | tipo de usuario, sistema afectado, palabras clave, número de usuarios afectados |
| ¿Este mensaje de correo requiere respuesta hoy? | sí / no | remitente (categoría), asunto, longitud, ¿tiene adjunto?, ¿me mencionan? |
| ¿Recomendaría esta película o serie? | sí / no | género, duración, idioma, ¿la vi acompañado?, plataforma |
| ¿Qué tan productiva fue mi jornada de estudio? | baja / media / alta | horas de sueño, lugar de estudio, ¿usé el celular?, hora de inicio, ¿había hecho ejercicio? |

También puedes proponer otro problema. Si tus atributos son **textos** (por ejemplo, comentarios de clientes), puedes usar la variante multinomial de Bayes ingenuo de la sección 3 de la práctica de la semana 6.

### A.2 Recolecta los datos

- Reúne **al menos 60 ejemplos** etiquetados. Más ejemplos dan resultados más confiables.
- Puedes recolectarlos llevando un registro diario, con un formulario de Microsoft Forms a tus compañeros, observando un proceso o exportando registros de un sistema al que tengas acceso autorizado.
- Guárdalos en un archivo `datos.csv`, con una fila por ejemplo y una columna por atributo, más la columna de la clase.

### A.3 Documenta los datos

Completa un **diccionario de datos** y una **ficha de recolección** con la [plantilla de `recursos/`](recursos/):

1. Qué significa cada atributo, qué valores toma y cómo se discretizó.
2. Cómo, cuándo y dónde se recolectaron los datos, y quién los etiquetó.
3. La distribución de las clases (cuántos ejemplos hay de cada una).
4. Las **limitaciones y posibles sesgos**: ¿a quién o qué representan tus datos y a quién o qué no?

### A.4 Cuida la ética y la privacidad

- **No recolectes datos sensibles**: salud, origen étnico, orientación sexual, creencias religiosas o políticas, datos biométricos ni datos de menores de edad. La Ley 1581 de 2012 de Colombia exige una protección especial para estos datos.
- Si tus datos son sobre otras personas, pídeles **consentimiento** con el texto de la plantilla y **no guardes nombres, documentos, correos ni teléfonos**.
- Si exportas datos de tu trabajo, **anonimízalos** y confirma que tienes autorización para usarlos.

### A.5 Separa los datos de prueba **antes** de empezar

Antes de escribir tus reglas, separa al azar el **30 %** de los ejemplos como **conjunto de prueba** (con una semilla fija, para que sea reproducible) y guárdalo en `prueba.csv`. **No lo mires** hasta la parte D: si escribes las reglas viendo los datos de prueba, la comparación no será justa.

---

## Parte B. Sistema basado en conocimiento (20 %)

Elige **una** de estas dos opciones:

**Opción 1. Sistema experto con encadenamiento hacia adelante**

- Al menos **10 reglas** SI-ENTONCES que concluyan la clase, con al menos **2 niveles** de encadenamiento (reglas cuyas conclusiones son condiciones de otras reglas).
- Las reglas deben salir de **tu conocimiento** del problema o de una **entrevista a un experto** (si entrevistas a alguien, resume la entrevista en el informe). Puedes revisar los datos de **entrenamiento**, pero no los de prueba.
- El sistema debe **explicar** cada conclusión, como el de la práctica de la semana 5.
- Define qué hace el sistema cuando **ninguna regla** concluye una clase (por ejemplo, una clase por defecto).

**Opción 2. Sistema de inferencia difusa de Mamdani**

- Al menos **2 variables de entrada** con 3 o más conjuntos difusos cada una, y una salida.
- Al menos **6 reglas** difusas, presentadas como una matriz FAM.
- Una forma justificada de convertir la salida defuzzificada en una clase (por ejemplo, umbrales).
- Gráficas de las funciones de pertenencia y de la superficie de control.

Puedes partir del código de la [práctica de la semana 5](../../semana-05-conocimiento-razonamiento/practicas/), indicando qué reutilizaste.

---

## Parte C. Clasificador bayesiano ingenuo (20 %)

1. Implementa el clasificador bayesiano ingenuo **desde cero**, con **suavizado de Laplace**. Puedes partir de la clase `BayesIngenuoCategorico` de la [práctica de la semana 6](../../semana-06-aprendizaje-automatico/practicas/).
2. Entrénalo **solo** con los datos de entrenamiento.
3. Muestra las tablas de probabilidades aprendidas para al menos dos atributos e interprétalas: ¿qué valores de cada atributo hacen más probable cada clase?
4. Como verificación, compara tus resultados con los de `CategoricalNB` de scikit-learn (opcional, pero recomendado).

---

## Parte D. Comparación (25 %)

Evalúa **los dos sistemas sobre el mismo conjunto de prueba** y responde con datos:

1. **Rendimiento.** Matriz de confusión, exactitud, y precisión y exhaustividad por clase de cada sistema.
2. **Estabilidad.** Repite la división entrenamiento/prueba con al menos 10 semillas distintas y reporta la media y la desviación estándar de la exactitud de Bayes ingenuo. (El sistema basado en conocimiento no se reentrena, pero evalúalo sobre los mismos conjuntos de prueba).
3. **Curva de aprendizaje.** Entrena Bayes ingenuo con el 25 %, el 50 %, el 75 % y el 100 % de los datos de entrenamiento y grafica su exactitud en el conjunto de prueba. ¿Con cuántos ejemplos supera (o no) al sistema basado en conocimiento?
4. **Explicabilidad.** Elige dos ejemplos de prueba (uno bien clasificado y uno mal clasificado por alguno de los sistemas) y muestra cómo «explica» su decisión cada uno.
5. **Desacuerdos.** ¿En qué ejemplos no coinciden los dos sistemas? ¿Quién tenía razón y por qué?
6. **Costo.** ¿Cuánto tiempo te tomó construir cada sistema? ¿Qué fue lo más difícil de cada uno?

---

## Parte E. Reflexión crítica (10 %)

En 400 a 700 palabras, responde:

1. Si tuvieras que poner uno de los dos sistemas en producción para que lo usaran otras personas, ¿cuál elegirías y por qué? ¿Combinarías ambos? ¿Cómo?
2. ¿Qué sesgos de tus datos podría haber aprendido Bayes ingenuo? ¿Y qué sesgos tuyos quedaron en tus reglas?
3. ¿Qué pasaría con cada sistema si las condiciones del problema cambiaran (por ejemplo, un nuevo medio de transporte, un nuevo tipo de ticket)?

---

## Parte F. Informe y repositorio (10 %)

Redacta un informe de **8 a 12 páginas** siguiendo la [plantilla de informe](../../recursos/plantillas/plantilla-informe.md), con: descripción del problema, datos (diccionario y ficha), sistema basado en conocimiento, clasificador bayesiano, comparación, reflexión crítica, conclusiones, referencias en APA y declaración de uso de IA.

## Entregables

En tu repositorio de entregas, dentro de la carpeta `ae3/`:

| Archivo | Contenido |
|---|---|
| `README.md` | Tu nombre, el problema elegido y una lista de los archivos de la carpeta. |
| `datos/datos.csv` | Todos los datos recolectados, anonimizados. |
| `datos/prueba.csv` | El conjunto de prueba separado en la parte A.5. |
| `datos/diccionario.md` | El diccionario de datos y la ficha de recolección. |
| `ae3.ipynb` | El cuaderno con las partes B, C y D, **ejecutado**. |
| `informe.pdf` | El informe. |

En la tarea de Teams entrega **el enlace a tu repositorio** y **el informe en PDF**. Revisa la [guía de entregas](../../guias/entregas-en-teams.md).

> Si tu repositorio es público, comprueba que `datos.csv` no contiene ningún dato que permita identificar a una persona. Si tienes dudas, pregunta a la docente antes de subirlo.

## Uso de herramientas de IA generativa

Puedes usar asistentes de IA para resolver dudas, depurar código o revisar la redacción, con tres condiciones:

1. Incluye al final del informe una sección **«Declaración de uso de IA»** que diga qué herramienta usaste, para qué y en qué partes. Si no usaste ninguna, decláralo también.
2. **Los datos y las reglas deben ser tuyos.** No se aceptan datos generados con IA ni reglas escritas por un asistente: el objetivo es comparar *tu* conocimiento con *tus* datos.
3. Debes poder explicar cualquier parte de tu trabajo. La docente puede pedirte que lo hagas en la sesión sincrónica.

## Evaluación

Ver la [rúbrica](rubrica.md).

## Preguntas frecuentes

**¿Puedo usar un conjunto de datos público en lugar de recolectar los míos?** No como conjunto principal: la recolección y su documentación son parte de lo que se evalúa. Puedes usar uno público como experimento adicional.

**Mis clases están muy desbalanceadas (por ejemplo, 50 «a tiempo» y 10 «tarde»).** Es un resultado real y valioso. Repórtalo, analiza la precisión y la exhaustividad de la clase minoritaria y discútelo en el informe.

**Mi sistema de reglas supera a Bayes ingenuo. ¿Hice algo mal?** No necesariamente. Con pocos datos y un buen conocimiento del problema, es un resultado esperable. Explica por qué ocurre con tu curva de aprendizaje.
