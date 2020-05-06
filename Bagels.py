#!/usr/bin/env python
from random import random as rnd

DIGITS = 3


def title():
    print((34 * " ") + "Bagels")
    print((22 * " ") + "Python version by Marc Brevoort")
    print("")
    print("")
    """
    *** BAGLES NUMBER GUESSING GAME
    *** ORIGINAL SOURCE UNKNOWN BUT SUSPECTED TO BE
    *** LAWRENCE HALL OF SCIENCE, U.C. BERKELY    
    """


def rules():
    print("")
    print("")
    print("")
    want = input("Would you like the rules (Yes or No)")
    if want.upper()[0] == "N":
        return
    print("")
    print("I am thinking of a three-digit number.  Try to guess")
    print("my number and I will give you clues as follows:")
    print("   Pico   - One digit correct but in the wrong position")
    print("   Fermi  - One digit correct and in the right position")
    print("   Bagels - No digits correct")
    return


def generate_number(numlen):
    a = ""
    for i in range(numlen):
        while True:
            b = str(int(10 * rnd()))
            if b in a:
                continue
            a += b
            break
    return a


title()
rules()
score = 0
while True:
    a = generate_number(DIGITS)
    print("")
    print("O.K.  I have a number in mind.")
    guessnum = 0

    while True:
        guessnum += 1
        if guessnum > 20:
            print("Oh well.")
            print("That's twenty guesses.  My number was %s" % a)
            break

        strg = "Guess #%s" % str(guessnum)
        while True:
            guess = input(strg.ljust(16) + "? ")
            if len(guess) != DIGITS:
                print("Try guessing a three-digit number!")
                continue

            try:
                intguess = int(guess)
            except TypeError:
                intguess = -1

            if intguess < 1:
                print("What?")
                continue

            digits_used = {digit for digit in guess}
            if len(digits_used) != DIGITS:
                print("Oh, I forgot to tell you that the number I have in mind")
                print("has no two digits the same.")
                continue
            break

        pico = 0
        fermi = 0
        for j in range(DIGITS):
            if guess[j] == a[j]:
                fermi += 1
                continue

            if guess[j] in a:
                pico += 1

        if fermi == DIGITS:
            score += 1
            print("You got it!!!")
            print("")
            break

        for j in range(0, pico):
            print("Pico ", end="")
        for j in range(0, fermi):
            print("Pico ", end="")
        if (pico + fermi) == 0:
            print("Bagels")
        print("")
        continue

    again = input("Play again (Yes or No)? ")
    if again.upper()[0] == "Y":
        continue

    print("")
    if score > 0:
        print("A %s point bagels buff!!" % score)

    print("Hope you had fun. Bye!")
    break

exit(0)
