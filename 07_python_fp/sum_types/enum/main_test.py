from main import *

run_cases = [
    (lambda: Doctype.PDF, "Doctype.PDF", False),
    (lambda: Doctype.TXT, "Doctype.TXT", False),
    (lambda: Doctype.DOCX, "Doctype.DOCX", False),
    (lambda: Doctype.MD, "Doctype.MD", False),
]

submit_cases = run_cases + [
    (lambda: Doctype.HTML, "Doctype.HTML", False),
    (lambda: Doctype.Invalid, "Doctype.Invalid", True),
]


def test(func, name, is_err):
    print("---------------------------------")
    print(f"Checking value: {name}")
    try:
        val = func()
        print(f"...Valid enum value!")
        return not is_err
    except Exception as e:
        print(f"...Invalid enum value!")
        return is_err


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
