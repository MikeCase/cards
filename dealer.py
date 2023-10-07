from deck import Deck
from player import Player

class Dealer(Player):

    """ Dealer will deal the cards to the players. """

    def __init__(self, deck: Deck, players: []) -> None:
        super().__init__()
        self.is_dealer: bool = True
        self.deck: Deck = deck
        self.players: [Player] = players

    def deal(self, count: int) -> None:
        """ Deal a card to a player """
        while count > 0:
            self.takeCard(self.deck.deck.pop(0))
            for player in self.players:
                if not self.deck.deck:
                    print("The deck is empty.")
                    return
                # get a card from the top of the deck 
                card = self.deck.deck.pop(0)
                # Give the card to the player
                player.takeCard(card)
            count -= 1
                
    def __repr__(self) -> str:
        return super().__repr__()