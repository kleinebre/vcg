#!/usr/bin/env python
# Original by David Ahl

import math
print((" " * 30) + "SINE WAVE")
print((" " * 20) + "Python version by Marc Brevoort")
print("")
print("")
print("")
print("")

toggle = 0

t = 0.0
while t <= 40:    
    col = int (26.0 + 25.0 * math.sin(t))
    tab = " " * col
    toggle = 1 - toggle

    if toggle == 1:
        print tab + "CREATIVE"
    else:    
        print tab + "COMPUTING"

    t += .25

