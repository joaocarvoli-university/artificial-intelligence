from modules.Graph import Graph
from modules.Built import createVertex, createEdges, getNumEdges


# This heuristic is about the smallest cost way from any city to Bucharest
heuristic = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77,
             'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
             'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
             'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}


def getHeuristic(city):
    return heuristic[city]


def getCost(node):
    return node[1]


def greedy(self, fromWh, toFound):
    fail = "fail, this node doesn't have any relationship!"
    explored = [fromWh]
    visited = []
    queue = [fromWh]
    index, smallestCost, costLastNode = [0, 0, 0]

    while len(queue) != 0:
        city = queue.pop(0)
        if len(self.graph[city]) == 0:
            return print(fail)
        if city == toFound:
            return print(f'The smallest cost from {fromWh} to {smallestCost[0]} is {smallestCost[1]}')

        for neighbour in self.graph[city]:
            if (index > 0) and (neighbour[0] not in explored):
                neighbour[1] = getHeuristic(neighbour[0]) + costLastNode
                visited.append(neighbour)
            elif index == 0:
                neighbour[1] = getHeuristic(neighbour[0])
                visited.append(neighbour)

        for node in visited:
            smallestCost = sorted(visited, key=getCost)[0]
        visited.pop(visited.index(smallestCost))
        explored.append(smallestCost[0])
        queue.append(smallestCost[0])

        costLastNode = smallestCost[1]

        index = index + 1


graph = Graph()
createVertex(graph)
createEdges(graph)

greedy(graph, 'Arad', 'Bucharest')

