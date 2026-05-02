from main import get_path

TestCase = tuple[str, dict[str, str], list[str]]

run_cases: list[TestCase] = [
    (
        "Minas Tirith",
        {"Minas Tirith": "Isengard", "Isengard": "Gondor", "Gondor": "Rivendell"},
        ["Rivendell", "Gondor", "Isengard", "Minas Tirith"],
    ),
    (
        "Minas Tirith",
        {"Minas Tirith": "Rivendell", "Isengard": "Gondor", "Rivendell": "Isengard"},
        ["Gondor", "Isengard", "Rivendell", "Minas Tirith"],
    ),
]

submit_cases: list[TestCase] = run_cases + [
    ("Minas Tirith", {}, ["Minas Tirith"]),
    ("Rivendell", {"Minas Tirith": "Rivendell"}, ["Rivendell"]),
    (
        "Gondor",
        {
            "Minas Tirith": "Isengard",
            "Isengard": "Gondor",
            "Gondor": "Rivendell",
            "Bree": "Minas Tirith",
        },
        ["Rivendell", "Gondor"],
    ),
]


def test(dest: str, predecessors: dict[str, str], expected_output: list[str]) -> bool:
    try:
        print("---------------------------------")
        print("Inputs:")
        print(f" * Destination: {dest}")
        print(f" * Predecessors: {predecessors}")
        print(f"Expected Path: {expected_output}")
        result = get_path(dest, predecessors)
        print(f"Actual Path: {result}")
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
    for i in range(len(test_cases)):
        correct = test(*test_cases[i])
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
