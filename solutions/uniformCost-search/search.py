from Graph import Graph
from Built import createVertex, createEdges, getNumEdges


def getCost(node):
    return node[1]


# Uniform Cost Search algorithm
def ucs(self, fromWh, toFound):
    fail = "fail, this node doesn't have any relationship!"
    explored = [fromWh]
    visited = []
    queue = [fromWh]
    results = []
    index, smallestCost, costLastNode = [0, 0, 0]

    while len(queue) != 0:
        city = queue.pop(0)
        if len(self.graph[city]) == 0:  # Checks if the node to be found has no relationship
            return print(fail)
        for neighbour in self.graph[city]:
            # from the second iteration sum a cost of expanded node
            if (index > 0) and (neighbour[0] not in explored):
                neighbour[1] = neighbour[1] + costLastNode  # updating the cost of actual node with its parent
                visited.append(neighbour)
            elif index == 0:
                visited.append(neighbour)

        # Checking if the node to be explored has already been visited
        for node in visited:
            smallestCost = sorted(visited, key=getCost)[0]
            # Getting the element name on list that has the smallest cost
            if node[0] == toFound:  # Checking if the actual node is what We're searching for
                results.append(node)
        visited.pop(visited.index(smallestCost))  # Popping just the element that has the smallest cost
        explored.append(smallestCost[0])
        queue.append(smallestCost[0])  # expanding based on the lowest cost node

        costLastNode = smallestCost[1]  # getting the cost of the parent or of the node that will be expanded

        index = index + 1
        if index == getNumEdges():
            return print(f'The smallest cost from {fromWh} to {sorted(results, key=getCost)[0][0]} is {sorted(results, key=getCost)[0][1]}')


graph = Graph()
createVertex(graph)
createEdges(graph)

ucs(graph, 'Arad', 'Bucharest')
