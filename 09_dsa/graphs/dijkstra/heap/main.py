import heapq


def dijkstra(graph, src, dest):
    distances = {node: float("inf") for node in graph}
    prev = {node: None for node in graph}
    distances[src] = 0

    queue = [(0, src)]
    visited = set()
    count = 0

    while queue:
        distance, neighbor = heapq.heappop(queue)
        if neighbor in visited:
            continue

        visited.add(neighbor)
        count += 1

        if neighbor == dest:
            break

        for node, weight in graph[neighbor].items():
            if node in visited:
                continue

            new_distance = distance + weight
            if new_distance < distances[node]:
                distances[node] = new_distance
                prev[node] = neighbor
                heapq.heappush(queue, (new_distance, node))

    if distances[dest] == float("inf"):
        return []

    path = []
    current = dest
    while current is not None:
        path.append(current)
        current = prev[current]

    path.reverse()
    return path, count


def dfs_path(graph, src, dest):
    stack = [(src, [src], 0)]
    best_path = []
    best_cost = float("inf")
    count = 0

    while stack:
        current_node, path, current_cost = stack.pop()
        count += 1

        if current_node == dest:
            if current_cost < best_cost:
                best_cost = current_cost
                best_path = path.copy()

            continue

        if current_cost >= best_cost:
            continue

        for neighbor in graph[current_node]:
            if neighbor not in path:
                new_path = path + [neighbor]
                new_cost = current_cost + graph[current_node][neighbor]
                stack.append((neighbor, new_path, new_cost))

    return best_path, count
