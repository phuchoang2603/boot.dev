from functions.get_files_info import get_files_info

run_cases = [
    (
        "calculator",
        ".",
        """
 - pkg: file_size=44 bytes, is_dir=True
 - main.py: file_size=741 bytes, is_dir=False
 - tests.py: file_size=1354 bytes, is_dir=False
""",
    ),
    (
        "calculator",
        "pkg",
        """
 - calculator.py: file_size=1754 bytes, is_dir=False
 - render.py: file_size=404 bytes, is_dir=False
""",
    ),
    (
        "calculator",
        "/bin",
        'Error: Cannot list "/bin" as it is outside the permitted working directory\n',
    ),
    (
        "calculator",
        "../",
        'Error: Cannot list "../" as it is outside the permitted working directory\n',
    ),
    (
        "calculator",
        "main.py",
        'Error: Directory not found or is not a valid directory: "main.py"\n',
    ),
]


def test(working_directory, directory, expected_output):
    print("---------------------------------")
    print(f"Inputs: {working_directory} {directory}")
    try:
        result = get_files_info(working_directory, directory)
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
