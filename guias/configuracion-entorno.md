# Configuración del entorno

Todas las prácticas del curso son cuadernos de Jupyter (`.ipynb`) que funcionan en Google Colab sin instalar nada. Si prefieres trabajar en tu computador, usa la opción 2.

## Opción 1: Google Colaboratory (recomendada)

1. Entra a https://colab.research.google.com con tu cuenta de Google.
2. Elige *Archivo → Subir cuaderno* y selecciona el `.ipynb` de la carpeta `practicas/` de la semana.
3. Ejecuta las celdas en orden con *Mayús + Enter*.

Colab ya trae todas las librerías que usa el curso. Recuerda que los archivos que subes al panel *Archivos* se borran al cerrar la sesión (por ejemplo, `ae2_instancias.py` de la Actividad Evaluativa 2): vuelve a subirlos cada vez.

## Opción 2: entorno local

- Python 3.11 o superior.
- Editor: Visual Studio Code con las extensiones de Python y Jupyter, o Jupyter Notebook.
- Librerías del curso:

| Librería | Semanas | Para qué |
|---|:-:|---|
| `numpy` | 5 a 8 | Cálculo numérico (lógica difusa, redes neuronales) |
| `matplotlib` | 3 a 7 | Gráficas |
| `pandas` | AE1, AE3 | Tablas de resultados y lectura de archivos CSV |
| `scikit-learn` | 6 y 7 | Comparación con implementaciones de referencia, *k*-medias y redes neuronales |

Instalación en una terminal:

```bash
python -m venv .venv
source .venv/bin/activate          # En Windows: .venv\Scripts\activate
pip install numpy matplotlib pandas scikit-learn jupyter
jupyter notebook
```

Las semanas 1 y 2 solo usan la librería estándar de Python. La sección 4 de la práctica de la semana 6 descarga un conjunto de datos de internet; el resto de los cuadernos funciona sin conexión.
