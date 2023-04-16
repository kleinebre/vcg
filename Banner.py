#!/usr/bin/env python3
from __future__ import print_function


def get_posint(message):
    while True:
        num = 0
        ri = input(message + " ")
        if ri.upper()[0] == "Q":
            exit(0)
        try:
            num = int(ri)
        except TypeError:
            num = 0

        if not (num > 0):
            print("Invalid input, try again.")
            continue
        break
    return num


font = {
    " ": [0, 0, 0, 0, 0, 0, 0],
    "A": [505, 37, 35, 34, 35, 37, 505],
    "G": [125, 131, 258, 258, 290, 163, 101],
    "E": [512, 274, 274, 274, 274, 258, 258],
    "T": [2, 2, 2, 512, 2, 2, 2],
    "W": [256, 257, 129, 65, 129, 257, 256],
    "L": [512, 257, 257, 257, 257, 257, 257],
    "S": [69, 139, 274, 274, 274, 163, 69],
    "O": [125, 131, 258, 258, 258, 131, 125],
    "N": [512, 7, 9, 17, 33, 193, 512],
    "F": [512, 18, 18, 18, 18, 2, 2],
    "K": [512, 17, 17, 41, 69, 131, 258],
    "B": [512, 274, 274, 274, 274, 274, 239],
    "D": [512, 258, 258, 258, 258, 131, 125],
    "H": [512, 17, 17, 17, 17, 17, 512],
    "M": [512, 7, 13, 25, 13, 7, 512],
    "?": [5, 3, 2, 354, 18, 11, 5],
    "U": [128, 129, 257, 257, 257, 129, 128],
    "R": [512, 18, 18, 50, 82, 146, 271],
    "P": [512, 18, 18, 18, 18, 18, 15],
    "Q": [125, 131, 258, 258, 322, 131, 381],
    "Y": [8, 9, 17, 481, 17, 9, 8],
    "V": [64, 65, 129, 257, 129, 65, 64],
    "X": [388, 69, 41, 17, 41, 69, 388],
    "Z": [386, 322, 290, 274, 266, 262, 260],
    "I": [258, 258, 258, 512, 258, 258, 258],
    "C": [125, 131, 258, 258, 258, 131, 69],
    "J": [65, 129, 257, 257, 257, 129, 128],
    "1": [0, 0, 261, 259, 512, 257, 257],
    "2": [261, 387, 322, 290, 274, 267, 261],
    "*": [69, 41, 17, 512, 17, 41, 69],
    "3": [66, 130, 258, 274, 266, 150, 100],
    "4": [33, 49, 41, 37, 35, 512, 33],
    "5": [160, 274, 274, 274, 274, 274, 226],
    "6": [194, 291, 293, 297, 305, 289, 193],
    "7": [258, 130, 66, 34, 18, 10, 8],
    "8": [69, 171, 274, 274, 274, 171, 69],
    "9": [263, 138, 74, 42, 26, 10, 7],
    "=": [41, 41, 41, 41, 41, 41, 41],
    "!": [1, 1, 1, 384, 1, 1, 1],
    "0": [57, 69, 131, 258, 131, 69, 57],
    ".": [1, 1, 129, 449, 129, 1, 1],
}

x = get_posint("Horizontal chars/pixel?")
y = get_posint("Vertical chars/pixel?")

while True:
    c = input("Centered (Y/N)? ")
    if c == "":
        continue
    c = c.upper()[0]
    if c == "Y":
        centered = 1
        break
    if c == "N":
        centered = 0
        break
    continue

while True:
    m = input("Char used to print banner (type 'all' to use the char being printed): ")
    if m.upper() == "ALL":
        m = "ALL"
        break
    if len(m) == 0:
        continue
    m = m[0]
    break

message = input("Message? ")
j = [0 for n in range(0, 16)]
f = [0 for n in range(0, 16)]

for onechar in message:
    chardef = font.get(onechar, ".")
    if m == "ALL":
        printchar = onechar
    else:
        printchar = m

    for u in range(0, len(chardef)):
        su = chardef[u]
        for invk in range(0, 9):
            k = 8 - invk
            j[9 - k] = 0
            if (2**k) < su:
                j[9 - k] = 1
                su -= 2**k
                if su == 1:
                    f[u] = 9 - k
                    break

        for t1 in range(1, x + 1):
            line = ""
            tab = int(((63 - 4.5 * y) * centered) / (len(message) + 1))
            while len(line) < tab:
                line += " "
            for b in range(1, f[u] + 1):
                if j[b] != 0:
                    line += printchar * y
                else:
                    line += " " * y
            print(line)
    for h in range(0, 2 * x):
        print("")

# page feed
for h in range(1, 75):
    print("")
