from main import *

try:
    DocFormat.MD and DocFormat.HTML and DocFormat.PDF and DocFormat.TXT
except Exception as error:
    print(f"Error: Missing attribute {error} from enum")

    class DocFormat(Enum):
        PDF = None
        TXT = None
        MD = None
        HTML = None


run_cases = [
    ("# Hello, world!", DocFormat.MD, DocFormat.HTML, "<h1>Hello, world!</h1>"),
    (
        "This is plain text.",
        DocFormat.TXT,
        DocFormat.PDF,
        "[PDF] This is plain text. [PDF]",
    ),
]

submit_cases = run_cases + [
    ("<h1>Title</h1>", DocFormat.HTML, DocFormat.MD, "# Title"),
    ("Something wicked", DocFormat.TXT, None, "invalid type"),
]


def test(content, from_format, to_format, expected_output):
    print("---------------------------------")
    print(f"Converting from {from_format} to {to_format}...")
    print(f"Content: {content}")
    print(f"Expected: {expected_output}")
    try:
        result = convert_format(content, from_format, to_format)
    except Exception as e:
        result = str(e)
    print(f"Actual: {result}")
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
