#!/usr/bin/env python3
from random import random

def print_title():
    print(" " * 33 + "KINEMA")
    print(" " * 15 + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
    print("\n\n\n")

def check_answer(correct_answer, prompt):
    a = float(input(prompt))
    if abs((a - correct_answer) / correct_answer) < 0.15:
        print("CLOSE ENOUGH.")
        result = 1
    else:
        print("NOT EVEN CLOSE....")
        result = 0
    print(f"CORRECT ANSWER IS {correct_answer}\n")
    return result

def main():
    print_title()
    q = 0
    while q < 3:
        correct = 0
        print()
        print()
        v = 5.0 + int(35.0 * random())
        print(f"A BALL IS THROWN UPWARDS AT {v} METERS PER SECOND.")
        print()

        a = 0.05 * v**2.0  # v0 squared, divided by 2G
        correct += check_answer(a, "HOW HIGH WILL IT GO (IN METERS)? ")

        a = v / 5.0  # 2 times v0 divided by G
        correct += check_answer(a, "HOW LONG UNTIL IT RETURNS (IN SECONDS)? ")

        t = 1.0 + int(2.0 * v * random()) / 10.0
        a = v - 10.0 * t   # v minus GT. Note that the value t here
                           # may be greater than amount of seconds until
                           # the ball returns.
                           # This means it may reach negative heights -
                           # I deduce we are standing on top of a cliff.
        correct += check_answer(a, f"WHAT WILL ITS VELOCITY BE AFTER {t} SECONDS? ")
        print()
        print(correct, "RIGHT OUT OF 3.")
        q += 1
    print("  NOT BAD.")


main()
