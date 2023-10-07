import random

class Card:
    
    """ A Card will have a suit and a denominator. """

    def __init__(self, suit: str, denom: str, value: int = 0):
        self.suit: str = suit
        self.denom: str = denom
        self.value: int = value

    def __repr__(self):
        return f'Card: {self.denom} of {self.suit} with value: {self.value}'

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

players = []
deck = Deck()

for i in range(4):
    players.append(Player())

dealer = Dealer(deck, players)
dealer.deal(2)
print(dealer)
for player in dealer.players:
    print(player, player.showHand())