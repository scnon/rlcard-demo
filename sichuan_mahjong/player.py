class Player:
    """
    表示玩家的类
    """
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = []
        self.discard_pile = []
        self.peng_pile = []
        self.gang_pile = []

    def draw_card(self, deck):
        """
        玩家摸牌
        """
        self.hand.append(deck.draw())

    def discard_card(self, card):
        """
        玩家出牌，并检查是否可以进行碰、杠、胡操作
        """
        self.hand.remove(card)
        self.discard_pile.append(card)
        if self.can_peng(card):
            self.peng(card)
        if self.can_gang(card):
            self.gang(card)
        if self.can_hu():
            self.hu()

    def can_peng(self, card):
        """
        检查是否可以碰
        """
        return self.hand.count(card) >= 2

    def peng(self, card):
        """
        进行碰操作
        """
        self.hand.remove(card)
        self.hand.remove(card)
        self.peng_pile.append(card)

    def can_gang(self, card):
        """
        检查是否可以杠
        """
        return self.hand.count(card) == 3

    def gang(self, card):
        """
        进行杠操作
        """
        self.hand.remove(card)
        self.hand.remove(card)
        self.hand.remove(card)
        self.gang_pile.append(card)

    def can_hu(self):
        """
        检查是否可以胡
        """
        return len(self.hand) == 14 and self.has_valid_combination(self.hand)

    def hu(self):
        """
        进行胡操作
        """
        return True

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
