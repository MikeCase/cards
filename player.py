from card import Card

class Player:

    """ Player will have a hand. """

    def __init__(self, hand: [] = None):
        self.hand = hand if hand is not None else []
        self.is_dealer = False
        self.is_human = False
        
    def takeCard(self, card: Card) -> None:
        self.hand.append(card)

    def showHand(self) -> list:
        return self.hand[0], self.hand[1]
    
    def __repr__(self) -> str:
        return f"I'm {'the dealer' if self.is_dealer else 'a player'}"