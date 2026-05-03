def dijkstra(graph, src, dest):
    unvisited = set()
    predecessors = {}
    distances = {}

    for node in graph:
        unvisited.add(node)
        if node == src:
            distances[node] = 0
            continue
        distances[node] = float("inf")

    while len(unvisited) != 0:
        nearest = next_nearest_node(distances, unvisited)
        unvisited.remove(nearest)
        if nearest == dest:
            return get_path(nearest, predecessors)

        for neighbor in graph[nearest]:
            if neighbor not in unvisited:
                continue
            total_dist = distances[nearest] + graph[nearest][neighbor]
            if total_dist < distances[neighbor]:
                distances[neighbor] = total_dist
                predecessors[neighbor] = nearest


# Don't touch below this line


def get_path(dest, predecessors):
    path = []
    pred = dest

    while pred is not None:
        path.append(pred)
        pred = predecessors.get(pred, None)

    path.reverse()
    return path


def next_nearest_node(distances, unvisited):
    min_dist = float("inf")
    next_nearest = None

    for v in unvisited:
        distance_so_far = distances[v]
        if distance_so_far < min_dist:
            min_dist = distance_so_far
            next_nearest = v

    return next_nearest
