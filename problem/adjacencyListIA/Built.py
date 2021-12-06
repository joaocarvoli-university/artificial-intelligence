list = ['Arad', 'Zerind', 'Oradea', 'Sibiu', 'Timisoara',
        'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Pitesti',
        'Rimnicu Vilcea', 'Fagaras', 'Giurgiu', 'Bucharest',
        'Urziceni', 'Hirsova', 'Eforie', 'Vaslui', 'Iasi', 'Neamt']

edges = [['Oradea', 'Zerind'], ['Sibiu', 'Oradea'], ['Zerind', 'Arad'],
         ['Arad', 'Timisoara'], ['Arad', 'Sibiu'], ['Timisoara', 'Lugoj'],
         ['Lugoj', 'Mehadia'], ['Mehadia', 'Drobeta'], ['Drobeta', 'Craiova'],
         ['Craiova', 'Rimnicu Vilcea'], ['Craiova', 'Pitesti'], ['Pitesti', 'Rimnicu Vilcea'],
         ['Pitesti', 'Bucharest'], ['Rimnicu Vilcea', 'Sibiu'], ['Sibiu', 'Fagaras'],
         ['Fagaras', 'Bucharest'], ['Bucharest', 'Giurgiu'], ['Bucharest', 'Urziceni'],
         ['Urziceni', 'Hirsova'], ['Hirsova', 'Eforie'], ['Urziceni', 'Vaslui'],
         ['Vaslui', 'Iasi'], ['Iasi', 'Neamt']]
print(len(edges))

weights = [71, 151, 75, 118, 140, 111, 70, 75, 120, 146, 138, 97, 97, 80, 99, 211, 90, 85, 98, 86, 142, 92, 87]


def getVertexList():
    return list


def createVertex(g):
    for vertex in getVertexList():
        g.add_vertex(vertex)
    return g


def createEdges(g):
    for i, relationship in enumerate(edges):
        relationship.append(weights[i])
        g.add_edge(relationship)
    return g



