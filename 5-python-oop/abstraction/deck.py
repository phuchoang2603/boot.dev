import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = (rank, suit)
                self.__cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if len(self.__cards) == 0:
            return None
        else:
            return self.__cards.pop()

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
