from Graph import Graph
from Built import createVertex, createEdges


def getCost(node):
    return node[1]


# Uniform Cost Search algorithm
def ucs(self, fromWh, toFound):
    fail = "fail, this node doesn't have any relationship!"
    explored = [[fromWh, 0]]
    visited = []
    queue = [fromWh]
    index, smallestCost, costLastNode = [0, 0, 0]

    while len(queue) != 0:
        city = queue.pop(0)
        if len(self.graph[city]) == 0:  # Checks if the node to be found has no relationship
            return print(fail)

        for neighbour in self.graph[city]:
            # from the second iteration sum a cost of expanded node
            if index > 0:
                neighbour[1] = neighbour[1] + costLastNode  # updating the cost of actual node with its parent
                visited.append(neighbour)
            else:
                visited.append(neighbour)
        # Checking if the node to be explored has already been visited
        for node in visited:
            if (node not in explored) and (node == sorted(visited, key=getCost)[0]):
                smallestCost = node  # Getting the element name on list that has the smallest cost

        # ERROR! Backing to arad
        print(f'visited: {visited}')
        visited.pop(visited.index(smallestCost))  # Popping just the element that has the smallest cost
        explored.append(smallestCost)
        queue.append(smallestCost[0])  # expanding based on the lowest cost node

        print(f'queue: {queue}')

        costLastNode = smallestCost[1]  # getting the cost of the parent or of the node that will be expanded

        index = index + 1
        # ! this return is for test
        if index == 5:
            return print('close')


graph = Graph()
createVertex(graph)
createEdges(graph)

ucs(graph, 'Arad', 'Bucharest')
