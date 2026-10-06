# Recursos · AE2

| Archivo | Para qué sirve |
|---|---|
| [`ae2_instancias.py`](ae2_instancias.py) | Genera tus instancias personales a partir de tu semilla (los últimos 6 dígitos de tu documento): un mapa de 60 poblaciones con sus vías y tres consultas de rutas para la parte A.1, y 80 puntos de reparto para la parte A.2. Incluye una función para dibujar el mapa y una ruta. |

## Cómo usarlo en Google Colab

1. Descarga `ae2_instancias.py`.
2. En Colab, abre el panel **Archivos** (icono de carpeta a la izquierda) y arrastra el archivo.
3. En la primera celda de tu cuaderno escribe:

```python
from ae2_instancias import mapa_rutas, consultas_rutas, instancia_tsp, dibujar_mapa

SEMILLA = 123456          # los últimos 6 dígitos de tu documento
mapa = mapa_rutas(SEMILLA)
dibujar_mapa(mapa)
```

Colab borra los archivos subidos cuando se cierra la sesión: vuelve a subirlo cada vez que abras el cuaderno.

## Qué contiene cada instancia

- `mapa["coordenadas"]`: diccionario `{"P00": (x, y), ...}` con la posición de cada población en kilómetros.
- `mapa["vias"]`: diccionario `{"P00": {"P07": 132.4, ...}, ...}` con la longitud de cada vía. El grafo es no dirigido y conexo. Cada vía mide entre 1,05 y 1,6 veces la distancia en línea recta, así que **la distancia euclídea es una heurística admisible**.
- `consultas_rutas(SEMILLA)`: tres pares `(origen, destino)`: uno cercano, uno a distancia media y uno lejano.
- `instancia_tsp(SEMILLA)`: lista de 80 tuplas `(x, y)`. El punto 0 es el depósito.
