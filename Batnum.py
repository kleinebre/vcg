#!/usr/bin/env python3
def title():
    print(" " * 33 + "BATNUM")
    print(" " * 15 + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
    print("\n\n")
    print("THIS PROGRAM IS A 'BATTLE OF NUMBERS' GAME, WHERE THE")
    print("COMPUTER IS YOUR OPPONENT.")
    print()
    print("THE GAME STARTS WITH AN ASSUMED PILE OF OBJECTS. YOU")
    print("AND YOUR OPPONENT ALTERNATELY REMOVE OBJECTS FROM THE PILE.")
    print("WINNING IS DEFINED IN ADVANCE AS TAKING THE LAST OBJECT OR")
    print("NOT. YOU CAN ALSO SPECIFY SOME OTHER BEGINNING CONDITIONS.")
    print("DON'T USE ZERO, HOWEVER, IN PLAYING THE GAME.")
    print("ENTER A NEGATIVE NUMBER FOR NEW PILE SIZE TO STOP PLAYING.")
    print()

def print_new_lines():
    for i in range(10):
        print()

def get_valid_pile_size():
    while True:
        n = input("ENTER PILE SIZE: ")
        try:
            n = int(n)
        except ValueError:
            print_new_lines()
            continue
        if n < 1 or n != int(n):
            print_new_lines()
            continue
        return n

def get_valid_win_option():
    while True:
        m = input("ENTER WIN OPTION - 1 TO TAKE LAST, 2 TO AVOID LAST: ")
        try:
            m = int(m)
        except ValueError:
            continue
        if m == 1 or m == 2:
            return m

def get_valid_min_max():
    while True:
        a, b = input("ENTER MIN AND MAX: ").split(",")
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            continue
        if a > b or a < 1 or a != int(a) or b != int(b):
            continue
        return a, b

def who_starts():
    while True:
        s = input("ENTER START OPTION - 1 COMPUTER FIRST, 2 YOU FIRST: ")
        try:
            s = int(s)
        except ValueError:
            continue
        if s == 1 or s == 2:
            return s

def play_game(n, m, a, b, s):
    c = a + b
    if s == 1:
        first_player_move = computer_move
        second_player_move = player_move
    else:
        first_player_move = player_move
        second_player_move = computer_move

    print_new_lines()
    while True:
        w, n = first_player_move(n, m, a, b, c)
        if w == 1:
            print_new_lines()
            return
        w, n = second_player_move(n, m, a, b, c)
        if w == 1:
            print_new_lines()
            return

def computer_move(n, m, a, b, c):
    q = n
    if m != 1:
        q = q - 1
    if m != 1 and n <= a:
        w = 1
        print("COMPUTER TAKES", n, "AND LOSES.")
        return w, n
    if n >= a and n <= b:
        w = 1
        print("COMPUTER TAKES", n, "AND WINS.")
        return w, n
    p = q - c * (q // c)
    if p < a:
        p = a
    elif p > b:
        p = b
    n = n - p
    print("COMPUTER TAKES", p, "AND LEAVES", n)
    w = 0
    return w, n

def player_move(n, m, a, b, c):
    print("\nYOUR MOVE? ", end="")
    while True:
        p = input()
        if not p.isdigit():
            print("INVALID INPUT. PLEASE ENTER AN INTEGER.")
            continue
        p = int(p)
        if p == 0:
            print("I TOLD YOU NOT TO USE ZERO! COMPUTER WINS BY FORFEIT.")
            w = 1
            return w, n
        if p < a or (p == n and m == 1) or p > b:
            print("ILLEGAL MOVE, REENTER IT: ", end="")
            continue
        n = n - p
        if n != 0:
            w = 0
            print("YOU TAKE", p, "AND LEAVE", n)
            return w, n
        if m == 1:
            print("TOUGH LUCK, YOU LOSE.")
            w = 1
            return w, n
        print("CONGRATULATIONS, YOU WIN.")
        w = 1
        return w, n


def main():
    title()
    while True:
        n = get_valid_pile_size()
        m = get_valid_win_option()
        a, b = get_valid_min_max()
        s = who_starts()
        play_game(n, m, a, b, s)

main()
