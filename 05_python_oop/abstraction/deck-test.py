from deck import *

run_cases = [
    ("shuffle_deck", 3, [("9", "Hearts"), ("Jack", "Clubs"), ("10", "Spades")]),
    (
        "deal_card",
        4,
        [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades"), ("10", "Spades")],
    ),
    ("deal_card", 3, [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades")]),
]

submit_cases = run_cases + [
    ("shuffle_deck", 3, [("9", "Hearts"), ("Jack", "Clubs"), ("10", "Spades")]),
    (
        "deal_card",
        4,
        [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades"), ("10", "Spades")],
    ),
    ("deal_card", 3, [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades")]),
    ("shuffle_deck", 3, [("9", "Hearts"), ("Jack", "Clubs"), ("10", "Spades")]),
    ("deal_card", 3, [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades")]),
    (
        "deal_card",
        53,
        [
            ("King", "Spades"),
            ("Queen", "Spades"),
            ("Jack", "Spades"),
            ("10", "Spades"),
            ("9", "Spades"),
            ("8", "Spades"),
            ("7", "Spades"),
            ("6", "Spades"),
            ("5", "Spades"),
            ("4", "Spades"),
            ("3", "Spades"),
            ("2", "Spades"),
            ("Ace", "Spades"),
            ("King", "Clubs"),
            ("Queen", "Clubs"),
            ("Jack", "Clubs"),
            ("10", "Clubs"),
            ("9", "Clubs"),
            ("8", "Clubs"),
            ("7", "Clubs"),
            ("6", "Clubs"),
            ("5", "Clubs"),
            ("4", "Clubs"),
            ("3", "Clubs"),
            ("2", "Clubs"),
            ("Ace", "Clubs"),
            ("King", "Diamonds"),
            ("Queen", "Diamonds"),
            ("Jack", "Diamonds"),
            ("10", "Diamonds"),
            ("9", "Diamonds"),
            ("8", "Diamonds"),
            ("7", "Diamonds"),
            ("6", "Diamonds"),
            ("5", "Diamonds"),
            ("4", "Diamonds"),
            ("3", "Diamonds"),
            ("2", "Diamonds"),
            ("Ace", "Diamonds"),
            ("King", "Hearts"),
            ("Queen", "Hearts"),
            ("Jack", "Hearts"),
            ("10", "Hearts"),
            ("9", "Hearts"),
            ("8", "Hearts"),
            ("7", "Hearts"),
            ("6", "Hearts"),
            ("5", "Hearts"),
            ("4", "Hearts"),
            ("3", "Hearts"),
            ("2", "Hearts"),
            ("Ace", "Hearts"),
            None,
        ],
    ),
]


def test(action, num_cards, expected):
    print("---------------------------------")
    print(f"Testing action: {action}, dealing {num_cards} cards")
    print(f"Expected Output:")
    print_cards(expected)
    deck = DeckOfCards()
    random.seed(1)
    result = []

    if action == "shuffle_deck":
        print("Shuffling deck...")
        deck.shuffle_deck()
        print(f"dealing {num_cards} cards")
        for _ in range(num_cards):
            result.append(deck.deal_card())

    elif action == "deal_card":
        for _ in range(num_cards):
            result.append(deck.deal_card())

    print(f"Actual Output:")
    print_cards(result)
    if result == expected:
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def print_cards(cards):
    for card in cards:
        if card is None:
            print("* <None>")
        else:
            print(f"* {card[0]} of {card[1]}")


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
