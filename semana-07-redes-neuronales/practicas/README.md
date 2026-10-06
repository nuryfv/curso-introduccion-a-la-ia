# Práctica · Semana 7: Redes neuronales por dentro y por fuera

**Tipo:** práctica autónoma, no calificable
**Tiempo estimado:** 3 horas
**Archivo:** [`practica-07-redes-neuronales.ipynb`](practica-07-redes-neuronales.ipynb) (parte A)
**Herramientas:** Google Colab, TensorFlow Playground y Teachable Machine; ver [`complementos/herramientas.md`](../complementos/herramientas.md)
**Relación con el capítulo:** secciones 7.1 a 7.8

## Propósito

Entender las redes neuronales desde dos ángulos: **por dentro**, programándolas desde cero, y **por fuera**, usándolas como lo haría una persona que no programa, para observar cómo aprenden y por qué fallan.

| Parte | Herramienta | Qué haces | Tiempo |
|---|---|---|:-:|
| A | Cuaderno de Python | Neurona de McCulloch y Pitts, perceptrón, red multicapa con retropropagación, red de Hopfield y clasificador de dígitos | 1 h 45 min |
| B | TensorFlow Playground | Experimentar con capas, neuronas, características, activaciones y sobreajuste | 30 min |
| C | Teachable Machine | Entrenar tu propio clasificador de imágenes y provocar sus errores | 45 min |

Crea un archivo `practica-semana-07.md` (o un documento de texto) para registrar las respuestas de las partes B y C. Llévalo a la sesión sincrónica junto con el cuaderno.

---

## Parte A. Redes neuronales en Python (1 h 45 min)

Abre el cuaderno [`practica-07-redes-neuronales.ipynb`](practica-07-redes-neuronales.ipynb) en Google Colab (*Archivo → Subir cuaderno*) y resuelve los ejercicios 1 a 5. Todas las celdas se probaron con Python 3 y usan librerías que Colab trae instaladas. Las cifras que cita el capítulo se obtuvieron con este cuaderno.

## Parte B. TensorFlow Playground (30 min)

Entra a **TensorFlow Playground** (https://playground.tensorflow.org). Arriba eliges la tasa de aprendizaje (*Learning rate*) y la activación (*Activation*); a la izquierda, el conjunto de datos, el ruido (*Noise*) y la proporción de datos de entrenamiento; en el centro, las características de entrada (*Features*) y las capas ocultas; a la derecha ves la frontera de decisión y las pérdidas de entrenamiento (*Training loss*) y de prueba (*Test loss*).

**B.1 El círculo y la capa oculta.**
1. Elige el conjunto **Circle** (el círculo), deja solo las características *X₁* y *X₂* y **elimina todas las capas ocultas**. Pulsa ▶. ¿Puede la red separar las clases? ¿Por qué? (Relaciónalo con la sección 7.2.3.)
2. Añade **una capa oculta con 2 neuronas**, luego con 3 y luego con 4. ¿A partir de cuántas neuronas aparece una frontera cerrada?
3. Vuelve a **cero capas ocultas**, pero activa las características *X₁²* y *X₂²*. ¿Qué pasa ahora? ¿Qué te dice eso sobre la diferencia entre diseñar características a mano (semana 6) y dejar que la red las aprenda (sección 7.5.1)?

**B.2 La espiral.**
1. Elige el conjunto **Spiral** (la espiral) con *X₁* y *X₂*. Busca la red **más pequeña** que logre una pérdida de prueba menor que 0,1. Anota su arquitectura, la activación y la tasa de aprendizaje.
2. Con esa red, cambia la tasa de aprendizaje a 3 y luego a 0,0001. Describe lo que ocurre.

**B.3 El sobreajuste.**
1. Elige el conjunto **Gaussian** o **Circle**, sube el ruido a 50 y baja la proporción de datos de entrenamiento al 10 %. Usa una red grande (por ejemplo, 3 capas de 8 neuronas).
2. Entrena durante unas 1.000 épocas. Compara la pérdida de entrenamiento con la de prueba. ¿Qué observas en la forma de la frontera?
3. Activa la regularización **L2** con una tasa de 0,01 y vuelve a entrenar. ¿Cambia la frontera? ¿Y la diferencia entre las dos pérdidas?

| Experimento | Configuración | Pérdida de entrenamiento | Pérdida de prueba | Observación |
|---|---|:-:|:-:|---|
| B.1.1 | Circle, sin capas ocultas | | | |
| B.1.3 | Circle, sin capas, con *X₁²* y *X₂²* | | | |
| B.2.1 | Spiral, tu red más pequeña | | | |
| B.3.2 | Ruido 50, 10 % de entrenamiento | | | |
| B.3.3 | Lo mismo, con L2 | | | |

## Parte C. Teachable Machine (45 min)

Entra a **Teachable Machine** (https://teachablemachine.withgoogle.com), pulsa *Comenzar* y elige **Proyecto de imagen → Modelo de imagen estándar**. Las imágenes se procesan en tu navegador; aun así, **no grabes a otras personas sin su permiso**.

**C.1 Entrena un clasificador.**
1. Crea **tres clases** con objetos que tengas a mano (por ejemplo, un esfero, una taza y tu celular) o con gestos de la mano (piedra, papel y tijera).
2. Captura **al menos 40 imágenes por clase** con la cámara, moviendo el objeto, cambiando el ángulo y la distancia.
3. Pulsa *Entrenar modelo* y prueba el modelo en vivo en la vista previa. Anota la confianza que muestra para cada clase.

**C.2 Provoca sus errores.**
1. Crea un **nuevo proyecto** con las mismas clases, pero esta vez captura todas las imágenes de una clase **con un mismo fondo y una misma luz**, y las de otra clase con un fondo distinto.
2. Entrena y prueba cada objeto **sobre el fondo equivocado**. ¿Qué aprendió realmente el modelo: el objeto o el fondo?
3. Prueba el modelo con un objeto que **no pertenece** a ninguna clase. ¿Qué responde? ¿Con qué confianza?

| Prueba | Clase real | Predicción | Confianza | ¿Por qué crees que ocurrió? |
|---|---|---|:-:|---|
| Objeto 1, fondo de entrenamiento | | | | |
| Objeto 1, fondo distinto | | | | |
| Objeto que no pertenece a ninguna clase | | | | |

**C.3 Analiza tu modelo como una persona diseñadora.**
Responde las seis preguntas de la tabla 7.4 del capítulo para un producto imaginario que use tu clasificador (por ejemplo, una aplicación que ayuda a una persona con baja visión a identificar objetos). ¿Qué cambiarías en los datos y en la interfaz para que el producto fuera confiable?

---

## Para la sesión sincrónica

Lleva tu cuaderno ejecutado, tus tablas de las partes B y C y tus respuestas. Compartiremos los modelos de Teachable Machine que «aprendieron el fondo» y discutiremos qué nos dicen sobre los datos de entrenamiento, el tema de la semana 8.

> Esta práctica no se califica, pero te prepara para la [Actividad Evaluativa 4](../../actividades-evaluativas/ae4-proyecto-integrador/), en la que construirás un prototipo con una red neuronal o un modelo entrenado con una herramienta como Teachable Machine.
