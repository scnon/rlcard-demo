class Card:
    """
    表示麻将牌的类
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.suit}{self.rank}"


class Deck:
    """
    表示一副麻将牌的类
    """
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['B', 'C', 'D'] for rank in range(1, 10)] * 4

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Player:
    """
    表示玩家的类
    """
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = []
        self.discard_pile = []

    def draw_card(self, deck):
        self.hand.append(deck.draw())

    def discard_card(self, card):
        self.hand.remove(card)
        self.discard_pile.append(card)


class Game:
    """
    表示游戏的类
    """
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(i) for i in range(4)]
        self.current_player = 0

    def start(self):
        self.deck.shuffle()
        for _ in range(13):
            for player in self.players:
                player.draw_card(self.deck)

    def play_turn(self):
        player = self.players[self.current_player]
        drawn_card = self.deck.draw()
        player.draw_card(drawn_card)
        # 简化的逻辑，丢弃手中的第一张牌
        discarded_card = player.hand[0]
        player.discard_card(discarded_card)
        self.current_player = (self.current_player + 1) % 4

    def is_game_over(self):
        # 简化的游戏结束条件
        return len(self.deck.cards) == 0

    def get_winner(self):
        # 简化的赢家确定
        return max(self.players, key=lambda p: len(p.hand))


class Environment:
    """
    表示游戏环境的类
    """
    def __init__(self):
        self.game = Game()

    def reset(self):
        self.game = Game()
        self.game.start()

    def step(self):
        self.game.play_turn()
        return self.game.is_game_over(), self.game.get_winner()


class Judger:
    """
    表示裁判的类
    """
    def __init__(self):
        pass

    def judge(self, game):
        return game.get_winner()


class Dealer:
    """
    表示庄家的类
    """
    def __init__(self):
        self.deck = Deck()

    def shuffle(self):
        self.deck.shuffle()

    def deal(self, players):
        for _ in range(13):
            for player in players:
                player.draw_card(self.deck)


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
        game = Game()
        game.start()
        while not game.is_game_over():
            game.play_turn()
        return game.get_winner()


class Utils:
    """
    工具类，包含一些静态方法
    """
    @staticmethod
    def calculate_score(player):
        # 简化的分数计算
        return len(player.hand)
