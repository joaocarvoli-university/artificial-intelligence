from collections import OrderedDict
from modules.Graph import Graph
from modules.Built import createVertex, createEdges, getNumEdges


def getCost(node):
    return node[1]


# Uniform Cost Search algorithm
def ucs(self, fromWh, toFound):
    fail = "fail, this node doesn't have any relationship!"
    explored = [fromWh]
    visited = []
    queue = [fromWh]
    index, smallestCost, costLastNode = [0, 0, 0]

    while len(queue) != 0:
        city = queue.pop(0)
        if len(self.graph[city]) == 0:  # Checks if the node to be found has no relationship
            return print(fail)
        if city == toFound:
            print(list(OrderedDict.fromkeys(explored)))
            return print(f'The smallest cost from {fromWh} to {smallestCost[0]} is {smallestCost[1]}')

        for neighbour in self.graph[city]:
            # from the second iteration sum a cost of expanded node
            if (index > 0) and (neighbour[0] not in explored):
                neighbour[1] = neighbour[1] + costLastNode  # updating the cost of actual node with its parent
                visited.append(neighbour)
            elif index == 0:
                visited.append(neighbour)

        
        smallestCost = sorted(visited, key=getCost)[0] # Getting the element name on list that has the smallest cost
        visited.pop(visited.index(smallestCost))  # Popping just the element that has the smallest cost
        explored.append(smallestCost[0])
        queue.append(smallestCost[0])  # expanding based on the lowest cost node

        costLastNode = smallestCost[1]  # getting the cost of the parent or of the node that will be expanded

        index = index + 1


graph = Graph()
createVertex(graph)
createEdges(graph)

ucs(graph, 'Zerind', 'Bucharest')
