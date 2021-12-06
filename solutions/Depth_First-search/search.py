from Graph import Graph
from Built import createVertex, createEdges


# Deep Search 
def deep_search(self, origem, destino):
    stack = [[origem]] 
    visited = [] 

    while (len(stack) != 0):
        path = stack.pop(0) 
        node = path[-1]

        if node == destino:
            return print("caminho igual a: ", path)

        for child , _ in self.graph[node]:
            if child not in visited:
                new_path = path + [child]
                stack.insert(0, new_path)
                visited.append(child)


graph = Graph()
createVertex(graph)
createEdges(graph)

deep_search(graph, 'Arad', 'Bucharest')