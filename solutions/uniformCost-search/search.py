from Graph import Graph
from Built import createVertex, createEdges


def getCost(node):
    return node[1]


# Uniform Cost Search algorithm
def ucs(self, fromWh, toFound):
    fail = 'falha, o nó não possui relacionamentos!'
    explored = [[fromWh, 0]]
    visited = []
    queue = [fromWh]
    index = 0
    costLastNode = 0

    while len(queue) != 0:
        print(queue[0])
        city = queue.pop(0)
        if len(self.graph[city]) == 0:  # Checks if the node to be found has no relationship
            return print(fail)

        for neighbour in self.graph[city]:
            if index > 0:
                neighbour[1] = neighbour[1] + costLastNode  # updating the cost of actual node with its parent
                visited.append(neighbour)
            else:
                visited.append(neighbour)

        smallestCost = sorted(visited, key=getCost)[0]
        # Ordering based on smallest cost and ignoring the first list ...
        # ... because  We come from there
        visited.pop(0)  # Popping just the first element
        queue.append(smallestCost)  # expanding based on the lowest cost node
        costLastNode = smallestCost[1]  # getting the cost of the parent or of the node that will be expanded
        explored.append(smallestCost)

        index = index + 1
        if index == 1:
            return print('to test')


graph = Graph()
createVertex(graph)
createEdges(graph)

ucs(graph, 'Arad', 'Bucharest')
