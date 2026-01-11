from functions.write_files import write_file
import os
import shutil

run_cases = [
    (
        "test/fixtures/temp",
        "new_file.txt",
        "This is new content",
        'Successfully wrote to "new_file.txt" (19 characters written)',
        None,
    ),
    (
        "test/fixtures/temp",
        "nested/deep/file.txt",  # Test creating nested directories
        "Deep nesting test",
        'Successfully wrote to "nested/deep/file.txt" (17 characters written)',
        None,
    ),
    (
        "test/fixtures/temp",
        "overwrite.txt",  # Overwriting existing file
        "First write",
        'Successfully wrote to "overwrite.txt" (11 characters written)',
        None,
    ),
    (
        "test/fixtures/temp",
        "/tmp/outside.txt",
        "Not allowed",
        None,
        'Error: Cannot write "/tmp/outside.txt" as it is outside the permitted working directory\n',
    ),
    (
        "test/fixtures/temp",
        "../escape.txt",
        "Not allowed",
        None,
        'Error: Cannot write "../escape.txt" as it is outside the permitted working directory\n',
    ),
    (
        "test/fixtures",
        "subdir",  # Existing directory
        "Cannot write to dir",
        None,
        'Error: Cannot write to "subdir" as it is a directory\n',
    ),
]


def test(working_directory, file_path, content, expected_result, expected_error):
    print("---------------------------------")
    print(f"Inputs: {working_directory} {file_path}")

    try:
        result = write_file(working_directory, file_path, content)

        # If we expect an error but didn't get one
        if expected_error:
            print(f"Expected error: {expected_error}")
            print(f"Actual: {result}")
            print("Fail")
            return False

        # Compare result string
        if result == expected_result:
            print(f"Expected: {expected_result}")
            print(f"Actual:   {result}")
            print("Pass")
            return True
        else:
            print(f"Expected: {expected_result}")
            print(f"Actual:   {result}")
            print("Fail")
            return False

    except Exception as e:
        error_result = f"{e}\n"

        if expected_error:
            print(f"Expected: {expected_error}")
            print(f"Actual:   {error_result}")
            if error_result == expected_error:
                print("Pass")
                return True
            else:
                print("Fail")
                return False
        else:
            print(f"Expected: {expected_result}")
            print(f"Actual:   {error_result}")
            print("Fail")
            return False


def cleanup():
    """Clean up test files created during tests"""
    temp_dir = "test/fixtures/temp"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir, exist_ok=True)
    print("Cleaned up temp directory")


def main():
    # Clean up before tests
    cleanup()
    print("=================================")

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
