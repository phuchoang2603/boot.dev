from formatters import *
from decorators import *

run_cases = [
    (
        ("# We like to play it all", "## Welcome to Tally Hall"),
        {},
        concat,
        """  First: We like to play it all
  Second: Welcome to Tally Hall""",
    ),
    (
        set(),
        {
            "title": "Why Python is Great",
            "body": "Maybe it isn't",
            "conclusion": "## That's why Python is great!",
        },
        format_as_essay,
        """  Title: Why Python is Great
  Body: Maybe it isn't
  Conclusion: That's why Python is great!""",
    ),
]

submit_cases = run_cases + [
    (
        ("# Boots' grocery list", "Salmon, gems, arcanum crystals"),
        {
            "conclusion": "## Don't forget!",
        },
        format_as_essay,
        """  Title: Boots' grocery list
  Body: Salmon, gems, arcanum crystals
  Conclusion: Don't forget!""",
    ),
]


def test(args, kwargs, func, expected_output):
    print("---------------------------------")
    print(f"Positional Arguments:")
    for arg in args:
        print(f" * {arg}")
    print(f"Keyword Arguments:")
    for key, value in kwargs.items():
        print(f" * {key}: {value}")
    print(f"Expected:")
    print(expected_output)
    try:
        result = func(*args, **kwargs)
    except Exception as error:
        result = f"Error: {error}"
    print(f"Actual:")
    print(result)
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
