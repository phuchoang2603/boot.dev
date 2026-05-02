from typing import Optional

from main import next_nearest_node

TestCase = tuple[dict[str, int], set[str], Optional[str]]

run_cases: list[TestCase] = [
    (
        {"Minas Tirith": 4, "Isengard": 2, "Gondor": 3, "Mirkwood": 1},
        {"Minas Tirith", "Gondor"},
        "Gondor",
    ),
    (
        {"Minas Tirith": 1, "Isengard": 2, "Gondor": 2, "Mirkwood": 1},
        {"Minas Tirith", "Gondor"},
        "Minas Tirith",
    ),
]

submit_cases: list[TestCase] = run_cases + [
    ({}, set(), None),
    (
        {"Minas Tirith": 1, "Isengard": 2, "Gondor": 2, "Mirkwood": 1},
        {"Isengard", "Mirkwood"},
        "Mirkwood",
    ),
    (
        {
            "Minas Tirith": 3,
            "Isengard": 8,
            "Gondor": 7,
            "Mirkwood": 12,
            "Rivendell": 10,
        },
        {"Isengard", "Mirkwood"},
        "Isengard",
    ),
]


def test(
    distances: dict[str, int], unvisited: set[str], expected: Optional[str]
) -> bool:
    try:
        print("---------------------------------")
        print("Inputs:")
        print(f"- Distances: {distances}")
        print(f"- Unvisited: {unvisited}\n")
        print(f"Expecting: {expected}")
        result = next_nearest_node(distances, unvisited)
        print(f"Actual: {result}\n")
        if result == expected:
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
