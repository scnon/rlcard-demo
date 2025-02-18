from .dealer import Dealer
from .game import Game

class Round:
    """
    表示一局游戏的类
    """
    def __init__(self, players):
        self.players = players
        self.dealer = Dealer()
        self.dealer.shuffle()
        self.dealer.deal(self.players)

    def play(self):
        """
        进行一局游戏
        """
        game = Game()
        game.start()
        while not game.is_game_over():
            game.play_turn()
        return game.get_winner()
