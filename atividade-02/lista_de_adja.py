# Usando dicionários

# Criando o vértice
def add_vertex(v):
    global graph
    global vertices_no

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

# Adicionando as arestas entre os vértices
# Structure: from / to / weight

add_edge('Zerind', 'Oradea', 1)
add_edge('Zerind', 'Sibiu', 1)
add_edge('Arad', 'Oradea', 1)
add_edge('Oradea', 'Sibiu', 1)
add_edge('Sibiu', 'Arad', 1)

print_graph()

print ("Internal representation: ", graph)