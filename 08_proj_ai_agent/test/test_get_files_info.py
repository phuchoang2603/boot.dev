from functions.get_files_info import get_files_info
import os


# Helper function to dynamically build expected output
def build_expected_listing(working_directory, directory, files_info):
    """
    Build expected directory listing output with actual file sizes.

    Args:
        working_directory: Base working directory
        directory: Target directory to list
        files_info: List of (filename, is_dir) tuples

    Returns:
        Expected output string with actual file sizes
    """
    result = "\n"
    for filename, is_dir in files_info:
        full_path = os.path.join(working_directory, directory, filename)
        file_size = os.path.getsize(full_path)
        result += f" - {filename}: file_size={file_size} bytes, is_dir={is_dir}\n"
    return result


run_cases = [
    (
        "test/fixtures",
        ".",
        lambda: build_expected_listing(
            "test/fixtures",
            ".",
            [
                ("emptydir", True),
                ("empty.txt", False),
                ("large.txt", False),
                ("sample.txt", False),
                ("subdir", True),
                ("temp", True),
            ],
        ),
    ),
    (
        "test/fixtures",
        "subdir",
        lambda: build_expected_listing(
            "test/fixtures",
            "subdir",
            [
                ("nested.txt", False),
            ],
        ),
    ),
    (
        "test/fixtures",
        "emptydir",
        "\n",  # Empty directory returns just newline
    ),
    (
        "test/fixtures",
        "sample.txt",  # File, not directory
        'Error: Directory not found or is not a valid directory: "sample.txt"\n',
    ),
    (
        "test/fixtures",
        "/bin",
        'Error: Cannot list "/bin" as it is outside the permitted working directory\n',
    ),
    (
        "test/fixtures",
        "../",
        'Error: Cannot list "../" as it is outside the permitted working directory\n',
    ),
    (
        "test/fixtures",
        "nonexistent_dir",
        'Error: Directory not found or is not a valid directory: "nonexistent_dir"\n',
    ),
]


def test(working_directory, directory, expected_output):
    print("---------------------------------")
    print(f"Inputs: {working_directory} {directory}")

    # If expected_output is a lambda, call it to get the actual expected value
    if callable(expected_output):
        expected_output = expected_output()

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
