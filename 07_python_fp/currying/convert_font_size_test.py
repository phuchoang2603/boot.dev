from convert_font_size import *

run_cases = [
    (12, "txt", 12),
    (16, "md", 32),
]

submit_cases = run_cases + [
    (14, "html", "invalid doc type"),
    (0, "txt", 0),
    (50, "md", 100),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * font_size: {input1}")
    print(f" * doc_type: {input2}")
    print(f"Expected: {expected_output}")
    try:
        result = converted_font_size(input1)(input2)
    except Exception as error:
        result = str(error)
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
