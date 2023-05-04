#!/usr/bin/env python3
# PRODUCED BY FRED MIRABELLE AND BOB HARPER ON JAN 29, 1973
# IT SIMULATES THE SLOT MACHINE.
import random

def beep(n):
    for _ in range(n):
        print(chr(7), end="")


def title():
    print(" " * 30 + "SLOTS")
    print(" " * 15 + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY\n\n")

    print("YOU ARE IN THE H&M CASINO, IN FRONT OF ONE OF OUR")
    print("ONE-ARM BANDITS. BET FROM $1 TO $100.")
    print("TO PULL THE ARM, PUNCH THE RETURN KEY AFTER MAKING YOUR BET.")


def main():
    title()
    p = 0
    wheel = ["BAR", "BELL", "ORANGE", "LEMON", "PLUM", "CHERRY"]
    while True:
        m = int(input("YOUR BET: "))
        if m > 100:
            print("HOUSE LIMITS ARE $100")
            continue
        if m < 1:
            print("MINIMUM BET IS $1")
            continue
        beep(10)
        x = int(6 * random.random())
        y = int(6 * random.random())
        z = int(6 * random.random())
        print("{} ".format(wheel[x]), end="")
        beep(5)
        print("{} ".format(wheel[y]), end="")
        beep(5)
        print("{} ".format(wheel[z]), end="")
        beep(5)
        print()
        if x == y == z:
            if z == 0:
                print("**TOP DOLLAR**\nYOU WON!")
                p = (10 * m) + m + p
            else:
                print("***JACKPOT***\nYOU WON!")
                p = (100 * m) + m + p
        elif (x == y) or (x == z) or (y == z):
            if z == 0 or y == 0:
                print("*DOUBLE BAR*\nYOU WON!")
                p = (5 * m) + m + p
        else:
            print("YOU LOST.")
            p = p - m
        print("YOUR STANDINGS ARE ${}".format(p))
        play_again = input("\nAGAIN? (Y/N) ").upper()
        if play_again == "Y":
            continue
        if p < 0:
            print("PAY UP! PLEASE LEAVE YOUR MONEY ON THE TERMINAL.")
            break
        if p == 0:
            print("HEY, YOU BROKE EVEN.")
            break
        print("COLLECT YOUR WINNINGS FROM THE H&M CASHIER.")
        break

main()
