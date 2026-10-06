# Recursos · AE3

| Archivo | Para qué sirve |
|---|---|
| [`plantilla-diccionario-datos.md`](plantilla-diccionario-datos.md) | Plantilla del diccionario de datos y de la ficha de recolección (parte A.3). Cópiala en tu repositorio como `ae3/datos/diccionario.md` y complétala. |
| [`plantilla-consentimiento.md`](plantilla-consentimiento.md) | Texto de consentimiento para incluir al inicio de tu formulario si recolectas datos de otras personas (parte A.4). |
| [`ejemplo-datos.csv`](ejemplo-datos.csv) | Ejemplo del formato esperado para `datos.csv`: los datos de la práctica de la semana 6 (Mitchell, 1997), con una fila por ejemplo y la clase en la última columna. |

## Cómo separar el conjunto de prueba (parte A.5)

```python
import pandas as pd

datos = pd.read_csv("datos/datos.csv")
prueba = datos.sample(frac=0.30, random_state=2026)     # semilla fija: siempre la misma división
entrenamiento = datos.drop(prueba.index)
prueba.to_csv("datos/prueba.csv", index=False)
print(len(entrenamiento), "ejemplos de entrenamiento |", len(prueba), "de prueba")
```

Ejecuta esta celda **una sola vez**, antes de escribir tus reglas, y no abras `prueba.csv` hasta la parte D.
