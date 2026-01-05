from dragon import *

run_cases = [
    (Dragon("Green Dragon", -1, -2, 1, 2, 1), -2, -3, 0, 0, True),
    (Dragon("Red Dragon", 2, 2, 2, 2, 2), 0, 1, 1, 0, True),
    (Dragon("Gold Dragon", 0, 0, 5, 5, 10), 4, 0, 5, 1, False),
    (Dragon("Blue Dragon", 4, -3, 2, 1, 1), 0, 0, 10, 10, False),
]

submit_cases = run_cases + [
    (Dragon("Orange Dragon", 0, 0, 20, 20, 20), 10, 10, 20, 20, True),
    (Dragon("Black Dragon", 5, -1, 3, 2, 2), -10, -10, 10, 10, True),
]


def test(dragon, x1, y1, x2, y2, expected_output):
    print("---------------------------------")
    print(f" * Dragon pos_x: {dragon.pos_x}")
    print(f" * Dragon pos_y: {dragon.pos_y}")
    print(f" * Dragon height: {dragon.height}")
    print(f" * Dragon width: {dragon.width}")
    print("")
    print(f" * Area x1: {x1}")
    print(f" * Area y1: {y1}")
    print(f" * Area x2: {x2}")
    print(f" * Area y2: {y2}")
    print("")
    result = dragon.in_area(x1, y1, x2, y2)
    print(f"Expected in area: {expected_output}")
    print(f"Actual in area:   {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
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
