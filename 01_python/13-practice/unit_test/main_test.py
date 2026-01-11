from math import isclose

from main import avg_luck_boost
from test_cases import run_cases


def test(luck_boosts: list[int], expected_avg: float, exceptions: list[int]) -> bool:
    print("---------------------------------")
    print(f"Party luck boosts: {luck_boosts}")

    try:
        avg = avg_luck_boost(luck_boosts)
    except ZeroDivisionError as err:
        print(f"Caught ZeroDivisionError: {err}")
        exceptions[0] += 1
        return False

    print(f"Expected average boost: {expected_avg}")
    print(f"Actual average boost:   {avg}")
    if isclose(avg, expected_avg):
        print("Pass")
        return True

    print("Fail")
    return False


def main() -> None:
    passed = 0
    failed = 0
    exceptions = [0]

    for case in run_cases:
        correct = test(**case, exceptions=exceptions)
        if correct:
            passed += 1
        else:
            failed += 1

    print()

    if len(run_cases) != 5:
        print("============= FAIL ==============")
        print("There should be five test cases!")
    elif failed != 1:
        print("============= FAIL ==============")
        print("There should be one failing test!")
    elif exceptions[0] != 1:
        print("============= FAIL ==============")
        print("One ZeroDivisionError should have been caught!")
    else:
        print("============= PASS ==============")

    print(f"{passed} tests passed; {failed} failed (1 expected)")


main()
