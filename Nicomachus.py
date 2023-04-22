#!/usr/bin/env python3
import time

print(" " * 33 + "NICOMA")
print(" " * 15 + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
print("\n\n\n")

print("BOOMERANG PUZZLE FROM ARITHMETICA OF NICOMACHUS -- A.D. 90!\n")

while True:
    print()
    print("PLEASE THINK OF A NUMBER BETWEEN 1 AND 100.")
    try:
        print("YOUR NUMBER DIVIDED BY 3 HAS A REMAINDER OF", end=" ")
        a = int(input())
    except ValueError:
        print("Invalid input. Please enter an integer.\n")

    try:
        print("YOUR NUMBER DIVIDED BY 5 HAS A REMAINDER OF", end=" ")
        b = int(input())
    except ValueError:
        print("Invalid input. Please enter an integer.\n")

    try:
        print("YOUR NUMBER DIVIDED BY 7 HAS A REMAINDER OF", end=" ")
        c = int(input())
    except ValueError:
        print("Invalid input. Please enter an integer.\n")

    print()

    print(" " * 26 + "LET ME THINK A MOMENT...")
    print()

    time.sleep(1.5)

    d = (70 * a + 21 * b + 15 * c) % 105

    print("YOUR NUMBER WAS", d, "RIGHT\n")

    while True:
        print(" " * 22 + "IS THAT CORRECT (YES OR NO)? ", end="")
        yn = input().upper()
        print()
        if yn == "YES":
            print(" " * 24 + "HOW ABOUT THAT!!")
            print()
            break
        elif yn == "NO":
            print(" " * 24 + "I FEEL YOUR ARITHMETIC IS IN ERROR.")
            print()
            break
        else:
            print(" " * 16 + "EH? I DON'T UNDERSTAND '", yn, "' TRY 'YES' OR 'NO'.\n")

    print(" " * 28 + "LET'S TRY ANOTHER.")
    print()
    continue
