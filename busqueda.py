from grafos import Grafo

def dfs(grafo, inicio, destino, visitados=None, camino=None):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []
    visitados.add(inicio)
    camino.append(inicio)
    if inicio == destino:
        return camino
    for vecino, _ in grafo.adyacencias.get(inicio, []):
        if vecino not in visitados:
            resultado = dfs(grafo, vecino, destino, visitados, camino)
            if resultado:
                return resultado
    camino.pop()
    return None

def bfs(grafo, inicio, destino):
    visitados = set()
    cola = [[inicio]]
    if inicio == destino:
        return [inicio]
    while cola:
        camino = cola.pop(0)
        nodo = camino[-1]
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, _ in grafo.adyacencias.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                if vecino == destino:
                    return nuevo_camino
                cola.append(nuevo_camino)
    return None
