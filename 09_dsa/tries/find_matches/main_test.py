import json
from main import Trie

run_cases = [
    (
        ["synergy", "alignment", "leverage", "bandwidth"],
        "Let's leverage our synergy to realign our bandwidth",
        ["synergy", "leverage", "bandwidth"],
    ),
    (
        ["circle", "back", "touch", "base"],
        "Let's circle back to touch base",
        ["circle", "back", "touch", "base"],
    ),
]

submit_cases = run_cases + [
    (
        ["pivot", "innovate", "scalable", "proactive"],
        "We need to pivot and innovate for truly scalable solutions",
        ["pivot", "innovate", "scalable"],
    ),
]


def test(words, document, expected_matches):
    print("---------------------------------")
    print("Trie:")
    trie = Trie()
    for word in words:
        trie.add(word)
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print(f"Expected matches: {sorted(expected_matches)}")
    try:
        actual = sorted(trie.find_matches(document))
        print(f"Actual matches: {actual}")
        if actual == sorted(expected_matches):
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
