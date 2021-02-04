class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return "{p} deck:\n {p_deck}".format(p=self.name, p_deck=self.hand)

    def play_card(self):
        play_card = self.hand.remove_from_hand()
        return play_card

    def play_war_card(self):
        war_cards = []

        for i in range(3):
            war_cards.append(self.hand.cards_in_hand.pop(0))

        return war_cards