from functions.get_file_content import get_file_content
from config import MAX_CHARS
import os

run_cases = [
    (
        "test/fixtures",
        "sample.txt",
        "Hello World!\nThis is a test file.\nLine 3.\n",
    ),
    (
        "test/fixtures",
        "subdir/nested.txt",
        "This file is in a subdirectory.\n",
    ),
    (
        "test/fixtures",
        "empty.txt",
        "",  # Empty file
    ),
    (
        "test/fixtures",
        "large.txt",
        lambda: get_expected_large_file_content(),
    ),
    (
        "test/fixtures",
        "nonexistent.txt",
        'Error: File not found or is not a regular file: "nonexistent.txt"\n',
    ),
    (
        "test/fixtures",
        "subdir",  # Directory, not a file
        'Error: File not found or is not a regular file: "subdir"\n',
    ),
    (
        "test/fixtures",
        "/etc/passwd",
        'Error: Cannot read "/etc/passwd" as it is outside the permitted working directory\n',
    ),
    (
        "test/fixtures",
        "../config.py",
        'Error: Cannot read "../config.py" as it is outside the permitted working directory\n',
    ),
]


def get_expected_large_file_content():
    """
    Get expected content for large.txt file.
    If file is > MAX_CHARS, it should be truncated with a message.
    """
    file_path = "test/fixtures/large.txt"

    # Read the actual file to determine expected output
    with open(file_path, "r") as f:
        full_content = f.read()

    if len(full_content) > MAX_CHARS:
        # File should be truncated
        expected = (
            full_content[:MAX_CHARS]
            + f'[...File "large.txt" truncated at {MAX_CHARS} characters]'
        )
        return expected
    else:
        # File is not large enough to trigger truncation
        return full_content


def test(working_directory, file_path, expected_output):
    print("---------------------------------")
    print(f"Inputs: {working_directory} {file_path}")

    # If expected_output is a lambda, call it to get the actual expected value
    if callable(expected_output):
        expected_output = expected_output()

    try:
        result = get_file_content(working_directory, file_path)
    except Exception as e:
        result = f"{e}\n"

    # For large output, just show first 100 chars
    if len(str(expected_output)) > 100 or len(str(result)) > 100:
        print(
            f"Expected: {str(expected_output)[:100]}... ({len(expected_output)} chars)"
        )
        print(f"Actual:   {str(result)[:100]}... ({len(result)} chars)")
    else:
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
    for test_case in run_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


if __name__ == "__main__":
    main()
