#!/usr/bin/env python3
import random

print(" " * 33 + "LETTER")
print(" " * 15 + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
print("\n" * 3)
print("LETTER GUESSING GAME\n")

print("I'LL THINK OF A LETTER OF THE ALPHABET, A TO Z.")
print("TRY TO GUESS MY LETTER AND I'LL GIVE YOU CLUES")
print("AS TO HOW CLOSE YOU'RE GETTING TO MY LETTER.\n")

while True:
    L = random.randint(65, 90)
    G = 0

    print("\nO.K., I HAVE A LETTER.  START GUESSING.\n")

    while True:
        print("\nWHAT IS YOUR GUESS? ", end="")
        G += 1
        A = ord(input().upper())

        if A == L:
            print("\nYOU GOT IT IN", G, "GUESSES!!")
            if G > 5:
                print("BUT IT SHOULDN'T TAKE MORE THAN 5 GUESSES!")
            else:
                print("GOOD JOB !!!!!")
            for N in range(1, 16):
                print(chr(7), end="")
            print("\nLET'S PLAY AGAIN.....\n")
            break

        if A < L:
            print("TOO LOW.  TRY A HIGHER LETTER.")
        else:
            print("TOO HIGH.  TRY A LOWER LETTER.") 
