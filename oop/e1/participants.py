from oop.e1.cards import Hand, Deck


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