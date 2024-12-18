class Bot:
    def __init__(self):
        self.capital = 1000

    def turn(self, player, dealer_card):
        hand_value = player.get_hand_value()
        if hand_value >= 17:
            return "Stand"
        elif hand_value >= 13 and dealer_card.value < 7:
            return "Stand"
        elif hand_value == 12 and 4 <= dealer_card.value <= 6:
            return "Stand"
        else:
            return "Hit"

    def bet(self, deck):
        if self.capital < 10:
            return capital
        return 10