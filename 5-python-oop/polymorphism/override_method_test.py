from override_method import *

run_cases = [
    (("Smaug", "red"), "I am Smaug, the red dragon"),
    (("Saphira", "blue"), "I am Saphira, the blue dragon"),
]

submit_cases = run_cases + [
    (("Eldrazi", "colorless"), "I am Eldrazi, the colorless dragon"),
    (("Glaurung", "gold"), "I am Glaurung, the gold dragon"),
    (("Fafnir", "green"), "I am Fafnir, the green dragon"),
]


def test(args, expected_output):
    try:
        print("---------------------------------")
        print(f"Name: {args[0]}, Color: {args[1]}")
        print("")
        print(f"Expected: {expected_output}")
        dragon = Dragon(*args)
        result = str(dragon)
        print(f"Actual:   {result}")
        if result == expected_output:
            return True
        return False
    except Exception as e:
        print(f"Error: {e}")
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
