#!/usr/bin/env python3
print(" "*33 + "TRAIN")
print(" "*15 + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
print("\n\n")

print("TIME - SPEED DISTANCE EXERCISE\n")

import random

while True:
    C = int(25 * random.random()) + 40
    D = int(15 * random.random()) + 5
    T = int(19 * random.random()) + 20

    print(f" A CAR TRAVELING {C} MPH CAN MAKE A CERTAIN TRIP IN")
    print(f" {D} HOURS LESS THAN A TRAIN TRAVELING AT {T} MPH.")

    A = float(input("HOW LONG DOES THE TRIP TAKE BY CAR? "))

    V = D * T / (C - T)
    E = int(abs((V - A) * 100 / A) + 0.5)

    if E <= 5:
        print(f"GOOD! ANSWER WITHIN {E} PERCENT.")
    else:
        print(f"SORRY. YOU WERE OFF BY {E} PERCENT.")
        print(f"CORRECT ANSWER IS {V} HOURS.\n")

    another_problem = input("ANOTHER PROBLEM (YES OR NO)? ")

    if another_problem.upper() != "YES":
        break
    print("\n")

print("\n")
