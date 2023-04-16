#!/usr/bin/env python3
from numpy import exp
from math import sqrt


def zval(z):
    return 30 * exp(-z * z / 100)


print((" " * 32) + "3D PLOT")
print((" " * 20) + "Python version by Marc Brevoort")
print("")
print("")
print("")
print("")

x = -30
while x <= 30:
    l = 0
    y1 = 5 * int(sqrt(900 - x * x) / 5)
    y = y1
    row = ""
    while y >= -y1:
        z = int(25 + zval(sqrt(x * x + y * y)) - 0.7 * y)
        if z > l:
            l = z
            row += " " * (z - len(row)) + "*"
        y -= 5

    print(row)
    row = ""
    x += 1.5
