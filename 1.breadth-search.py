from modules.Graph import Graph
from modules.Built import createVertex, createEdges, getNumEdges


# Breadth Search based on weight algorithm
def bfs(self, fromWh, toFound):
    fail = 'falha, o nó não possui relacionamentos!'
    explored = []
    visited = []
    cities = []
    finalCost, index = [0, 0]

    visited.append(fromWh)

    while len(visited) != 0:
        city = visited.pop(0)

        if len(self.graph[city]) == 0:  # Checks if the node to be found has no relationship
            return print(fail)
        if city == toFound:
            return print(cities), print(f'The smallest cost from {fromWh} to {toFound} is {finalCost}')
        if index > 0:
            if city not in cities:
                cities.append(city)
                finalCost = finalCost + cost
            else:
                None

        for neighbour, cost in self.graph[city]:
            if neighbour not in visited:
                if neighbour not in cities:
                    cities.append(neighbour)
                    finalCost = finalCost + cost
                else:
                    None
                visited.append(neighbour)
                if neighbour == toFound:
                    return print(cities), print(f'The smallest cost from {fromWh} to {toFound} is {finalCost}')
        explored.append(city)

        index = index + 1


graph = Graph()
createVertex(graph)
createEdges(graph)

bfs(graph, 'Arad', 'Bucharest')
