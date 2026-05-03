from main import dijkstra

TestCase = tuple[dict[str, dict[str, int]], str, str, list[str]]

run_cases: list[TestCase] = [
    (
        {
            "Minas Tirith": {"Isengard": 4, "Gondor": 1},
            "Isengard": {"Minas Tirith": 4, "Bree": 3, "Mirkwood": 8},
            "Gondor": {"Minas Tirith": 1, "Bree": 2, "Misty Mountains": 6},
            "Bree": {"Gondor": 2, "Isengard": 3, "Mirkwood": 4},
            "Mirkwood": {"Bree": 4, "Isengard": 8, "Lothlorien": 2},
            "Misty Mountains": {"Gondor": 6, "Lothlorien": 8},
            "Lothlorien": {"Misty Mountains": 8, "Mirkwood": 2},
        },
        "Minas Tirith",
        "Lothlorien",
        ["Minas Tirith", "Gondor", "Bree", "Mirkwood", "Lothlorien"],
    ),
    (
        {
            "Minas Tirith": {"Isengard": 4, "Gondor": 1},
            "Isengard": {"Minas Tirith": 4, "Bree": 3, "Mirkwood": 8},
            "Gondor": {"Minas Tirith": 1, "Bree": 2, "Misty Mountains": 6},
            "Bree": {"Gondor": 2, "Isengard": 3, "Mirkwood": 4},
            "Mirkwood": {"Bree": 4, "Isengard": 8, "Lothlorien": 2},
            "Misty Mountains": {"Gondor": 6, "Lothlorien": 8},
            "Lothlorien": {"Misty Mountains": 8, "Mirkwood": 2},
        },
        "Isengard",
        "Gondor",
        ["Isengard", "Bree", "Gondor"],
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        {"Minas Tirith": {"Isengard": 2}, "Isengard": {"Minas Tirith": 2}},
        "Minas Tirith",
        "Isengard",
        ["Minas Tirith", "Isengard"],
    ),
    (
        {
            "Erebor": {"Minas Tirith": 2, "Isengard": 1},
            "Minas Tirith": {"Erebor": 3, "Isengard": 4, "Gondor": 8},
            "Isengard": {"Erebor": 4, "Minas Tirith": 2, "Bree": 2},
            "Gondor": {"Minas Tirith": 2, "Bree": 7, "Osgiliath": 4},
            "Bree": {"Isengard": 1, "Gondor": 11, "Osgiliath": 5},
            "Osgiliath": {"Gondor": 3, "Bree": 5},
        },
        "Erebor",
        "Osgiliath",
        ["Erebor", "Isengard", "Bree", "Osgiliath"],
    ),
    (
        {
            "Erebor": {"Minas Tirith": 2, "Isengard": 1},
            "Minas Tirith": {"Erebor": 3, "Isengard": 4, "Gondor": 8},
            "Isengard": {"Erebor": 4, "Minas Tirith": 2, "Bree": 2},
            "Gondor": {"Minas Tirith": 2, "Bree": 7, "Osgiliath": 4},
            "Bree": {"Isengard": 1, "Gondor": 11, "Osgiliath": 5},
            "Osgiliath": {"Gondor": 3, "Bree": 5},
        },
        "Minas Tirith",
        "Bree",
        ["Minas Tirith", "Isengard", "Bree"],
    ),
]


def test(
    graph: dict[str, dict[str, int]], src: str, dest: str, expected_output: list[str]
) -> bool:
    try:
        print("---------------------------------")
        print("Graph:")
        for k, v in graph.items():
            print(f" Vertex {k}: {v}")
        print(f"\n - Src: {src}")
        print(f" - Dest: {dest}\n")
        print(f"Expected Path: {expected_output}")
        result = dijkstra(graph, src, dest)
        print(f"Actual Path: {result}\n")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print("Fail")
        print(e)
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
