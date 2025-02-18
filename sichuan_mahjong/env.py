from .game import Game

class Env:
    """
    表示游戏环境的类
    """
    def __init__(self):
        self.game = Game()

    def reset(self):
        """
        重置游戏环境
        """
        self.game = Game()
        self.game.start()

    def step(self):
        """
        进行一步游戏
        """
        self.game.play_turn()
        return self.game.is_game_over(), self.game.get_winner()
