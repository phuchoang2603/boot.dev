from main import dfs, bfs, dijkstra, prim, kruskal

graph_data = {
    "A": {"B": 13, "D": 10},
    "B": {"A": 13, "C": 5, "D": 17, "E": 20, "F": 18},
    "C": {"B": 5, "E": 22, "F": 30},
    "D": {"A": 10, "B": 17},
    "E": {"B": 20, "C": 22},
    "F": {"B": 18, "C": 30},
}


def test_traversal(traversal_type, starting_at="C"):
    print(f"Running {traversal_type} from: {starting_at}")

    try:
        if traversal_type == "DFS":
            visited = dfs(graph_data, starting_at)
            expected_visited = ["C", "B", "A", "D", "F", "E"]
        else:
            visited = bfs(graph_data, starting_at)
            expected_visited = ["C", "B", "E", "F", "A", "D"]

        print(f"Result:   {visited}")
        print(f"Expected: {expected_visited}")

        if visited == expected_visited:
            print("Pass")
            return True
        else:
            print("Fail")
            return False
    except Exception as e:
        print(f"Error during {traversal_type}: {e}")
        return False


def test_pathfinding(start="D", end="E"):
    print(f"=== Pathfinding from {start} to {end} ===")

    dijkstra_path = dijkstra(graph_data, start, end)

    print(f"Dijkstra Path: {dijkstra_path}")

    expected_path = ["D", "B", "E"]

    try:
        if dijkstra_path == expected_path:
            print("Pass")
            return True
        else:
            print("Fail")
            return False
    except Exception as e:
        print(f"Error during pathfinding: {e}")
        return False


def test_mst(algo_name):
    print(f"=== Testing MST Algorithm: {algo_name} ===")

    expected_edges = [
        {"B", "C"},  # Weight 5
        {"A", "D"},  # Weight 10
        {"A", "B"},  # Weight 13
        {"B", "F"},  # Weight 18
    ]

    # Convert expected edges to a set of frozensets for easy comparison
    expected_set = {frozenset(e) for e in expected_edges}

    try:
        if algo_name == "Prim":
            result_edges = prim(graph_data, "F", limit=4)
        else:
            result_edges = kruskal(graph_data, limit=4)

        result_set = {frozenset(edge) for edge in result_edges}

        print(f"Edges Found: {list(result_edges)}")
        print(f"Expected:    {expected_edges}")

        if result_set == expected_set:
            print(f"{algo_name} Passed: Correct 4 edges found.")
            return True
        else:
            print(f"{algo_name} Failed: Edge list mismatch.")
            return False

    except Exception as e:
        print(f"Error during {algo_name}: {e}")
        return False


def main():
    passed = 0
    failed = 0

    if test_traversal("DFS"):
        passed += 1
    else:
        failed += 1

    if test_traversal("BFS"):
        passed += 1
    else:
        failed += 1

    if test_pathfinding():
        passed += 1
    else:
        failed += 1

    if test_mst("Prim"):
        passed += 1
    else:
        failed += 1

    if test_mst("Kruskal"):
        passed += 1
    else:
        failed += 1

    print("\n=================================")
    if failed == 0:
        print("Final Result: PASS")
    else:
        print("Final Result: FAIL")
    print(f"{passed} passed, {failed} failed")


if __name__ == "__main__":
    main()
