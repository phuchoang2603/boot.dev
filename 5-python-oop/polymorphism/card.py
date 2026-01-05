SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        return (
            self.rank_index == other.rank_index and self.suit_index == other.suit_index
        )

    def __lt__(self, other):
        return self.rank_index < other.rank_index or (
            self.rank_index == other.rank_index and self.suit_index < other.suit_index
        )

    def __gt__(self, other):
        return self.rank_index > other.rank_index or (
            self.rank_index == other.rank_index and self.suit_index > other.suit_index
        )

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Round:
    def resolve_round(self):
        raise NotImplementedError("Subclasses must implement resolve_round()")


class HighCardRound(Round):
    def __init__(self, card1, card2) -> None:
        super().__init__()
        self.__card1 = card1
        self.__card2 = card2

    def resolve_round(self):
        if self.__card1 > self.__card2:
            return 1
        elif self.__card1 < self.__card2:
            return 2
        else:
            return 0


class LowCardRound(Round):
    def __init__(self, card1, card2) -> None:
        super().__init__()
        self.__card1 = card1
        self.__card2 = card2

    def resolve_round(self):
        if self.__card1 < self.__card2:
            return 1
        elif self.__card1 > self.__card2:
            return 2
        else:
            return 0
