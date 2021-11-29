class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        global vertices_no
        vertices_no = 0

        if v in self.graph:
            print(f"The vertex {v} already was created!")
        else:
            vertices_no = vertices_no + 1
            self.graph[v] = []

    def add_edge(self, relationship):
        v1, v2, weight = relationship
        if v1 not in self.graph:
            print(f'There is no {v1} vertex!')
        elif v2 not in self.graph:
            print(f'There is no {v2} vertex!')
        else:
            temp = [v2, weight]
            temp2 = [v1, weight]
            self.graph[v1].append(temp)
            self.graph[v2].append(temp2)

