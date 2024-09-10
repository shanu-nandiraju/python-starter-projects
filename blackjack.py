import random
import art

def over_21():
    if sum(player_cards) > 21:
        ace(player_cards)
        if sum(player_cards) > 21:
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
            print("You went over. You lose 😭")
            return True
    return False

def ace(deck):
    while 11 in deck and sum(deck) > 21:
        deck[deck.index(11)] = 1

def display():
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {dealer_cards[0]}")

def add_card(deck):
    deck.append(random.choice(cards))

def initialize_decks():
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

def immediate_blackjack():
    if len(dealer_cards) == 2 and (11 in dealer_cards) and (10 in dealer_cards):
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {dealer_cards}, final score: 0")
        print("Lose, opponent has Blackjack 😱")
        return True
    elif len(player_cards) == 2 and (11 in player_cards) and (10 in player_cards):
        print(f"Your final hand: {player_cards}, final score: 0")
        print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
        print("Win with a Blackjack 😎")
        return True
    return False

def dealer():
    while sum(dealer_cards) < 17:
        add_card(dealer_cards)
    ace(dealer_cards)
    return sum(dealer_cards)

def comparison():
    dealer_score = dealer()
    player_score = sum(player_cards)
    if dealer_score > 21:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("Opponent went over. You win 😁")
    elif player_score > 21:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("You went over. You lose 😭")
    elif dealer_score == player_score:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("Draw 🙃")
    elif dealer_score > player_score:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("You lose 😤")
    else:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("You win 😃")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

for count in range(100):
    player_cards = []
    dealer_cards = []
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play.lower() == "y":
        print("\n" * 100)
        print(art.logo)
        initialize_decks()
        display()
        if immediate_blackjack():
            continue
        while True:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card.lower() == "n":
                break
            else:
                add_card(player_cards)
                ace(player_cards)
                display()
                if over_21():
                    break
        comparison()
