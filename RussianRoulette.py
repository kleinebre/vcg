#!/usr/bin/env python3
from random import random

print(" " * 28 + "RUSSIAN ROULETTE")
print(" " * 15 + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY\n\n")

print("THIS IS A GAME OF >>>>>>>>>>RUSSIAN ROULETTE.\n")
print("HERE IS A REVOLVER.")
print("TYPE '1' TO SPIN CHAMBER AND PULL TRIGGER.")
print("TYPE '2' TO GIVE UP.\n")
print("GO")

N = 0
while True:
    try:
        i = int(input())
        if i != 1 and i != 2:
            raise ValueError
    except ValueError:
        print("INVALID INPUT. ENTER 1 or 2.")
        continue
    if i == 2:
        print("     CHICKEN!!!!!")
        break
    else:
        N += 1
        if random() > 0.833333:
            print("     BANG!!!!!   YOU'RE DEAD!")
            print("CONDOLENCES WILL BE SENT TO YOUR RELATIVES.\n\n")
            print("...NEXT VICTIM...")
            N = 0
        elif N > 10:
            print("YOU WIN!!!!!")
            print("LET SOMEONE ELSE BLOW HIS BRAINS OUT.\n")
            break
        else:
            print("- CLICK -\n")
