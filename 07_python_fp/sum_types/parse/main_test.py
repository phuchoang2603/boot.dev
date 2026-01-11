from main import *

run_cases = [
    Parsed("why_fp.txt", "Because we're better than everyone else"),
    ParseError("why_fp.docx", "Can't handle weird windows files"),
]

submit_cases = run_cases + [
    Parsed("why_fp.md", "Because we're better than everyone else"),
    ParseError("why_fp.pdf", "Can't handle weird adobe files"),
]


def test(obj):
    print("---------------------------------")
    print(f"Testing properties of {obj.doc_name}...")
    if isinstance(obj, Parsed):
        if not obj.text:
            print(f"Expecting .text to be non-empty")
            print("Fail")
            return False
        if not obj.doc_name:
            print(f"Expecting .doc_name to be non-empty")
            print("Fail")
            return False
    elif isinstance(obj, ParseError):
        if not obj.err:
            print(f"Expecting .err to be non-empty")
            print("Fail")
            return False
        if not obj.doc_name:
            print(f"Expecting .doc_name to be non-empty")
            print("Fail")
            return False
    else:
        raise ValueError(f"unknown class type for: {obj}")
    print("Pass")
    return True


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(test_case)
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
