#!/usr/bin/env python3
from random import random as rnd


def title():
    print("")
    print((21 * " ") + "Acey Ducey card game")
    print((15 * " ") + "Python version by Marc Brevoort")
    print("")
    print("Acey Ducey is played in the following manner.")
    print("The dealer (computer) deals two cards face up")
    print("You have an option to bet or not to bet, depending")
    print("on whether or not you feel the card will have ")
    print("a value between the first two.")
    print("If you do not want to bet, input a 0.")


def pick_a_card():
    return int(13 * rnd()) + 2


def pick_two_cards():
    while True:
        card_1 = pick_a_card()
        card_2 = pick_a_card()

        if card_1 == card_2:
            # They're the same! Keep picking cards
            # until we find two different ones
            continue

        break

    if card_1 > card_2:
        # First card is higher than the second,
        # Swap them around.
        return card_2, card_1

    return card_1, card_2


def cardname(card):
    card_names = (
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    )
    return card_names[card - 2]


def ask_bet_amount(player_money):
    while True:
        bet = input("What is your bet?")
        if bet.strip() == "":
            continue
        bet_amount = round(float(bet) * 100) / 100

        if bet_amount > player_money:
            # We keep asking how much until we get
            # an answer that is low enough.
            print("Sorry, my friend but you bet too much")
            print("You have only {} dollars to bet".format(player_money))
            continue

        if bet_amount < 0:
            print("Negative bets are not allowed!")
            continue

        break

    return round(float(bet_amount) * 100) / 100


def play_one_round(player_money):
    print("You now have {} dollars".format(player_money))
    print("")

    print("Here are your next two cards: ")
    a, b = pick_two_cards()
    print(cardname(a))
    print(cardname(b))

    bet_amount = ask_bet_amount(player_money)
    if bet_amount == 0:
        print("Chicken!")
        return player_money

    c = pick_a_card()
    print(cardname(c))

    if c > a and c < b:
        print("You win!")
        return player_money + bet_amount

    print("Sorry, you lose")
    return player_money - bet_amount


def play_one_game():
    player_money = 100

    while True:
        player_money = play_one_round(player_money)
        if player_money > 0:
            # We keep going as long as the player has money
            continue

        # But after that, the game is over.
        break

    return


title()
while True:
    play_one_game()

    # The game always ends
    # with the player losing all their money
    print("")
    print("Sorry, friend but you blew your wad")

    again = input("Try again (Yes or No)?") or "N"
    if again.upper()[0] != "Y":
        print("OK hope you had fun")
        break
