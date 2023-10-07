from player import Player
from dealer import Dealer
from deck import Deck

players = []
deck = Deck()

for i in range(4):
    players.append(Player())

dealer = Dealer(deck, players)
dealer.deal(2)
print(dealer)
print(dealer.showHand())
for player in dealer.players:
    print(player, player.showHand())