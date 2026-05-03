from main import dfs_path, dijkstra

Graph = dict[str, dict[str, int]]
TestCase = tuple[Graph, str, str, list[str], tuple[int, int]]


run_cases: list[TestCase] = [
    (
        {
            "Denver": {
                "Boise": 2,  # DFS with LIFO queue will try this last
                "Phoenix": 80,
                "Dallas": 80,
                "Seattle": 80,
            },
            # Trap branches: 2 levels deep with some dead ends
            "Phoenix": {
                "Las_Vegas": 15,
                "Tucson": 15,
            },
            "Dallas": {
                "Austin": 15,
                "Houston": 15,
            },
            "Seattle": {
                "Portland": 15,
                "Spokane": 15,
            },
            # Second level: mix of high-cost paths to Miami, dead ends
            "Las_Vegas": {"Miami": 40},
            "Tucson": {},
            "Austin": {"Miami": 40},
            "Houston": {},
            "Portland": {"Miami": 40},
            "Spokane": {},
            # Low-cost path, but with more hops
            "Boise": {"Salt_Lake": 2},
            "Salt_Lake": {"Provo": 2},
            "Provo": {"Flagstaff": 2},
            "Flagstaff": {"Santa_Fe": 2},
            "Santa_Fe": {"Miami": 2},
            "Miami": {},
        },
        "Denver",
        "Miami",
        ["Denver", "Boise", "Salt_Lake", "Provo", "Flagstaff", "Santa_Fe", "Miami"],
        (7, 19),
    )
]

submit_cases = run_cases + [
    (
        {
            "Berlin": {
                "Potsdam": 1,
                "Hamburg": 100,
                "Bremen": 100,
                "Bielefeld": 100,
            },
            "Hamburg": {
                "Kiel": 20,
                "Rostock": 20,
                "Schwerin": 20,
            },
            "Bremen": {
                "Achim": 20,
                "Hanover": 20,
                "Oldenburg": 20,
            },
            "Bielefeld": {
                "Hildesheim": 20,
                "Paderborn": 20,
                "Hamm": 20,
            },
            "Kiel": {"Molfsee": 10, "Preetz": 10},
            "Rostock": {"Schwaan": 10, "Marlow": 10},
            "Schwerin": {"Pampow": 10, "Pinnow": 10},
            "Achim": {"Martfeld": 10, "Blender": 10},
            "Hanover": {"Garbsen": 10, "Lehrte": 10},
            "Oldenburg": {"Edewecht": 10, "Hude": 10},
            "Hildesheim": {"Gronau": 10, "Burgdorf": 10},
            "Paderborn": {"Warburg": 10, "Brakel": 10},
            "Hamm": {"Dortmund": 10, "Solingen": 10},
            "Molfsee": {"Frankfurt": 500},
            "Preetz": {},
            "Schwaan": {},
            "Marlow": {"Frankfurt": 500},
            "Pampow": {"Frankfurt": 500},
            "Pinnow": {},
            "Martfeld": {},
            "Blender": {"Frankfurt": 500},
            "Garbsen": {"Frankfurt": 500},
            "Lehrte": {},
            "Edewecht": {},
            "Hude": {"Frankfurt": 500},
            "Gronau": {"Frankfurt": 500},
            "Burgdorf": {},
            "Warburg": {},
            "Brakel": {"Frankfurt": 500},
            "Dortmund": {},
            "Solingen": {"Frankfurt": 500},
            "Potsdam": {"Leipzig": 1},
            "Leipzig": {"Bayreuth": 1},
            "Bayreuth": {"Bamberg": 1},
            "Bamberg": {"Frankfurt": 1},
            "Frankfurt": {},
        },
        "Berlin",
        "Frankfurt",
        ["Berlin", "Potsdam", "Leipzig", "Bayreuth", "Bamberg", "Frankfurt"],
        (6, 45),
    )
]


def test(
    graph: Graph,
    src: str,
    dest: str,
    expected_path: list[str],
    expected_visits: tuple[int, int],
) -> bool:
    try:
        print("---------------------------------")

        dijkstra_route, dijkstra_visits = dijkstra(graph, src, dest)
        dfs_route, dfs_visits = dfs_path(graph, src, dest)

        print(f"Expected path:            {expected_path}")
        print(f"Actual path (Dijkstra's): {dijkstra_route}")
        print(f"Actual path (DFS):        {dfs_route}")
        if dijkstra_route != expected_path or dfs_route != expected_path:
            print("\nFail")
            return False

        print(f"\nExpected node visits (Dijkstra's): {expected_visits[0]}")
        print(f"Actual node visits (Dijkstra's):   {dijkstra_visits}")
        if dijkstra_visits != expected_visits[0]:
            print("\nFail")
            return False

        print(f"\nExpected node visits (DFS): {expected_visits[1]}")
        print(f"Actual node visits (DFS):   {dfs_visits}")
        if dfs_visits != expected_visits[1]:
            print("\nFail")
            return False

        print("\nPass\n")
        return True
    except Exception as e:
        print("\nFail")
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
