def next_nearest_node(distances, unvisited):
    closest = None
    min_dist = float("inf")

    for node in unvisited:
        if distances[node] < min_dist:
            min_dist = distances[node]
            closest = node

    return closest
