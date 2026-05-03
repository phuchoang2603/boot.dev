import json
from main import Trie

run_cases = [
    (["Jerry", "Jess", "Jeremy"], "Je"),
    (["manifesto", "mantra", "management"], "man"),
]

submit_cases = run_cases + [
    (["Cush", "Rod", "Laurel"], ""),
    (["money"], "money"),
    (["contract", "conduit", "connection"], "con"),
]


def test(words, expected_prefix):
    print("---------------------------------")
    print("Trie:")
    trie = Trie()
    for word in words:
        trie.add(word)
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print(f'Expected: "{expected_prefix}"')
    try:
        actual = trie.longest_common_prefix()
        print(f'Actual: "{actual}"')
        if actual == expected_prefix:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
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
