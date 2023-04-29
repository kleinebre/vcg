#!/usr/bin/env python3
import random
EMPTY=0
DESTROYER=1
CRUISER=2
CARRIER=3
SUNK=4
# THE GAME STARTS WITH 6 SHIPS
# Also, we have 6 ships in total, 2 of each type.
# ship 1 and 2 are destroyers (2 long),
# 3 and 4 are cruisers (3 long)
# 5 and 6 are carriers (4 long)
# ships may be placed on the board horizontally, vertically or diagonally.

def title():
    """
    BATTLE WRITTEN BY RAY WESTERGARD  10/70
    COPYRIGHT 1971 BY THE REGENTS OF THE UNIV. OF CALIF.
    PRODUCED AT THE LAWRENCE HALL OF SCIENCE, BERKELEY
    """
    print(" "*33 + "BATTLE")
    print(" "*15 + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")

def get_input():
    while True:
        try:
            x, y = map(int, input("Enter x and y separated by a comma: ").split(","))
            if x < 1 or x > 6 or int(x) != abs(x):
                print("INVALID INPUT. TRY AGAIN.")
            elif y < 1 or y > 6 or int(y) != abs(y):
                print("INVALID INPUT. TRY AGAIN.")
            else:
                return x, y
        except ValueError:
            print("INVALID INPUT. TRY AGAIN.")

def ship_sunk(row, col, fleet, LOSSES, SPLASH, HIT):
    game_over = False
    SHIPNUM = fleet[row][col]
    SHIPTYPE = (SHIPNUM - 1) // 2 + 1
    LOSSES[SHIPTYPE] += 1
    print("AND YOU SUNK IT.  HURRAH FOR THE GOOD GUYS.")
    print("SO FAR, THE BAD GUYS HAVE LOST", LOSSES[1], "DESTROYER(S),", LOSSES[2], "CRUISER(S), AND", LOSSES[3], "AIRCRAFT CARRIER(S).")
    print("YOUR CURRENT SPLASH/HIT RATIO IS", SPLASH/HIT)
    if (LOSSES[1] + LOSSES[2] + LOSSES[3]) < 6:
        return game_over
    game_over = True
    print()
    print("YOU HAVE TOTALLY WIPED OUT THE BAD GUYS' FLEET")
    print("WITH A FINAL SPLASH/HIT RATIO OF", SPLASH/HIT)
    if SPLASH == 0:
        print("CONGRATULATIONS -- A DIRECT HIT EVERY TIME.")
    print()
    print("****************************")
    print()
    return game_over


def post_board_init(fleet):
    print("THE FOLLOWING CODE OF THE BAD GUYS' FLEET DISPOSITION")
    print("HAS BEEN CAPTURED BUT NOT DECODED:")
    print()
    for i in range(6):
        for j in range(6):
            print(fleet[j+1][i+1], end=' ')
        print()
    print()
    print("DE-CODE IT AND USE IT IF YOU CAN")
    print("BUT KEEP THE DE-CODING METHOD A SECRET.")
    print()
    return

def play_game(fleet, HISTORY, LOSSES, DAMAGE, SPLASH, HIT):
    print("START GAME")
    game_over = False
    while not game_over:
        x, y = get_input()
        row = 7 - y
        col = x
        if fleet[row][col] == EMPTY:
            SPLASH += 1
            print("SPLASH! TRY AGAIN.")
            continue
        if DAMAGE[fleet[row][col]] >= 4:
            print("THERE USED TO BE A SHIP AT THAT POINT, BUT YOU SUNK IT.")
            print("SPLASH! TRY AGAIN.")
            SPLASH += 1
            continue
        if HISTORY[row][col] > 0:
            print("YOU ALREADY PUT A HOLE IN SHIP NUMBER", fleet[row][col], "AT THAT POINT.")
            print("SPLASH! TRY AGAIN.")
            SPLASH += 1
            continue
        HIT += 1
        HISTORY[row][col] = fleet[row][col]
        print("A DIRECT HIT ON SHIP NUMBER", fleet[row][col])
        DAMAGE[fleet[row][col]] += 1
        if DAMAGE[fleet[row][col]] < 4:
            print("TRY AGAIN.")
            continue
        game_over=ship_sunk(row, col, fleet, LOSSES, SPLASH, HIT)
        if game_over:
            break
    # game over
    return  # SPLASH, HIT, LOSSES, DAMAGE, HISTORY

def main():
    title()
    while True:
        fleet = board_setup()
        damage = [0, 2, 2, 1, 1, 0, 0]  # Initialized with 0 for 4-size ships, 1 for 3-size ships, 2 for 2-size ships
        losses = [0]*4
        history = [[0 for i in range(7)] for j in range(7)]
        splash = 0
        hit = 0
        post_board_init(fleet)
        play_game(fleet, history, losses, damage, splash, hit)

def position_ship(try_x, try_y, fleet, n, i, j):
    fleet[try_x][try_y] = 9 - (2 * i) - j
    for k in range(1, n+1):
        fleet[try_x[k+1]][try_x[k+1]] = fleet[try_x][try_y]
    return fleet

def check_fit_4(fleet, temp_x, temp_y):
    if temp_x[1]<temp_x[2] and temp_x[1]<temp_x[3]:
        Z1=temp_x[1]
    if temp_x[2]<temp_x[1] and temp_x[2]<temp_x[3]:
        Z1=temp_x[2]
    if temp_x[3]<temp_x[1] and temp_x[3]<temp_x[2]:
        Z1=temp_x[3]
    if temp_y[1]>temp_y[2] and temp_y[1]>temp_y[3]:
        Z2=temp_y[1]
    if temp_y[2]>temp_y[1] and temp_y[2]>temp_y[3]:
        Z2=temp_y[2]
    if temp_y[3]>temp_y[1] and temp_y[3]>temp_y[2]:
        Z2=temp_y[3]

    if Z1==1 or Z2==6:
        result=false
        return result, temp_x, temp_y

    if fleet[Z1-1,Z2+1]>0:
        result=false
        return result, temp_x, temp_y

    if fleet[Z1,Z2+1]>0 and fleet[Z1,Z2+1]==fleet[Z1-1,Z2]:
        result=false
        return result, temp_x, temp_y

    result=true
    temp_x[k+1]=Z1-1
    temp_y[k+1]=Z2+1
    return result, temp_x, temp_y


def try_direction_1(try_x, try_y, n, i, j, fleet):
    m = 1
    temp_y = [0, try_y, 7, 7]
    for k in range(1, n + 1):
        if m > 1:
            break
        if temp_y[k] == 6:
            m = 2
            break
        if fleet[try_x][temp_y[k]+1] > 0:
            m = 2
            break
        temp_y.append(temp_y[k]+1)
        if temp_y[k+1] == 1:
            m = 2
            break
    if m == 2:
        if temp_y[1] < temp_y[2] and temp_y[1] < temp_y[3]:
            z = temp_y[1]
        elif temp_y[2] < temp_y[1] and temp_y[2] < temp_y[3]:
            z = temp_y[2]
        elif temp_y[3] < temp_y[1] and temp_y[3] < temp_y[2]:
            z = temp_y[3]
        else:
            z = 0
        if z == 1 or fleet[try_x][Z-1] > 0:
            result = False
            return result, fleet
        temp_y[k + 1] = z - 1
    fleet[try_x][try_y] = 9-2*i-j
    for k in range(N):
        fleet[try_x][temp_y[k+1]] = fleet[try_x][try_y]
    result = True
    return result, fleet


def try_direction_2(try_x, try_y, n, i, j, fleet):
    m = 1
    temp_x = [0, try_x, 0, 0, 0]
    temp_y = [0, try_y, 0, 0, 0]

    # CLEAR COORDS
    for k in range(1, n + 1):
        if m > 1:
            return False, fleet
        if temp_x[k] == 1 or temp_y[k] == 1:
            return False, fleet
        if fleet[temp_x[k]-1][temp_y[k]-1] > 0:
            return False, fleet
        if (fleet[temp_x[k]-1][temp_y[k]] > 0 and
            fleet[temp_x[k]-1][temp_y[k]] == fleet[temp_x[k]][temp_y[k]-1]):
            return False, fleet
        temp_x[k+1] = temp_x[k]-1
        temp_y[k+1] = temp_y[k]-1
        if k == n:
            break

    if temp_x[1] > temp_x[2] and temp_x[1] > temp_x[3]:
        z1 = temp_x[1]
    elif temp_x[2] > temp_x[1] and temp_x[2] > temp_x[3]:
        z1 = temp_x[2]
    elif temp_x[3] > temp_x[1] and temp_x[3] > temp_x[2]:
        z1 = temp_x[3]

    if temp_y[1] > temp_y[2] and temp_y[1] > temp_y[3]:
        z2 = temp_y[1]
    elif temp_y[2] > temp_y[1] and temp_y[2] > temp_y[3]:
        z2 = temp_y[2]
    elif temp_y[3] > temp_y[1] and temp_y[3] > temp_y[2]:
        z2 = temp_y[3]

    if z1 == 6 or z2 == 6:
        return False, fleet
    if fleet[z1 + 1][z2 + 1] > 0:
        return False, fleet
    if fleet[z1][z2+1] > 0 and fleet[z1][z2+1] == fleet[z1+1][z2]:
        return False, fleet

    temp_x[k+1] = z1+1
    temp_y[k+1] = z2+1

    fleet = position_ship(try_x, try_y, fleet, n, i, j)
    return True, fleet

def try_direction_3(try_x, try_y, n, i, j, fleet):
    temp_x = [0, try_x, 7, 7]

def try_direction_3(try_x, try_y, n, i, j, fleet):
    temp_x = [0, try_x, 7, 7]
    m = 1

    for k in range(1, n+1):
        if m > 1:
            break
        if temp_x[k] == 6:
            break
        if fleet[temp_x[k]+1][try_y] > 0:
            break
        print(f"k={k}")
        temp_x[k+1] = temp_x[k] + 1
        continue
    else:
        m = 2

    if temp_x[1] < temp_x[2] and temp_x[1] < temp_x[3]:
        z = temp_x[1]
    elif temp_x[2] < temp_x[1] and temp_x[2] < temp_x[3]:
        z = temp_x[2]
    elif temp_x[3] < temp_x[1] and temp_x[3] < temp_x[2]:
        z = temp_x[3]

    if z == 1 or fleet[z-1][try_y] > 0:
        result = False
        return result, fleet
    temp_x[k+1] = z - 1
    fleet[try_x][try_y] = 9 - 2 * i - j
    for k in range(1, n+1):
        fleet[temp_x[k+1]][try_y] = fleet[try_x][try_y]

    result = True
    return result, fleet

def try_direction_4(try_x, try_y, n, i, j, fleet):
    m=0
    temp_x = [0, try_x, 7, 7]
    temp_y = [0, try_y, 0, 0]
    for k in range(1, n+1):
        if m>1:
            result = check_fit(...)
            if not result:
                return result, fleet
            continue
        if temp_x[k]==6 or temp_y[k]==1:
            m=2
            result, temp_x, temp_y = check_fit_4(fleet, temp_x, temp_y)
            if not result:
                return result, fleet
            continue
        if fleet[temp_x[k] + 1, temp_y[k] - 1] > 0:
            m=2
            result, temp_x, temp_y = check_fit_4(fleet, temp_x, temp_y)
            if not result:
                return result, fleet
            continue
        if (
            fleet[temp_x[k]+1,temp_y[k]]>0
            and fleet[temp_x[k]+1][temp_y[k]] == fleet[temp_x[k]][temp_y[k]-1]
        ):
            m=2
            result, temp_x, temp_y = check_fit_4(fleet, temp_x, temp_y)
            if not result:
                return result, fleet
            continue
        temp_x[k+1]=temp_x[k]+1
        temp_y[k+1]=temp_y[k]-1
        continue
    result = true
    return result, fleet

def board_setup():
    temp_x = [0 for i in range(5)]
    temp_y = [0 for i in range(5)]
    fleet = [[0 for i in range(7)] for j in range(7)]
    dir_delta_x = [1, 1, 0, -1]
    dir_delta_y = [0, 1, 1, 1]
    for st in range(3):
        shiptype=(2-st)
        shipsize = shiptype+2
        for j in range(2):
            shipnum = 1+shiptype*2+j
            while True:
                try_x = random.randint(1, 6)
                try_y = random.randint(1, 6)
                direction = random.randint(0, 3)
                valid = True
                for n in range(shipsize):
                    # check if ship falls within board range
                    if (
                        (try_x + n * dir_delta_x[direction] > 6)
                        or (try_y + n * dir_delta_y[direction] > 6)
                        or (try_x + n * dir_delta_x[direction] < 1)
                        or (try_y + n * dir_delta_y[direction] < 1)
                    ):
                        valid = False
                        break
                    # check if ship falls within board range
                    if (
                        fleet[
                            try_x + n * dir_delta_x[direction]
                        ][
                            try_y + n * dir_delta_y[direction]
                        ]
                    != EMPTY):
                        valid = False
                        break
                if not valid:
                    continue
                break
            # valid, place ship
            for n in  range(shipsize):
                fleet[
                    try_x + n * dir_delta_x[direction]
                ][
                    try_y + n * dir_delta_y[direction]
                ] = shipnum
    return fleet
main()
