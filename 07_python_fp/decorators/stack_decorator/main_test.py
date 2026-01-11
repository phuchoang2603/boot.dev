from main import *


run_cases = [
    (
        replacer("faith", "salmon")(lambda x: x),
        'replacer("faith", "salmon")(lambda x: x)',
        "I find your lack of faith disturbing, young Skywalker.",
        "I find your lack of salmon disturbing, young Skywalker.",
    ),
    (
        replacer("paragraph", "span")(replacer("p>", "span>")(lambda x: x)),
        'replacer("paragraph", "span")(replacer("p>", "span>")(lambda x: x))',
        "<p>Here is a paragraph</p>",
        "<span>Here is a span</span>",
    ),
    (
        tag_pre,
        "tag_pre",
        '<a href="https://blog.boot.dev/wiki/troubleshoot-code-editor-issues/">link</a>',
        "<pre>&lt;a href=&quot;https://blog.boot.dev/wiki/troubleshoot-code-editor-issues/&quot;&gt;link&lt;/a&gt;</pre>",
    ),
]

submit_cases = run_cases + [
    (
        tag_pre,
        "tag_pre",
        '<img src="https://imgur.com/a/VlMAK0B" alt="mystery">',
        "<pre>&lt;img src=&quot;https://imgur.com/a/VlMAK0B&quot; alt=&quot;mystery&quot;&gt;</pre>",
    ),
    (
        tag_pre,
        "tag_pre",
        "<p>This paragraph has <em>italic text</em></p>",
        "<pre>&lt;p&gt;This paragraph has &lt;em&gt;italic text&lt;/em&gt;&lt;/p&gt;</pre>",
    ),
]


def test(func, func_name, input, expected_output):
    print("---------------------------------")
    print(f"Function: {func_name}")
    print(f"    Input: {input}")
    print(f"Expected: {expected_output}")
    result = func(input)
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
