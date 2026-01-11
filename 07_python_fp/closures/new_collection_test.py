from new_collection import *


run_cases = [
    (["Dan Evans"], ["Charlie Prince"], ["Dan Evans", "Charlie Prince"]),
    (
        ["Dan Evans", "Ben Wade"],
        ["Alice Evans"],
        ["Dan Evans", "Ben Wade", "Alice Evans"],
    ),
    (
        ["Dan Evans", "Ben Wade", "Alice Evans"],
        ["Doc Potter", "Butterfield"],
        ["Dan Evans", "Ben Wade", "Alice Evans", "Doc Potter", "Butterfield"],
    ),
]

submit_cases = run_cases + [
    (
        ["Dan Evans", "Ben Wade", "Alice Evans"],
        [],
        ["Dan Evans", "Ben Wade", "Alice Evans"],
    ),
    ([], ["William Evans"], ["William Evans"]),
    (
        ["Dan Evans", "Ben Wade"],
        ["Charlie Prince", "Butterfield"],
        ["Dan Evans", "Ben Wade", "Charlie Prince", "Butterfield"],
    ),
]


def test(initial_docs, docs_to_add, expected_output):
    print("---------------------------------")
    print(f"Initial documents: {initial_docs}")
    print(f"Documents to add: {docs_to_add}")
    print(f"Expected: {expected_output}")
    copy_of_initial_docs = initial_docs.copy()
    add_doc = new_collection(initial_docs)
    result = initial_docs.copy()
    for doc in docs_to_add:
        result = add_doc(doc)
    print(f"Actual:   {result}")
    if copy_of_initial_docs != initial_docs:
        print("Fail: You should not modify the initial list")
        return False
    if result != expected_output:
        print("Fail: Unexpected result")
        return False
    print("Pass")
    return True


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
