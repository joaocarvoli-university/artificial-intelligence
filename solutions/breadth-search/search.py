from Graph import Graph
from Built import createVertex, createEdges


# Breadth Search based on weight algorithm
def bfs(self, fromWh, toFound):
    fail = 'falha, o nó não possui relacionamentos!'
    explored = []
    visited = []
    cities = []

    visited.append(fromWh)

    while len(visited) != 0:
        city = visited.pop(0)

        if len(self.graph[city]) == 0:  # Checks if the node to be found has no relationship
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


graph = Graph()
createVertex(graph)
createEdges(graph)

bfs(graph, 'Arad', 'Bucharest')
