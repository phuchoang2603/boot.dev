class Graph:
    def unconnected_vertices(self):
        zero_conn = []

        for vertices in self.graph:
            if len(self.graph[vertices]) == 0:
                zero_conn.append(vertices)

        return zero_conn

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()
