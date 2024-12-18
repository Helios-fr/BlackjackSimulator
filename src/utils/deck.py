from .card import Card
from random import Random

class Deck:
    def __init__(self, decks: int = 1, seed: int = None):
        self.cards = [Card(suit, value) for suit in range(1, 5) for value in range(1, 14) for _ in range(decks)]
        self._random = Random(seed)
        self.shuffle()

    def shuffle(self) -> None:
        self._random.shuffle(self.cards)

    def draw(self, n: int = 1) -> list[Card]:
        if n > len(self.cards): raise ValueError("Not enough cards to draw")
        return [self.cards.pop() for _ in range(n)]

    def __str__(self) -> str:
        return [str(card) for card in self.cards].__str__()

    def __repr__(self) -> str:
        return str(self)

    def __len__(self) -> int:
        return len(self.cards)

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.draw(5))
    print(deck)
    print(len(deck))
    print(deck.draw(32))
    print(len(deck))



