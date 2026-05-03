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
