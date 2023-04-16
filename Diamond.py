#!/usr/bin/env python3
print(" " * 33 + "DIAMOND")
print(" " * 15 + "CREATIVE COMPUTING MORRISTOWN, NEW JERSEY")
print("\n\n")

print("FOR A PRETTY DIAMOND PATTERN,")
d_width = int(input("TYPE IN AN ODD NUMBER BETWEEN 5 AND 21: "))
print()  # prints an empty line.

q = int(60 / d_width)  # page width / diamond width = diamond count
astr = "CC"
set = 0
for half in range(q * 2):
    # delta is positive for top half diamond, negative for bottom
    delta = -((half % 2) * 2 - 1)
    if delta > 0:
        # start at size 1, then grow until we reach full width
        startwidth = 1
        endwidth = d_width
    else:
        # start at size r-2, then shrink until we reach 1
        startwidth = d_width - 2
        endwidth = 1

    n = startwidth
    while (n * delta) <= (endwidth * delta):
        line = " " * int((d_width - n) / 2)
        for m in range(q):
            for a in range(n):
                line += "!" if a >= len(astr) else astr[a]
            line += " " * (int(d_width * (m + 1) + (d_width - n) / 2) - len(line))
        print(line)
        n += delta * 2
