from random import random as rnd

# A bit stupid game - ultimately you pretty much always win
# by selecting the same number over and over again.
def title():
    print((33 * " ") + "Number")
    print((15 * " ") + "Creative Computing  Morristown, New Jersey")
    print((15 * " ") + "Python version by Marc Brevoort")
    print("")
    print("")
    print("")
    print("You have 100 points.  By guessing numbers from 1 to 5, you")
    print("can gain or lose points depending upon how close you get to")
    print("a random number selected by the computer.")
    print("")
    print("You occasionally will get a jackpot which will double(!)")
    print("your point count.  You win when you get 500 points.")
    print("")


def fnr():
    return int(5 * rnd() + 1)


def main():
    title()
    p = 100.0
    while True:
        g = input("Guess a number from 1 to 5: ")
        r = fnr()
        s = fnr()
        t = fnr()
        u = fnr()
        v = fnr()
        if g == r:
            p -= 5
        elif g == s:
            p += 5
        elif g == t:
            p *= 2
            print("You hit the jackpot!")
        elif g == u:
            p += 1
        elif g == v:
            p -= p / 2
        elif g > 5:
            continue
        else:
            p -= 5

        if p <= 500:
            print("You have {} points.".format(p))
            continue
        print("!!!!YOU WIN!!!! With {} points.".format(p))
        break


main()
