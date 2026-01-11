from main import *

run_cases = [
    ([6, 8, 10], 2, [3.0, 4.0, 5.0]),
    ([1, 2, 3, 4], 1, [1.0, 2.0, 3.0, 4.0]),
]

submit_cases = run_cases + [
    ([15, 30, 45], 3, [5.0, 10.0, 15.0]),
    ([0], 1, [0.0]),
    ([27, 54, 81], 9, [3.0, 6.0, 9.0]),
    ([100, 200, 300, 400], 10, [10.0, 20.0, 30.0, 40.0]),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * List of numbers: {input1}")
    print(f" * Divisor: {input2}")
    result = divide_list(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
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
