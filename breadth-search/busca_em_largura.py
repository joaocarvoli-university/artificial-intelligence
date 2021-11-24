# Usando dicionários
from collections import defaultdict 

class Graph:
    def __init__(self): 
 
        #Quando você cria um defaultdict, fornece uma função usada para criar valores, nesse caso criou-se a lista
        self.graph = defaultdict(list) 

    def add_vertex(self, v):

        global vertices_no
 
        if v in self.graph:
            print(f"O vértice {v} já existe!")
        else:
            vertices_no = vertices_no + 1
            self.graph[v] = []

    # Criando as relações ponderadas
    def add_edge(self, v1, v2, weight):

        # Fazendo o check para validar o Grafo
        if v1 not in self.graph:
            print(f'O vértice {v1} não existe!')
        elif v2 not in self.graph:
            print(f'O vértice {v2} não existe!')
        else:
            temp = [v2, weight]
            temp2 = [v1, weight]
            self.graph[v1].append(temp)
            self.graph[v2].append(temp2)

    # Printando o Grafo
    def print_graph(self):

        for vertex in self.graph:
            for edges in self.graph[vertex]:
                print(f'{vertex} -> {edges[0]} peso: {edges[1]}')

    # Algoritmo de busca em largura
    def busca(self, fromWh, toFound):
        fail = 'falha, o nó não possui relacionamentos!'
        explored = []
        visited =  []
        cities =   []

        visited.append(fromWh)

        while len(visited) != 0:
            city = visited.pop(0)

            if len(g.graph[city]) == 0: # Verifica se o nó a ser encontrado não tem nenhum relacionamento
                return print(fail)
            if city == toFound:
                return print(cities)
            cities.append(city) if city not in cities else None

            for neighbour, _ in self.graph[city]:
                if neighbour not in visited:
                    cities.append(neighbour) if neighbour not in cities else None
                    visited.append(neighbour)
                    if neighbour == toFound:
                        return print(cities)
            explored.append(city)
            
        
g = Graph() 

# Armazenamento do número de vértices no Grafo
vertices_no = 0
g.add_vertex('Arad')
g.add_vertex('Zerind')
g.add_vertex('Oradea')
g.add_vertex('Sibiu')
g.add_vertex('Timisoara')
g.add_vertex('Lugoj')
g.add_vertex('Mehadia')
g.add_vertex('Drobeta')
g.add_vertex('Craiova')
g.add_vertex('Pitesti')
g.add_vertex('Rimnicu Vilcea')
g.add_vertex('Fagaras')
g.add_vertex('Giurgiu')
g.add_vertex('Bucharest')
g.add_vertex('Urziceni')
g.add_vertex('Hirsova')
g.add_vertex('Eforie')
g.add_vertex('Vaslui')
g.add_vertex('Iasi')
g.add_vertex('Neamt')

# Adicionando as arestas entre os vértices
# Structure: from / to / weight

g.add_edge('Oradea', 'Zerind', 71)
g.add_edge('Sibiu', 'Oradea', 151)

g.add_edge('Zerind', 'Arad', 75)
g.add_edge('Arad', 'Timisoara', 118)
g.add_edge('Arad', 'Sibiu', 140)
g.add_edge('Timisoara', 'Lugoj', 111)
g.add_edge('Lugoj', 'Mehadia', 70)
g.add_edge('Mehadia', 'Drobeta', 75)
g.add_edge('Drobeta', 'Craiova', 120)
g.add_edge('Craiova', 'Rimnicu Vilcea', 146)
g.add_edge('Craiova', 'Pitesti', 138)
g.add_edge('Pitesti', 'Rimnicu Vilcea', 97)
g.add_edge('Pitesti', 'Bucharest', 97)
g.add_edge('Rimnicu Vilcea', 'Sibiu', 80)
g.add_edge('Sibiu', 'Fagaras', 99)
g.add_edge('Fagaras', 'Bucharest', 211)
g.add_edge('Bucharest', 'Giurgiu', 90)
g.add_edge('Bucharest', 'Urziceni', 85)
g.add_edge('Urziceni', 'Hirsova', 98)
g.add_edge('Hirsova', 'Eforie', 86)
g.add_edge('Urziceni', 'Vaslui', 142)
g.add_edge('Vaslui', 'Iasi', 92)
g.add_edge('Iasi', 'Neamt', 87)


g.busca('Arad', 'Bucharest')