"""Generador de instancias personales para la Actividad Evaluativa 2.

Cada estudiante usa como semilla los últimos 6 dígitos de su documento de identidad.
La misma semilla produce siempre las mismas instancias, así que la docente puede
reproducir tus resultados.

Uso en Colab o Jupyter (con este archivo en la misma carpeta que el cuaderno):

    from ae2_instancias import mapa_rutas, consultas_rutas, instancia_tsp, dibujar_mapa

    SEMILLA = 123456                     # últimos 6 dígitos de tu documento
    mapa = mapa_rutas(SEMILLA)           # parte A.1
    consultas = consultas_rutas(SEMILLA) # tres pares (origen, destino)
    puntos = instancia_tsp(SEMILLA)      # parte A.2
"""

import math
import random

__all__ = ["mapa_rutas", "consultas_rutas", "instancia_tsp", "dibujar_mapa"]


def mapa_rutas(semilla, n=60, vecinos=4, lado=1000.0):
    """Mapa de n poblaciones en un cuadrado de lado × lado km.

    Devuelve un diccionario con:
      - "coordenadas": {nombre: (x, y)}
      - "vias": {nombre: {vecino: km}}   (grafo no dirigido y conexo)

    Cada población se une con sus `vecinos` más cercanas. La longitud de cada vía es
    la distancia en línea recta multiplicada por un factor entre 1,05 y 1,6 que
    representa las curvas de la carretera, de modo que la distancia euclídea es
    siempre una heurística admisible.
    """
    rng = random.Random(semilla)
    nombres = [f"P{i:02d}" for i in range(n)]
    coords = {p: (rng.uniform(0, lado), rng.uniform(0, lado)) for p in nombres}

    def d(a, b):
        return math.dist(coords[a], coords[b])

    vias = {p: {} for p in nombres}

    def unir(a, b):
        if b not in vias[a]:
            km = round(d(a, b) * rng.uniform(1.05, 1.6), 1)
            vias[a][b] = km
            vias[b][a] = km

    for a in nombres:
        for b in sorted((x for x in nombres if x != a), key=lambda x: d(a, x))[:vecinos]:
            unir(a, b)

    # Garantiza la conexidad uniendo componentes por su par de poblaciones más cercano
    def componentes():
        vistos, comps = set(), []
        for p in nombres:
            if p in vistos:
                continue
            pila, comp = [p], set()
            while pila:
                x = pila.pop()
                if x not in comp:
                    comp.add(x)
                    pila.extend(vias[x])
            vistos |= comp
            comps.append(comp)
        return comps

    comps = componentes()
    while len(comps) > 1:
        a, b = min(((x, y) for x in comps[0] for y in comps[1]), key=lambda par: d(*par))
        unir(a, b)
        comps = componentes()

    return {"coordenadas": coords, "vias": vias}


def consultas_rutas(semilla, mapa=None):
    """Tres pares (origen, destino) de dificultad creciente: cercano, medio y lejano."""
    mapa = mapa or mapa_rutas(semilla)
    coords = mapa["coordenadas"]
    rng = random.Random(semilla + 1)
    nombres = sorted(coords)
    pares = [(a, b) for a in nombres for b in nombres if a < b]
    pares.sort(key=lambda p: math.dist(coords[p[0]], coords[p[1]]))
    n = len(pares)
    tercios = [pares[: n // 3], pares[n // 3: 2 * n // 3], pares[-n // 10:]]
    return [rng.choice(t) for t in tercios]


def instancia_tsp(semilla, n=80, lado=1000.0):
    """Lista de n puntos (x, y). El punto 0 es el depósito donde empieza y termina el recorrido."""
    rng = random.Random(semilla * 7 + 3)
    return [(round(rng.uniform(0, lado), 1), round(rng.uniform(0, lado), 1)) for _ in range(n)]


def dibujar_mapa(mapa, ruta=None, titulo="Mapa de rutas"):
    """Dibuja el mapa y, si se indica, una ruta (lista de nombres) resaltada."""
    import matplotlib.pyplot as plt

    coords, vias = mapa["coordenadas"], mapa["vias"]
    plt.figure(figsize=(7, 7))
    for a in vias:
        for b in vias[a]:
            if a < b:
                plt.plot(*zip(coords[a], coords[b]), color="#bbbbbb", lw=0.8, zorder=1)
    xs, ys = zip(*coords.values())
    plt.scatter(xs, ys, s=12, zorder=2)
    for p, (x, y) in coords.items():
        plt.annotate(p, (x, y), fontsize=6, xytext=(2, 2), textcoords="offset points")
    if ruta:
        plt.plot(*zip(*(coords[p] for p in ruta)), color="crimson", lw=2.2, zorder=3)
    plt.title(titulo)
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    m = mapa_rutas(123456)
    print("Poblaciones:", len(m["coordenadas"]),
          "| vías:", sum(len(v) for v in m["vias"].values()) // 2)
    print("Consultas:", consultas_rutas(123456, m))
    print("Primeros puntos del TSP:", instancia_tsp(123456)[:3])
