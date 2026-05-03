def get_path(dest, predecessors):
    visited = []
    current = dest
    while current is not None:
        visited.insert(0, current)
        current = predecessors.get(current)
    return visited
