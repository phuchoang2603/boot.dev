from main import *

try:
    (
        CSVExportStatus.PENDING
        and CSVExportStatus.PROCESSING
        and CSVExportStatus.SUCCESS
        and CSVExportStatus.FAILURE
    )
except Exception as error:
    print(f"Error: Missing attribute {error} from enum")

    class CSVExportStatus(Enum):
        PENDING = None
        PROCESSING = None
        SUCCESS = None
        FAILURE = None


run_cases = [
    (
        CSVExportStatus.PENDING,
        [
            ["Customer ID", "Billed", "Paid"],
            [1, 100, 100],
            [2, 400, 99],
            [3, 50, 25],
        ],
        (
            "Pending...",
            [
                ["Customer ID", "Billed", "Paid"],
                ["1", "100", "100"],
                ["2", "400", "99"],
                ["3", "50", "25"],
            ],
        ),
    ),
    (
        CSVExportStatus.PROCESSING,
        [
            ["Customer ID", "Billed", "Paid"],
            ["1", "100", "100"],
            ["2", "400", "99"],
            ["3", "50", "25"],
        ],
        (
            "Processing...",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
    (
        CSVExportStatus.SUCCESS,
        "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        (
            "Success!",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
    (
        CSVExportStatus.FAILURE,
        [
            ["Customer ID", "Billed", "Paid"],
            [1, 100, 100],
            [2, 400, 99],
            [3, 50, 25],
        ],
        (
            "Unknown error, retrying...",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
]

submit_cases = run_cases + [
    (
        CSVExportStatus.PENDING,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", 100],
            ["Moist Turtle", "Good", 200],
            ["Burning Lizard", "Very Good", 1000],
            ["Mossy Frog", "Poor", 10],
        ],
        (
            "Pending...",
            [
                ["Card Name", "Condition", "Value"],
                ["Sparky Mouse", "Fair", "100"],
                ["Moist Turtle", "Good", "200"],
                ["Burning Lizard", "Very Good", "1000"],
                ["Mossy Frog", "Poor", "10"],
            ],
        ),
    ),
    (
        CSVExportStatus.PROCESSING,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", "100"],
            ["Moist Turtle", "Good", "200"],
            ["Burning Lizard", "Very Good", "1000"],
            ["Mossy Frog", "Poor", "10"],
        ],
        (
            "Processing...",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
    ),
    (
        CSVExportStatus.SUCCESS,
        "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        (
            "Success!",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
    ),
    (
        CSVExportStatus.FAILURE,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", 100],
            ["Moist Turtle", "Good", 200],
            ["Burning Lizard", "Very Good", 1000],
            ["Mossy Frog", "Poor", 10],
        ],
        (
            "Unknown error, retrying...",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
    ),
    (1, None, ("Exception Raised:", "unknown export status")),
]


def test(status, data, expected_output):
    print("---------------------------------")
    print(f"Checking: {status}")
    print("Expected:")
    print(f"{expected_output[0]}")
    print(f"{expected_output[1]}")
    try:
        result = get_csv_status(status, data)
    except Exception as e:
        result = expected_output[0], str(e)
    print("Actual:")
    print(f"{result[0]}")
    print(f"{result[1]}")
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
