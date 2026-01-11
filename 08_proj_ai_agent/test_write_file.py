from functions.write_files import write_file
import os

run_cases = [
    (
        "calculator",
        "lorem.txt",
        "wait, this isn't lorem ipsum",
        "wait, this isn't lorem ipsum",  # Expected content
        None,  # Expected error (None means should succeed)
    ),
    (
        "calculator",
        "pkg/morelorem.txt",
        "lorem ipsum dolor sit amet",
        "lorem ipsum dolor sit amet",
        None,
    ),
    (
        "calculator",
        "/tmp/temp.txt",
        "this should not be allowed",
        None,
        'Error: Cannot write "/tmp/temp.txt" as it is outside the permitted working directory\n',
    ),
    (
        "calculator",
        "../outside.txt",
        "this should also not be allowed",
        None,
        'Error: Cannot write "../outside.txt" as it is outside the permitted working directory\n',
    ),
    (
        "calculator",
        "pkg",  # Trying to write to a directory
        "cannot write to directory",
        None,
        'Error: Cannot write to "pkg" as it is a directory\n',
    ),
    (
        "calculator",
        "main.py",  # Overwriting existing file
        "overwrite existing file",
        "overwrite existing file",
        None,
    ),
]


def test(working_directory, file_path, content, expected_content, expected_error):
    print("---------------------------------")
    print(f"Inputs: {working_directory} {file_path}")

    full_path = os.path.join(working_directory, file_path)

    try:
        write_file(working_directory, file_path, content)

        # If we expect an error but didn't get one
        if expected_error:
            print(f"Expected error: {expected_error}")
            print(f"Actual: File written successfully (should have failed)")
            print("Fail")
            return False

        # Verify the file was written with correct content
        if os.path.isfile(full_path):
            with open(full_path, "r") as f:
                actual_content = f.read()

            if actual_content == expected_content:
                print(f"Expected content: {expected_content}")
                print(f"Actual content: {actual_content}")
                print("Pass")
                return True
            else:
                print(f"Expected content: {expected_content}")
                print(f"Actual content: {actual_content}")
                print("Fail")
                return False
        else:
            print(f"Expected: File to be written")
            print(f"Actual: File not found at {full_path}")
            print("Fail")
            return False

    except Exception as e:
        result = f"{e}\n"

        if expected_error:
            print(f"Expected error: {expected_error}")
            print(f"Actual error: {result}")
            if result == expected_error:
                print("Pass")
                return True
            else:
                print("Fail")
                return False
        else:
            print(f"Expected: Success")
            print(f"Actual error: {result}")
            print("Fail")
            return False


def cleanup():
    """Clean up test files"""
    test_files = [
        "calculator/lorem.txt",
        "calculator/pkg/morelorem.txt",
    ]

    for file_path in test_files:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Cleaned up: {file_path}")

    # Restore main.py if it was overwritten
    main_py_path = "calculator/main.py"
    if os.path.exists(main_py_path):
        # Just check if it's been overwritten (contains our test content)
        with open(main_py_path, "r") as f:
            content = f.read()
            if content == "overwrite existing file":
                print(
                    f"WARNING: {main_py_path} was overwritten in test. Please restore from git."
                )


def main():
    passed = 0
    failed = 0

    for test_case in run_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1

    print("=================================")
    cleanup()
    print("=================================")

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


if __name__ == "__main__":
    main()
