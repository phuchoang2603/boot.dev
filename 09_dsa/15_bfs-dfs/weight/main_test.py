from main import dfs, bfs

graph_data = {
    "A": {"B": 13, "D": 10},
    "B": {"A": 13, "C": 5, "D": 17, "E": 20, "F": 18},
    "C": {"B": 5, "E": 22, "F": 30},
    "D": {"A": 10, "B": 17},
    "E": {"B": 20, "C": 22},
    "F": {"B": 18, "C": 30},
}

# format: (graph, start_node, expected_output, type_label)
run_cases = [
    (graph_data, "C", ["C", "B", "A", "D", "F", "E"], "DFS"),
    (graph_data, "C", ["C", "B", "E", "F", "A", "D"], "BFS"),
]

submit_cases = run_cases


def test(graph_dict, starting_at, expected_visited, traversal_type):
    print("=================================")
    print(f"Running {traversal_type} from: {starting_at}")
    print("Rule: Smallest edge weight first")
    print("---------------------------------")

    try:
        if traversal_type == "DFS":
            visited = dfs(graph_dict, starting_at)
        else:
            visited = bfs(graph_dict, starting_at)

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


def main():
    passed = 0
    failed = 0

    for test_case in submit_cases:
        if test(*test_case):
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
