import random

class Bot:
    def __init__(self):
        self.capital = 1000  # Starting balance

    def count_face_cards(self, deck):
        face_cards = 0
        for card in deck:
            if card.value >= 10:
                face_cards += 1
        return face_cards

    def bet(self, deck):
        face_card_count = self.count_face_cards(deck)
        if face_card_count > len(deck)*0.3:
            return min(self.capital, 100)  # Bet higher if there are more face cards
        else:
            return min(self.capital, 10)  # Bet lower if there are fewer face cards

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