from .card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['B', 'C', 'D'] for rank in range(1, 10)] * 4

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Dealer:
    def __init__(self):
        self.deck = Deck()

    def shuffle(self):
        self.deck.shuffle()

    def deal(self, players):
        for _ in range(13):
            for player in players:
                player.draw_card(self.deck)
