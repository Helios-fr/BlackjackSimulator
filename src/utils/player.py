class Player:
    def __init__(self):
        self.hand = []

    def add(self, cards):
        for card in cards:
            self.hand.append(card)

    def clear_hand(self):
        self.hand = []
    
    def get_hand_value(self):
        hand = sorted(self.hand, key=lambda x: x.value)[::-1]
        value = 0
        for card in self.hand:
            if card.value != 1 and card.value < 11:
                value += card.value
            elif card.value == 1:
                if value + 11 > 21:
                    value += 1
                else:
                    value += 11
            else:
                value += 10
        return value

    def __str__(self):
        return str(self.hand)

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    from card import Card

    player = Player()
    print(player)  # []
    
    player.add_card(Card(1, 1))
    print(player)  # [A♠]
    
    player.add_card(Card(2, 11))
    print(player)  # [A♠, J♥]
    print(player.get_hand_value())  # 21
    
    player.add_card(Card(3, 12))
    print(player)  # [A♠, J♥, Q♦]
    print(player.get_hand_value())  # 21
    
    player.add_card(Card(4, 13))
    print(player)  # [A♠, J♥, Q♦, K♣]
    print(player.get_hand_value())  # 31
    
    player.clear_hand()
    print(player)  # []
    
    player.add_card(Card(1, 1))
    player.add_card(Card(2, 11))
    player.add_card(Card(3, 12))
    player.add_card(Card(4, 13))
    print(player.get_hand_value())  # 41