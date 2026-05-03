import heapq


def dfs(graph: dict[str, dict[str, int]], start_node: str) -> list[str]:
    visited = []
    stack = [start_node]

    while len(stack) > 0:
        current = stack.pop()

        if current not in visited:
            visited.append(current)

            neighbors = graph.get(current, {})
            for neigh in sorted(
                neighbors.keys(), key=lambda node: neighbors[node], reverse=True
            ):
                if neigh not in visited:
                    stack.append(neigh)

    return visited


def bfs(graph: dict[str, dict[str, int]], start_node: str) -> list[str]:
    visited = []
    queue = [start_node]

    while len(queue) > 0:
        current = queue.pop(0)
        visited.append(current)

        neighbors = graph.get(current, {})
        for neigh in sorted(neighbors.keys(), key=lambda node: neighbors[node]):
            if neigh not in visited and neigh not in queue:
                queue.append(neigh)

    return visited


def dijkstra(graph: dict[str, dict[str, int]], start, end):
    distances = {}
    prev = {}
    for node in graph:
        distances[node] = 0 if node == start else float("inf")
        prev[node] = None

    visited = set()

    queue = [(0, start)]

    while queue:
        distance, current = heapq.heappop(queue)
        if current in visited:
            continue

        visited.add(current)

        if current == end:
            break

        for neigh, weight in graph[current].items():
            if neigh in visited:
                continue

            new_dist = distance + weight
            if new_dist < distances[neigh]:
                distances[neigh] = new_dist
                prev[neigh] = current
                heapq.heappush(queue, (new_dist, neigh))

    if distances[end] == float("inf"):
        return []

    path = []
    current = end

    while current is not None:
        path.insert(0, current)
        current = prev[current]

    return path


def prim(graph, start, limit):
    costs = {}
    prev = {}
    for node in graph:
        costs[node] = 0 if node == start else float("inf")
        prev[node] = None

    visited = set()
    mst_edges = []
    queue = [(0, start)]

    while queue and len(mst_edges) < limit:
        _, current = heapq.heappop(queue)  # <--- LOG V operation

        if current in visited:
            continue
        visited.add(current)

        if prev[current] is not None:
            mst_edges.append((prev[current], current))

        for neigh, weight in graph[current].items():  # <--- This runs E times total
            if neigh in visited:
                continue

            if weight < costs[neigh]:
                costs[neigh] = weight
                prev[neigh] = current
                heapq.heappush(queue, (weight, neigh))  # <--- LOG V operation

    return mst_edges


class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False


def kruskal(graph, limit=None):
    # 1. Extract and Sort Edges - Complexity: O(E log E)
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            if u < v:  # Ensure each edge is only added once
                edges.append((weight, u, v))

    edges.sort()

    # 2. Initialize Union-Find - Complexity: O(V)
    nodes = list(graph.keys())
    uf = UnionFind(nodes)
    mst_edges = []

    # 3. Process Edges - Complexity: O(E * α(V))
    # (α is the Inverse Ackermann function, which is nearly constant)
    for weight, u, v in edges:
        if limit is not None and len(mst_edges) >= limit:
            break

        if uf.union(u, v):
            mst_edges.append((u, v))

    return mst_edges
