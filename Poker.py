class Poker:
    def __init__(self, player, table, deck):
        self.player = player
        self.player.hand = []
        self.table = table
        self.deck = deck
        for i in range(0, 4):
            self.player.hand.append(i)


rank = ["A", "2","3","4","5","6","7","8","9","T","J","Q","K"]
suit = ["S", "D", "C", "H"]

cards = []

for i in rank:
    for j in suit:
        cards.append(i + j)

print(cards)