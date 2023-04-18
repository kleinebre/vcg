#!/usr/bin/env python
from __future__ import print_function

PLAYER_HOME = 6
COMPUTER_HOME = 13

movecounter = 0
gamenum = 0


def title():
    print((34 * " ") + "Awari")
    print((22 * " ") + "Python version by Marc Brevoort")


def print_board(bowl):
    print("")
    print(" " * 13, end="")

    for i in range(0, 6):
        print(str(bowl[12 - i]).rjust(3), end="")

    print("")
    print(str(bowl[13]).rjust(13), end="")
    print(19 * " ", end="")
    print(str(bowl[6]).rjust(3))

    print(" " * 13, end="")
    for i in range(0, 6):
        print(str(bowl[i]).rjust(3), end="")

    print("")
    print("")
    return


def play_the_move(bowl, homebowl, move, show=False):
    global PLAYER_HOME
    global COMPUTER_HOME
    start_move = move

    p = bowl[move]
    bowl[move] = 0
    for r in range(0, p):
        move = (move + 1) % 14
        if move == PLAYER_HOME and start_move > PLAYER_HOME:
            # Computer doesn't give beans to player pot
            continue
        if move == COMPUTER_HOME and start_move < PLAYER_HOME:
            # Player doesn't give beans to computer pot
            continue

        bowl[move] += 1

        if show:
            print_board(bowl)

    if bowl[move] != 1:
        # last one landed in a nonempty bowl, end the move.
        return bowl, move

    if move == PLAYER_HOME:
        return bowl, move
    if move == COMPUTER_HOME:
        return bowl, move
    if bowl[12 - move] == 0:
        return bowl, move

    if (start_move < PLAYER_HOME and move < PLAYER_HOME) or (
        start_move > PLAYER_HOME and move > PLAYER_HOME
    ):
        # grab opposite beans only if landing in an empty bowl
        # on own side
        bowl[homebowl] += 1 + bowl[12 - move]
        bowl[move] = 0
        bowl[12 - move] = 0

    return bowl, move


def have_empty_side(bowl):
    """
    When either side is empty, the game is finished.
    """
    for i in range(0, 6):
        if bowl[i]:
            """Player side not empty. check comp side"""
            for i in range(7, 13):
                if bowl[i]:
                    return False

    return True


def player_move(bowl):
    global movecounter, gamenum
    again = False
    while True:
        if again:
            print("Again? ", end="")
        again = True

        try:
            rawmove = input("")
            move = int(rawmove)
        except TypeError:
            move = 0

        if rawmove and rawmove.upper()[0] == "Q":
            # quit
            exit(0)

        legal = False
        if move >= 1 and move <= 6:
            move -= 1
            if bowl[move] != 0:
                legal = True

        if not legal:
            print("Illegal move")
            continue

        keep = move
        bowl, move = play_the_move(bowl, PLAYER_HOME, move)
        print_board(bowl)
        keep = keep % 7

        movecounter = movecounter + 1
        if movecounter < 9:
            # change computer strategy depending on no. of moves played
            f[gamenum] *= 6 + keep

        se = have_empty_side(bowl)
        if se:
            break
        if move != PLAYER_HOME:
            break

        # Ended up in home bowl - play another move

    return bowl, se


def move_score(bowl, j):
    # verify the result of this move
    global movecounter
    global gamenum
    q = 0
    # verify the result of this move
    for i in range(0, 6):
        if bowl[i] == 0:
            continue

        l = bowl[i] + i
        r = 0
        if l > 13:
            l = l % 14
            r = 1

        if bowl[l] == 0:
            if l != PLAYER_HOME:
                if l != COMPUTER_HOME:
                    r = bowl[12 - l] + r
        if r > q:
            q = r

    q = bowl[COMPUTER_HOME] - bowl[PLAYER_HOME] - q
    if movecounter <= 8:
        k = j
        if k > 6:
            k -= 7
        for i in range(0, gamenum):
            if f[gamenum] * 6 + k == int(f[i] / 6 ^ (7 - movecounter) + 0.1):
                q -= 2
    return q


def computer_move(bowl):
    global PLAYER_HOME
    global COMPUTER_HOME

    while True:
        save = [0 for x in range(0, 14)]
        best_so_far_move = 0
        best_so_far_score = -99
        for i in range(0, 14):
            save[i] = bowl[i]

        # try moves
        for j in range(7, 13):
            if bowl[j] == 0:
                continue

            bowl, move = play_the_move(bowl, COMPUTER_HOME, j)
            score = move_score(bowl, j)

            if score >= best_so_far_score:
                best_so_far_move = j
                best_so_far_score = score

            # restore playing field
            for i in range(0, 14):
                bowl[i] = save[i]

        move = best_so_far_move
        print(chr(42 + move), end="")

        bowl, move = play_the_move(bowl, COMPUTER_HOME, move)

        se = have_empty_side(bowl)
        if se:
            break

        if move != COMPUTER_HOME:
            break

        print(", ", end="")

    return bowl, se


title()
gamenum = 0
while True:

    bowl = [3 for x in range(0, 14)]
    bowl[COMPUTER_HOME] = 0
    bowl[PLAYER_HOME] = 0

    g = [0 for x in range(0, 13)]
    f = [0 for x in range(0, 50)]

    print("")
    print("")
    movecounter = 0
    f[gamenum] = 0
    bowl[13] = 0
    bowl[6] = 0

    while True:
        print_board(bowl)

        print("Your move? ", end="")
        bowl, side_empty = player_move(bowl)
        if side_empty:
            break

        print("My move is ", end="")
        bowl, side_empty = computer_move(bowl)
        if side_empty:
            break

    print("")
    print_board(bowl)
    print("Game over")
    diff = bowl[PLAYER_HOME] - bowl[COMPUTER_HOME]
    if diff < 0:
        print("I win by %s points" % -diff)
    else:
        gamenum += 1
        if diff == 0:
            print("Drawn game")
        else:
            print("You win by %s points" % diff)

    again = input("Play again (Yes or No)? ")
    if again.upper()[0] != "Y":
        print("Okay, hope you had fun!")
        exit(0)
