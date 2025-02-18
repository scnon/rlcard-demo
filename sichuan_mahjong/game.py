from .card import Card
from .player import Player
from .dealer import Dealer
from .judger import Judger

class Game:
    """
    表示游戏的类
    """
    def __init__(self):
        self.deck = Dealer().deck
        self.players = [Player(i) for i in range(4)]
        self.current_player = 0

    def start(self):
        """
        开始游戏，洗牌并发牌
        """
        self.deck.shuffle()
        for _ in range(13):
            for player in self.players:
                player.draw_card(self.deck)

    def play_turn(self):
        """
        进行一轮游戏，当前玩家摸牌并出牌
        """
        player = self.players[self.current_player]
        drawn_card = self.deck.draw()
        player.draw_card(drawn_card)
        # 简化的逻辑，丢弃手中的第一张牌
        discarded_card = player.hand[0]
        player.discard_card(discarded_card)
        self.current_player = (self.current_player + 1) % 4

    def is_game_over(self):
        """
        检查游戏是否结束
        """
        return len(self.deck.cards) == 0 or any(self.check_victory(player) for player in self.players)

    def get_winner(self):
        """
        获取游戏的赢家
        """
        for player in self.players:
            if self.check_victory(player):
                return player
        return None

    def check_victory(self, player):
        """
        检查玩家是否获胜
        """
        return len(player.hand) == 14 and self.has_valid_combination(player.hand)

    def has_valid_combination(self, hand):
        """
        检查手牌是否有有效的组合
        """
        def is_valid_set(tiles):
            return len(tiles) == 3 and (tiles[0] == tiles[1] == tiles[2] or
                                        tiles[0] + 1 == tiles[1] and tiles[1] + 1 == tiles[2])

        def is_valid_pair(tiles):
            return len(tiles) == 2 and tiles[0] == tiles[1]

        def can_form_melds(tiles):
            if not tiles:
                return True
            for i in range(len(tiles) - 2):
                if is_valid_set(tiles[i:i + 3]):
                    if can_form_melds(tiles[:i] + tiles[i + 3:]):
                        return True
            return False

        def can_form_pairs(tiles):
            if not tiles:
                return True
            for i in range(len(tiles) - 1):
                if is_valid_pair(tiles[i:i + 2]):
                    if can_form_pairs(tiles[:i] + tiles[i + 2:]):
                        return True
            return False

        hand.sort()
        return can_form_melds(hand) and can_form_pairs(hand)

    def calculate_score(self, player):
        """
        计算玩家的分数
        """
        return len(player.hand)

    def get_scores(self):
        """
        获取所有玩家的分数
        """
        return {player.player_id: self.calculate_score(player) for player in self.players}

    def peng(self, player, card):
        """
        处理玩家的碰操作
        """
        if player.hand.count(card) >= 2:
            player.hand.remove(card)
            player.hand.remove(card)
            player.peng_pile.append(card)
            return True
        return False

    def gang(self, player, card):
        """
        处理玩家的杠操作
        """
        if player.hand.count(card) == 3:
            player.hand.remove(card)
            player.hand.remove(card)
            player.hand.remove(card)
            player.gang_pile.append(card)
            return True
        return False

    def hu(self, player):
        """
        处理玩家的胡操作
        """
        return self.check_victory(player)
