# 1: Spades ♠
# 2: Hearts ♥
# 3: Diamonds ♦
# 4: Clubs ♣

class Card:
    def __init__(self, suit: int, value: int):
        if suit not in range(1, 5): raise ValueError("Invalid suit")
        if value not in range(1, 14): raise ValueError("Invalid value")

        self.suit = suit
        self.value = value

    def __str__(self):
        suits = {
            1: "♠",
            2: "♥",
            3: "♦",
            4: "♣"
        }

        values = {
            1: "A",
            11: "J",
            12: "Q",
            13: "K"
        }

        suit = suits[self.suit]
        value = values.get(self.value, self.value)

        return f"{value}{suit}"

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    card = Card(1, 1)
    print(card)  # A♠

    card = Card(2, 11)
    print(card)  # J♥

    card = Card(3, 12)
    print(card)  # Q♦

    card = Card(4, 13)
    print(card)  # K♣

    card = Card(5, 1)  # ValueError: Invalid suit
    card = Card(1, 14)  # ValueError: Invalid value