from deck import Deck as d
from hand import Hand as h
from player import Player as p

######################
#### GAME PLAY #######
######################
SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

# generate, shuffle and divide deck by 2 for 2 player2
def generate_deck():
    d1 = d()
    d1.shuffle_deck()
    p1_deck, p2_deck = d1.divided_deck()
    return (p1_deck, p2_deck)


# generate 2 players with 2 deck generated. Player1 is user, Player2 is computer


def generate_player():

    gen_deck = generate_deck()
    hand1 = h(gen_deck[0])
    hand2 = h(gen_deck[1])

    input_name = input("Enter player name: ")
    player1 = p(input_name, hand1)
    player2 = p("machine", hand2)
    return (player1, player2)


# game end if 1 of 2 players has empty hand
def is_game_end(p1, p2):
    return p1.hand.is_hand_empty() or p2.hand.is_hand_empty()


# message display how many cards left of each user at start of the round
def game_start_message(p1, p2):
    print("\n-------------------------------\n")
    print("It's time to start a new round!")
    print(p1)
    print(p2)
    print("\n-------------------------------\n")


# ask user enter y to place a card
def ask_user():
    check = input("enter y to place a card (y): ").lower().strip()

    try:
        if check == "y":
            return True
    except Exception as err:
        print("please enter y only")
        print(err)

    return False


# player turn, place a card
def player_turn(p):
    print("\nIt's {} turn!".format(p.name))
    check = ask_user()

    while not check:
        check = ask_user()

    card = p.play_card()

    return card


# computer turn, auto place a card after user play
def computer_turn(p):
    print("\nIt's computer turn")

    card = p.play_card()

    return card


# check rank of 2 cards. If it's a same rank then it's a war
def is_a_war(p1_card, p2_card):
    return RANKS.index(p1_card[1]) == RANKS.index(p2_card[1])


# display war message
def display_war_message():
    print("\n----------------------------WAR------------------------------\n")
    print("We have a match, time for war!")
    print("Each player removes 3 cards 'face down' and then one card face up")
    print("\n----------------------------WAR------------------------------\n")


# add to hand
def add_to_hand():
    pass


def start_round():
    gen_player = generate_player()
    p1 = gen_player[0]
    p2 = gen_player[1]
    table_cards = []
    wars_count = 0
    wars_p1_win = 0
    wars_p2_win = 0

    while not is_game_end(p1, p2):
        # welcome to new round, display how many card left
        game_start_message(p1, p2)

        # both player play a card
        p_card = player_turn(p1)
        c_card = computer_turn(p2)

        # add to table cards
        table_cards.append(p_card)
        table_cards.append(c_card)

        # check war
        if is_a_war(p_card, c_card):
            wars_count += 1
            display_war_message()
            table_cards.extend(p1.play_war_card())
            table_cards.extend(p2.play_war_card())

            # after set 3 cards face down, both player play 1 card
            p_card = player_turn(p1)
            c_card = computer_turn(p2)

            # add to table cards
            table_cards.append(p_card)
            table_cards.append(c_card)
            # if not a war, check rank of 2 cards play like normal
            if RANKS.index(p_card[1]) < RANKS.index(c_card[1]):
                wars_p2_win += 1
                print("\n{} has higher rank, adding cards to hand".format(p2.name))
                p2.hand.add_to_hand(table_cards)
            else:
                wars_p1_win += 1
                print("\n{} has higher rank, adding cards to hand".format(p1.name))
                p1.hand.add_to_hand(table_cards)
            table_cards.clear()
        else:
            if RANKS.index(p_card[1]) < RANKS.index(c_card[1]):
                print("\n{} has higher rank, adding cards to hand".format(p2.name))
                p2.hand.add_to_hand(table_cards)
            else:
                print("\n{} has higher rank, adding cards to hand".format(p1.name))
                p1.hand.add_to_hand(table_cards)
            table_cards.clear()
    print("\nGame ended\n")

    # message who win
    if not p1.hand.is_hand_empty():
        print("{} win!".format(p1.name))
    else:
        print("{} win!".format(p2.name))

    # print how many wars each player win
    print("\nThere are total {} wars".format(wars_count))
    print("\n{} wins {} wars!".format(p1.name, wars_p1_win))
    print("\n{} wins {} wars!".format(p2.name, wars_p2_win))


def play():

    print("\nWelcome to War, let's begin...\n")

    start_round()


play()