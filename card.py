class Card:
    
    """ A Card will have a suit and a denominator. """

    def __init__(self, suit: str, denom: str, value: int = 0):
        self.suit: str = suit
        self.denom: str = denom
        self.value: int = value

    def __repr__(self):
        return f'Card: {self.denom} of {self.suit} with value: {self.value}'