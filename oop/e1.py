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


class Participant:
    hand: Hand

    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def draw_card(self, deck: Deck):
        card = deck.give_first_card()
        self.hand.add_card(card)

    @staticmethod
    def decide_draw(self):
        return NotImplementedError()

    @property
    def total_score(self):
        return self.hand.total_score

    @property
    def show_card(self):
        return self.hand.show_card_numbers()


class Player(Participant):

    def decide_draw(self):
        answer = None
        while answer not in ["y", "n"]:
            answer = input("Do you draw card? y/n\n")

        if answer == "y":
            return True
        else:
            return False


class Dealer(Participant):
    THRESHOLD = 17

    @property
    def has_to_draw(self):
        if self.hand.total_score < 17:
            return True
        return False

    def decide_draw(self, player_total_score):
        if self.has_to_draw:
            return True

        if self.hand.total_score <= player_total_score:
            return True

        return False

    def show_first_card(self):
        return self.hand.show_first_card_number()


class BlackJackGame:
    dealer: Dealer
    player: Player
    deck: Deck

    def __init__(self, dealer: Dealer, player: Player):
        self.dealer = dealer
        self.player = player
        self.deck = self._get_deck()

    @staticmethod
    def _get_deck() -> Deck:
        cards = []
        for mark in MARKS:
            for number in CARD_NUMBERS:
                card = BlackJackCard(mark, number)
                cards.append(card)

        deck = Deck(cards)
        deck.shuffle()
        return deck

    @staticmethod
    def check_excess(participant: Participant):
        if participant.total_score > 21:
            print(f"{participant.name} lose! {participant.name}'s total score has exceeded 21")
            return True

    def start(self):
        for _ in range(2):
            self.dealer.draw_card(self.deck)
            self.player.draw_card(self.deck)

        print(f"{self.dealer.name}: {self.dealer.show_first_card()}")
        print(f"{self.player.name}: {self.player.show_card}")

        while self.player.decide_draw():
            self.player.draw_card(self.deck)
            print(f"{self.player.name}: {self.player.show_card}")
            if self.check_excess(self.player):
                return

        while self.dealer.decide_draw(self.player.total_score):
            self.dealer.draw_card(self.deck)
            print(f"{self.dealer.name}: {self.dealer.show_card}")
            if self.check_excess(self.dealer):
                return

        print(f"{self.player.name} lose!")
        print(f"player's score {self.player.total_score}")
        print(f"dealer's score {self.dealer.total_score}")


if __name__ == "__main__":
    dealer = Dealer("dealer1")
    player = Player("player1")
    game = BlackJackGame(dealer, player)
    game.start()
