from .game import Game

class Env:
    def __init__(self):
        self.game = Game()

    def reset(self):
        self.game = Game()
        self.game.start()

    def step(self):
        self.game.play_turn()
        return self.game.is_game_over(), self.game.get_winner()
