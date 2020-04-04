from oop.e1.games import BlackJackGame
from oop.e1.participants import Player, Dealer

if __name__ == "__main__":
    dealer = Dealer("dealer1")
    player = Player("player1")
    game = BlackJackGame(dealer, player)
    game.start()
