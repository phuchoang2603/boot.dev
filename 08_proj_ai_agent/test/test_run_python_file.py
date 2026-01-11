from functions.run_python_file import run_python_file

run_cases = [
    (
        "calculator",
        "main.py",
        None,
    ),
    (
        "calculator",
        "main.py",
        ["3 + 5"],
    ),
    (
        "calculator",
        "tests.py",
        None,
    ),
    (
        "calculator",
        "../main.py",
        None,
    ),
    (
        "calculator",
        "nonexistent.py",
        None,
    ),
    (
        "calculator",
        "lorem.txt",
        None,
    ),
]


def test(working_directory, file_path, args):
    print("---------------------------------")
    args_str = f" {args}" if args else ""
    print(f"Running: {working_directory} {file_path}{args_str}")

    try:
        result = run_python_file(working_directory, file_path, args)
        print(result)
    except Exception as e:
        print(e)


def main():
    for test_case in run_cases:
        test(*test_case)


if __name__ == "__main__":
    main()
