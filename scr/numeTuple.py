
import collections
import random

Card = collections.namedtuple("Card", ["rank", "suit"])

class Coloda:
    """
    >>> coloda = Coloda()
    >>> for c in coloda:
    ...     print(c)

    >>> Card("2", "бубна") in coloda
    >>>
    """
    ranks = [str(x) for x in range(2, 11)] + list("VDKT")
    suit = "бубна крест пика чирва".split()
    def __init__(self):
        self._cards = [Card(r, s) for s in self.suit for r in self.ranks]


    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


if __name__ == '__main__':
    suit_values = dict(бубна=3, крест=2, пика=1, чирва=0)

    def spades_high(card):
        rank_value = Coloda.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]


    c = Coloda()
    # for card in sorted(c, key=spades_high, reverse=True):
    #     print(card)
    print(c[12::13])