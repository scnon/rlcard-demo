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
        return len(self.deck.cards) == 0 or any(self.check_victory(player) for player in self.players)

    def get_winner(self):
        # Improved winner determination based on Sichuan Mahjong rules
        for player in self.players:
            if self.check_victory(player):
                return player
        return None

    def check_victory(self, player):
        # Check if the player has a winning hand
        # This is a simplified version of the actual Sichuan Mahjong victory check
        # In a real implementation, you would need to check for specific winning patterns
        return len(player.hand) == 14 and self.has_valid_combination(player.hand)

    def has_valid_combination(self, hand):
        # Check if the hand has a valid combination of tiles
        # This is a simplified version of the actual Sichuan Mahjong combination check
        # In a real implementation, you would need to check for specific tile combinations
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
        # Calculate the score for a player based on their hand
        # This is a simplified version of the actual Sichuan Mahjong score calculation
        # In a real implementation, you would need to calculate the score based on specific tile combinations and patterns
        return len(player.hand)

    def get_scores(self):
        # Get the scores for all players
        return {player.player_id: self.calculate_score(player) for player in self.players}

    def peng(self, player, card):
        # Add logic for "碰" action
        if player.hand.count(card) >= 2:
            player.hand.remove(card)
            player.hand.remove(card)
            player.peng_pile.append(card)
            return True
        return False

    def gang(self, player, card):
        # Add logic for "杠" action
        if player.hand.count(card) == 3:
            player.hand.remove(card)
            player.hand.remove(card)
            player.hand.remove(card)
            player.gang_pile.append(card)
            return True
        return False

    def hu(self, player):
        # Add logic for "胡" action
        return self.check_victory(player)
