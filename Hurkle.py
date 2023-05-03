#!/usr/bin/env python3
import random

def title(tries, gridsize):
    print(" " * 33, "HURKLE")
    print(" " * 15, "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
    print("\n\n")
    print()
    print("A HURKLE IS HIDING ON A", gridsize, "BY", gridsize, "GRID. HOMEBASE")
    print("ON THE GRID IS POINT 0,0 IN THE SOUTHWEST CORNER,")
    print("AND ANY POINT ON THE GRID IS DESIGNATED BY A")
    print("PAIR OF WHOLE NUMBERS SEPERATED BY A COMMA. THE FIRST")
    print("NUMBER IS THE HORIZONTAL POSITION AND THE SECOND NUMBER")
    print("IS THE VERTICAL POSITION. YOU MUST TRY TO")
    print("GUESS THE HURKLE'S GRIDPOINT. YOU GET", tries, "TRIES.")
    print("AFTER EACH TRY, I WILL TELL YOU THE APPROXIMATE")
    print("DIRECTION TO GO TO LOOK FOR THE HURKLE.")
    print()

def main():
    n = 5
    g = 10
    title(n, g)
    while True:
        a = random.randint(0, g-1)
        b = random.randint(0, g-1)
        for k in range(1, n+1):
            print("GUESS #", k)
            x, y = map(int, input().split(","))
            if abs(x-a) + abs(y-b) == 0:
                print("\nYOU FOUND HIM IN", k, "GUESSES!\n")
                break
            # PRINT INFO
            direction = "GO "
            if y != b:
                direction += "NORTH" if y < b else "SOUTH"
            if x != a:
                direction += "WEST" if x > a else "EAST"
            print(direction)
        else:
            print("\nSORRY, THAT'S", n, "GUESSES.")
            print("THE HURKLE IS AT", a, ",", b, "\n")
        print("LET'S PLAY AGAIN, HURKLE IS HIDING.\n")

main()
