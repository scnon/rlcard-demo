class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.suit}{self.rank}"


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['B', 'C', 'D'] for rank in range(1, 10)] * 4

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Player:
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
        # Simplified logic for discarding the first card in hand
        discarded_card = player.hand[0]
        player.discard_card(discarded_card)
        self.current_player = (self.current_player + 1) % 4

    def is_game_over(self):
        # Simplified game over condition
        return len(self.deck.cards) == 0

    def get_winner(self):
        # Simplified winner determination
        return max(self.players, key=lambda p: len(p.hand))


class Environment:
    def __init__(self):
        self.game = Game()

    def reset(self):
        self.game = Game()
        self.game.start()

    def step(self):
        self.game.play_turn()
        return self.game.is_game_over(), self.game.get_winner()


class Judger:
    def __init__(self):
        pass

    def judge(self, game):
        return game.get_winner()


class Dealer:
    def __init__(self):
        self.deck = Deck()

    def shuffle(self):
        self.deck.shuffle()

    def deal(self, players):
        for _ in range(13):
            for player in players:
                player.draw_card(self.deck)


class Round:
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
    @staticmethod
    def calculate_score(player):
        # Simplified score calculation
        return len(player.hand)
