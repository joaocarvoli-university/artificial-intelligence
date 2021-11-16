from collection import defaultdict


class Grafo:
    def __init__(self, vertices ):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        # lógica de grafo não direcionado
        self.grafo[u - 1].append([v, peso]) # de u para v
        self.grafo[v - 1].append([u, peso]) # de v para u

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end=' ')
            for j in self.grafo[i]:
                print(f' {j} ->', end=' ')
            print('')

g = Grafo(4)

# g.adiciona_aresta(1,2,3) - Grafo de 1 para 2 e 2 para 1 com peso 3
g.adiciona_aresta(1,2, 5)
g.adiciona_aresta(1,3, 7)
g.adiciona_aresta(1,4, 6)
g.adiciona_aresta(2,3, 9)



#g.adiciona_aresta('Zerind', 'Oradea')
#g.adiciona_aresta('Oradea', 'Sibiu')
#g.adiciona_aresta('Zerind', 'Arad')
#g.adiciona_aresta('Arad', 'Sibiu')

g.mostra_lista()