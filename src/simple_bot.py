class Bot:
    def __init__(self):
        self.capital = 1000

    def turn(self, player, dealer_card):
        if player.get_hand_value() < 16:
            return "Hit"
        else:
            return "Stand"

    def bet(self, deck):
        if self.capital < 10:
            return capital
        return 10