import random
from typing import List

MARKS = ["HEART", "SPADE", "DIAMOND", "CLUB"]
CARD_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
PICUTURE_CARD_NUMBERS = [10, 11, 12, 13]
ACE_NUMBER = 1


class CardEmptyError(Exception):
    pass


class Card:
    mark: str
    number: int

    def __init__(self, mark: str, number: int):
        if mark not in MARKS:
            raise ValueError

        if number not in CARD_NUMBERS:
            raise ValueError

        self.mark = mark
        self.number = number

    @property
    def score(self):
        return NotImplementedError()


class BlackJackCard(Card):
    @property
    def score(self):
        if self.number in PICUTURE_CARD_NUMBERS:
            return 10

        if self.number == ACE_NUMBER:
            return self.ace_score

        return self.number

    @property
    def ace_score(self):
        answer = None
        while answer not in ["one", "ten"]:
            answer = input("Which do you choose 1 or 10 as ace's score? 1 => one, 10 => ten")

        return 1 if answer == "one" else 10


class Deck:
    def __init__(self, cards: List[Card]):
        self.__cards = cards

    def shuffle(self):
        random.shuffle(self.__cards)
        return

    def give_first_card(self) -> Card:
        if not self.__cards:
            raise CardEmptyError()

        return self.__cards.pop(0)


class Hand:
    __cards: List[Card]

    def __init__(self):
        self.__cards = []

    def add_card(self, card):
        self.__cards.append(card)

    def show_card_numbers(self):
        numbers = [card.number for card in self.__cards]
        return numbers

    def show_first_card_number(self):
        if not self.__cards:
            raise CardEmptyError()

        return self.__cards[0].number

    @property
    def total_score(self):
        total = 0
        for card in self.__cards:
            total += card.number
        return total