class Utils:
    """
    工具类，包含一些静态方法
    """
    @staticmethod
    def calculate_score(player):
        """
        计算玩家的分数
        """
        return len(player.hand)
