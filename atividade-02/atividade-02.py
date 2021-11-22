from collections import defaultdict


class Grafo(object):

    def __init__(self, arestas, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)

    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo. """
        for u, v, r in arestas:
            self.adiciona_arco(u, v, r)


    def adiciona_arco(self, u, v, peso):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
        self.adj[u].add((v, peso))
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add((u, peso))
        


arestas = [('A', 'B', 1), ('B', 'C', 2), ('B', 'D', 3), ('C', 'B', 4), ('C', 'E', 5), ('D', 'A', 6), ('E', 'B', 7)]

# Cria e imprime o grafo.
grafo = Grafo(arestas, direcionado=False)
print(grafo.adj)


def bfs(grafo, vertice_fonte):
    visitados, fila = set(), [vertice_fonte]
    while fila:
        vertice = queue.pop(0)
        if vertice not in visitados:
            visitados.add(vertice)
            fila.extend(grafo[vertice] - visitados)
    return visitados

bfs(grafo, 'A')
