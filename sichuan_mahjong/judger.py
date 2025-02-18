class Judger:
    """
    表示裁判的类
    """
    def __init__(self):
        pass

    def judge(self, game):
        """
        判断游戏的赢家
        """
        winner = game.get_winner()
        if winner:
            return winner
        for player in game.players:
            if game.hu(player):
                return player
        return None
