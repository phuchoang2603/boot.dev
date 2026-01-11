from get_filter_cwd import *

run_cases = [
    (
        replace_bad,
        replace_ellipsis,
        [
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                ),
                "I'm good, and that's good. I will never be good, and that's not good..",
            ),
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                    "--one",
                ),
                "I'm good, and that's good. I will never be good, and that's not good..",
            ),
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                    "--two",
                ),
                "I'm bad, and that's good. I will never be good, and that's not bad...",
            ),
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                    "--three",
                ),
                "I'm good, and that's good. I will never be good, and that's not good...",
            ),
        ],
    ),
]

submit_cases = run_cases + [
    (
        replace_ellipsis,
        fix_ellipsis,
        [
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                ),
                "There's no place like home... but sometimes, it's nice to get away.... and explore......",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "--one",
                ),
                "There's no place like home... but sometimes, it's nice to get away.... and explore......",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "--two",
                ),
                "There's no place like home.. but sometimes, it's nice to get away... and explore...",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "--three",
                ),
                "There's no place like home... but sometimes, it's nice to get away... and explore.....",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "",
                ),
                "invalid option",
            ),
        ],
    ),
]


def test(filter_one, filter_two, test_cases):
    print("---------------------------------")
    print(f"Input functions: {filter_one.__name__} and {filter_two.__name__}")
    filter_cmd = get_filter_cmd(filter_one, filter_two)
    failed = False
    for case in test_cases:
        try:
            result = filter_cmd(*case[0])
        except Exception as e:
            result = str(e)
        expected_output = case[1]
        print(f"Expected: {expected_output}")
        print(f"Actual:   {result}")
        if result != expected_output:
            failed = True
            print("Fail")
        else:
            print("Pass")
    passed = not failed
    return passed


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
