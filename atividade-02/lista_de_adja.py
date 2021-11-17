# Usando dicionários

# Criando o vértice
def add_vertex(v):
    global graph
    global vertices_no
    global cost

    if v in graph:
        print(f"O vértice {v} já existe!")
    else:
        vertices_no = vertices_no + 1
        graph[v] = []

# Criando as relações ponderadas
def add_edge(v1, v2, weight):
    global graph
    # Fazendo o check para validar o Grafo
    if v1 not in graph:
        print(f'O vértice {v1} não existe!')
    elif v2 not in graph:
        print(f'O vértice {v2} não existe!')
    else:
        temp = [v2, weight]
        graph[v1].append(temp)

# Printando o Grafo
def print_graph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print(f'{vertex} -> {edges[0]} peso: {edges[1]}')


# Casos de teste

graph = {}
# Armazenamento do número de vértices no Grafo
vertices_no = 0
add_vertex('Zerind')
add_vertex('Oradea')
add_vertex('Sibiu')
add_vertex('Arad')
add_vertex('Timisoara')
add_vertex('Lugoj')
add_vertex('Mehadia')
add_vertex('Drobeta')
add_vertex('Craiova')
add_vertex('Pitesti')
add_vertex('Rimnicu Vilcea')
add_vertex('Fagaras')
add_vertex('Giurgiu')
add_vertex('Bucharest')
add_vertex('Urziceni')
add_vertex('Hirsova')
add_vertex('Eforie')
add_vertex('Vaslui')
add_vertex('Iasi')
add_vertex('Neamt')


# Adicionando as arestas entre os vértices
# Structure: from / to / weight

add_edge('Oradea', 'Zerind', 71)
add_edge('Zerind', 'Arad', 75)
add_edge('Arad', 'Timisoara', 118)
add_edge('Arad', 'Sibiu', 140)
add_edge('Timisoara', 'Lugoj', 111)
add_edge('Lugoj', 'Mehadia', 70)
add_edge('Mehadia', 'Drobeta', 75)
add_edge('Drobeta', 'Craiova', 120)
add_edge('Craiova', 'Rimnicu Vilcea', 146)
add_edge('Craiova', 'Petesti', 138)
add_edge('Pitesti', 'Rimnicu Vilcea', 97)
add_edge('Pitesti', 'Bucharest', 97)
add_edge('Rimnicu Vilcea', 'Sibiu', 80)
add_edge('Sibiu', 'Oradea', 151)
add_edge('Sibiu', 'Fagaras', 99)
add_edge('Fagaras', 'Bucharest', 211)
add_edge('Bucharest', 'Giurgiu', 90)
add_edge('Bucharest', 'Urziceni', 85)
add_edge('Urziceni', 'Hirsova', 98)
add_edge('Hirsova', 'Eforie', 86)
add_edge('Urziceni', 'Vaslui', 142)
add_edge('Vaslui', 'Iasi', 92)
add_edge('Iasi', 'Neamt', 87)

print_graph()

# print ("Internal representation: ", graph)


# Busca em largura

fail = 'A borda está vazia!'
explored = []
#def widthSearch():
#    # list(graph.values())[0][0][0] -> equivale ao nome da cidade
#    # list(graph.values())[0][0][0] -> equivale ao peso da aresta
#    first = list(graph.values())[0][0][0]
#    while True:
#        if v1 or v2 not in graph:
#            return fail

