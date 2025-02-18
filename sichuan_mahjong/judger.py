class Judger:
    def __init__(self):
        pass

    def judge(self, game):
        winner = game.get_winner()
        if winner:
            return winner
        for player in game.players:
            if game.hu(player):
                return player
        return None
