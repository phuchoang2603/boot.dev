from create_markdown_image import *


run_cases = [
    (
        "seal",
        "https://imgur.com/oglPAXK",
        "this is a seal",
        '![seal](https://imgur.com/oglPAXK "this is a seal")',
    ),
    (
        "cinnamon roll",
        "https://imgur.com/a/0MyOP",
        "this is a cinnamon roll",
        '![cinnamon roll](https://imgur.com/a/0MyOP "this is a cinnamon roll")',
    ),
]

submit_cases = run_cases + [
    (
        "banana",
        "https://imgur.com/nlArAKx",
        None,
        "![banana](https://imgur.com/nlArAKx)",
    ),
    (
        "not an image",
        "https://en.wikipedia.org/wiki/Variable_(computer_science)",
        "showing escape characters",
        '![not an image](https://en.wikipedia.org/wiki/Variable_%28computer_science%29 "showing escape characters")',
    ),
]


def test(alt_text, url, title, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f"* Alt Text: {alt_text}")
    print(f"* URL: {url}")
    print(f"* Title: {title}")
    print(f"Expected: {expected_output}")
    result = create_markdown_image(alt_text)(url)()
    if title:
        result = create_markdown_image(alt_text)(url)(title)
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
