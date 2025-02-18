from .card import Card
from .player import Player
from .dealer import Dealer
from .judger import Judger

class Game:
    def __init__(self):
        self.deck = Dealer().deck
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
