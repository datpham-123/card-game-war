from random import shuffle

SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        print("\nGENERATING DECK OF 52 CARDS\n")
        self.deck = [(s, r) for s in SUITE for r in RANKS]

    def __str__(self):
        return "Deck generated:\n{}".format(self.deck)

    def shuffle_deck(self):
        print("SHUFFLING DECK....\n")
        shuffle(self.deck)

    def divided_deck(self):
        print("DIVIDE DECK BY 2, EACH PLAYER HAVE 26 CARDS!\n")
        return (self.deck[:26], self.deck[26:])