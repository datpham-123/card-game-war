from deck import Deck as d
from hand import Hand as h
from player import Player as p

######################
#### GAME PLAY #######
######################


def generate_deck():
    d1 = d()
    d1.shuffle_deck()
    p1_deck, p2_deck = d1.divided_deck()
    return (p1_deck, p2_deck)


def generate_player():

    gen_deck = generate_deck()
    input_name = input("Enter player name: ")
    player1 = p(input_name, gen_deck[0])
    player2 = p("machine", gen_deck[1])
    return (player1, player2)


gen_player = generate_player()
p1 = gen_player[0]
p2 = gen_player[1]

print(p1.hand.is_hand_empty())
print(p2)


def is_game_end(p1, p2):
    return p1.hand.is_hand_empty() or p2.hand.is_hand_empty()


def game_start_message(p1, p2):
    print("\nIt's time to start a new round!")
    print(
        "\n{p1} have {p1_cards} cards left!".format(p1=p1, p1_cards=len(p1.hand.cards))
    )
    print(
        "\n{p2} have {p2_cards} cards left!".format(p1=p2, p2_cards=len(p2.hand.cards))
    )
    print("\nnoth player draw a card\n")


def start_round():
    gen_player = generate_player()
    p1 = gen_player[0]
    p2 = gen_player[1]

    while not is_game_end(p1, p2):
        game_start_message(p1, p2)


def play():

    print("\nWelcome to War, let's begin...\n")

    start_round()


# play()