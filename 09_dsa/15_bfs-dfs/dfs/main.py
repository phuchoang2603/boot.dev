class Graph:
    # def depth_first_search(self, start_vertex):
    #     visited = []
    #     stack = [start_vertex]
    #     while len(stack) > 0:
    #         current_vertex = stack.pop()
    #         if current_vertex not in visited:
    #             visited.append(current_vertex)
    #             for neigh in sorted(self.graph[current_vertex], reverse=True):
    #                 if neigh not in visited:
    #                     stack.append(neigh)
    #     return visited

    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        for neigh in sorted(self.graph[current_vertex]):
            if neigh not in visited:
                self.depth_first_search_r(visited, neigh)

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
