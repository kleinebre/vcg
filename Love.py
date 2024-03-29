#!/usr/bin/env python3

print(" " * 33 + "LOVE")
print(" " * 15 + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY\n\n")

print("A TRIBUTE TO THE GREAT AMERICAN ARTIST, ROBERT INDIANA.")
print("HIS GREATEST WORK WILL BE REPRODUCED WITH A MESSAGE OF")
print("YOUR CHOICE UP TO 60 CHARACTERS.  IF YOU CAN'T THINK OF")
print("A MESSAGE, SIMPLE TYPE THE WORD 'LOVE'\n")
data = [
    60,60,1,12,26,9,12,3,8,24,17,8,4,6,23,21,6,4,6,22,12,5,6,5,
    4,6,21,11,8,6,4,4,6,21,10,10,5,4,4,6,21,9,11,5,4,
    4,6,21,8,11,6,4,4,6,21,7,11,7,4,4,6,21,6,11,8,4,
    4,6,19,1,1,5,11,9,4,4,6,19,1,1,5,10,10,4,4,6,18,2,1,6,8,11,4,
    4,6,17,3,1,7,5,13,4,4,6,15,5,2,23,5,1,29,5,17,8,
    1,29,9,9,12,1,13,5,40,1,1,13,5,40,1,4,6,13,3,10,6,12,5,1,
    5,6,11,3,11,6,14,3,1,5,6,11,3,11,6,15,2,1,
    6,6,9,3,12,6,16,1,1,6,6,9,3,12,6,7,1,10,
    7,6,7,3,13,6,6,2,10,7,6,7,3,13,14,10,8,6,5,3,14,6,6,2,10,
    8,6,5,3,14,6,7,1,10,9,6,3,3,15,6,16,1,1,
    9,6,3,3,15,6,15,2,1,10,6,1,3,16,6,14,3,1,10,10,16,6,12,5,1,
    11,8,13,27,1,11,8,13,27,1,60
]
a = input("YOUR MESSAGE, PLEASE: ")
l = len(a)

for i in range(10):
    print()
space = False

col = 0
line = ""

# Play with the style!
# 1=classic; col dictates char.
# 2=combine row and col to dictate char
# 3=ignore position, just print the message.
style = 1

row = 0
charnum = 0
for x in data[1:]:
    for n in range(x):
        col += 1
        if space:
            line += " "
        else:
            index = {1: len(line), 2: (col + row - 1), 3: charnum}.get(style, len(line))
            line += a[index % l]
            charnum += 1
        if len(line) >= data[0]:
            print(line)
            line = ""
            row += 1
            col = 0
            space = True
    space = not space
