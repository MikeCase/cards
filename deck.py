import random
from card import Card

class Deck:

    """ Deck will have 52 cards. """

    def __init__(self):
        self.deck = []
        self.suits = ['\u2660', '\u2663', '\u2665', '\u2666']
        self.denoms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.values = [2,3,4,5,6,7,8,9,10,10,10,10,1]
        self._build_deck()

    def _build_deck(self):
        self.deck = [Card(suit, denom, value=value) for suit in self.suits for denom,value in zip(self.denoms, self.values)]
        self._shuffle_deck()

    def _shuffle_deck(self):
        random.shuffle(self.deck)

    def __repr__(self):
        return self.deck