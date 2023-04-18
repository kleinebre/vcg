#!/usr/bin/env python3
from random import random as rnd

# Original apparently by Danny Freidus


def title():
    print((33 * " ") + "Number")
    print((15 * " ") + "Creative Computing  Morristown, New Jersey")
    print((15 * " ") + "Python version by Marc Brevoort")
    print("")
    print("")
    print("")
    print("This program simulates the rolling of a pair of dice.")
    print("You enter the number of times you want the computer to")
    print("'roll' the dice.  Watch out, very large numbers take")
    print("a long time.  In particular, numbers over 5000.")
    print("(Haha, modern hardware go brrrrr... how about 10 million)")


def main():
    while True:
        total_spots = [0 for x in range(12)]
        print("")
        x = input("How many rolls? ")
        for s in range(int(x)):
            a = int(rnd() * 6 + 1)
            b = int(rnd() * 6 + 1)
            r = a + b
            total_spots[r - 1] += 1
        print("")
        print("Total spots | Number of times")
        for v in range(1, 12):
            print("{}      | {}".format(v + 1, total_spots[v]))
        print("")
        print("")
        z = input("Try again? ")
        if z == "y":
            continue
        break


title()
main()
