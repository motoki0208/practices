from oop.e1.cards import Deck, MARKS, CARD_NUMBERS, BlackJackCard
from oop.e1.participants import Dealer, Player, Participant


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