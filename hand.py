class Hand:
    """
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    """

    def __init__(self, cards):
        self.cards = cards

    def cards_left(self):
        return len(self.cards)

    def is_hand_empty(self):
        return self.cards_left() == 0

    def add_to_hand(self, list_card):
        return self.cards.extend(list_card)

    def remove_from_hand(self):
        return self.cards.pop()

    def __str__(self):
        return "You have {cards_left} cards left\nYour hand is {nums_card}\n".format(
            cards_left=self.cards_left(),
            nums_card=self.cards,
        )
