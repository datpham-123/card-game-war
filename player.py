class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return "\n{} have {} cards".format(self.name, self.hand.cards_left())

    def play_card(self):
        play_card = self.hand.remove_from_hand()
        print("{} have been placed!".format(play_card))
        return play_card

    def play_war_card(self):
        war_cards = []

        if len(self.hand.cards) >= 3:
            for i in range(3):
                war_cards.append(self.hand.cards.pop(0))

        return war_cards