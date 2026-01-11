from functions.get_file_content import get_file_content

run_cases = [
    (
        "calculator",
        "main.py",
        """Bruh""",
    ),
    (
        "calculator",
        "pkg/calculator.py",
        """Bruh""",
    ),
    (
        "calculator",
        "/bin/cat",
        'Error: Cannot read "/bin/cat" as it is outside the permitted working directory\n',
    ),
    (
        "calculator",
        "pkg/does_not_exist.py",
        'Error: File not found or is not a regular file: "pkg/does_not_exist.py"\n',
    ),
]


def test(working_directory, file_path, expected_output):
    print("---------------------------------")
    print(f"Inputs: {working_directory} {file_path}")
    try:
        result = get_file_content(working_directory, file_path)
    except Exception as e:
        result = f"{e}\n"
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
