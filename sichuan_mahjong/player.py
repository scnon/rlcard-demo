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
