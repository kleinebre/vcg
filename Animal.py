#!/usr/bin/env python3
from random import random as rnd


def title():
    print((32 * " ") + "Animal")
    print((20 * " ") + "Python version by Marc Brevoort")
    print("")
    print("")
    print("")
    print("Play 'Guess the Animal'")
    print("")
    print("Think of an animal and the computer will try to guess it.")
    print("")
    return


def show_animals(data):
    print("")
    print("Animals I already know are:")
    x = 0
    for animal in data:
        if animal[0] == "!":
            animal_name = animal[1:].split("\\")[0]
            print(animal_name + " ", end="")
            x += 1
            if x == 4:
                x = 0
                print("")
    print("")
    return


def ask_question(data, k):
    # SUBROUTINE TO PRINT QUESTIONS
    q = data[k]
    while True:
        answer = input(q.split("\\")[0][1:] + "? ")
        answer = answer.upper()[0]
        if answer != "Y" and answer != "N":
            continue
        break
    t = "\\" + answer
    answer = q.split(t)[1]
    k = int(answer.split("\\")[0])
    return k


data = []
data = ["?Does it swim\\Y1\\N2\\", "!fish", "!bird"]

#           MAIN CONTROL SECTION
while True:
    response = input("Are you thinking of an animal (Yes/List/Quit)? ")
    if response.upper()[0] == "L":
        show_animals(data)
        continue
    if response.upper()[0] == "Q":
        print("OK. Hope you had fun!")
        exit(0)
    if response.upper()[0] == "N":
        print("How about now?")
        continue
    if response.upper()[0] != "Y":
        print("I don't understand.")
        continue

    k = 0
    while True:
        k = ask_question(data, k)
        if data[k][0] == "?":
            continue
        break
    response = input("Is it a " + data[k][1:] + "? ")
    if response.upper()[0] == "Y":
        print("I knew it! Why not try another animal?")
        continue

    new_animal = input("I give up. What animal were you thinking of? ")
    tell_apart = input(
        "With what question can I tell apart a "
        + new_animal
        + " and a "
        + data[k][1:]
        + "?"
    )
    while True:
        answer = input("For a " + new_animal + " the answer would be? ")
        answer = answer.upper()[0]
        if answer != "Y" and answer != "N":
            print("Please type Y or N.")
            continue
        if answer == "Y":
            opposite = "N"
            break

        if answer == "N":
            opposite = "Y"
            break

    z1 = len(data)
    data.append(data[k])
    data.append("!" + new_animal)
    data[k] = (
        "?"
        + tell_apart
        + "\\"
        + answer
        + str(z1 + 1)
        + "\\"
        + opposite
        + str(z1)
        + "\\"
    )
