#!/usr/bin/env python3
from random import random as rnd


def title():
    print((28 * " ") + "Amazing program")
    print((20 * " ") + "Python version by Marc Brevoort")
    print("")
    print("")
    print("")
    print("")
    return


def get_maze_size():
    while True:
        try:
            hori, vert = input("What are your width and length: ").split(",")
            hori = int(hori)
            vert = int(vert)
        except TypeError:
            hori = 0
            vert = 0

        if hori <= 1 or vert <= 1:
            print("Meaningless dimensions.  Try again.")
            continue

        return hori, vert


def print_maze(maze, width, height, start_col):
    # top row
    for col in range(1, width + 1):
        if col == start_col:
            print(".  ", end="")
        else:
            print(".--", end="")
    print(".")
    # rest of the maze
    for row in range(1, height + 1):
        print("I", end="")
        for col in range(1, width + 1):
            if maze[col][row] < 2:
                print("  I", end="")
            else:
                print("   ", end="")
        print("")
        for col in range(1, width + 1):
            if maze[col][row] in (0, 2):
                print(":--", end="")
            else:
                print(":  ", end="")
        print(".")
    return


def find_used_pos(work, width, height, col, row):
    # scan the working area until we find a filled field
    while True:
        col += 1
        if col > width:
            row += 1
            col = 1
            if row > height:
                row = 1

        if work[col][row] != 0:
            break
    return col, row


def available_directions(work, height, width, col, row, have_exit):
    directions = []
    if not (col == 1 or work[col - 1][row]):
        directions.append("LEFT")

    if not (col == width or work[col + 1][row]):
        directions.append("RIGHT")

    if not (row == 1 or work[col][row - 1]):
        directions.append("UP")

    if row == height:
        if not have_exit:
            directions.append("DOWN")
    else:
        if not work[col][row + 1]:
            directions.append("DOWN")

    return directions


title()
width, height = get_maze_size()

work = [x[:] for x in [[0] * (height + 1)] * (width + 1)]
maze = [x[:] for x in [[0] * (height + 1)] * (width + 1)]

# meaning of the numbers for maze array:
# 0: Has right wall, has bottom wall
# 1: has right wall, no bottom wall
# 2: no right wall, has bottom wall
# 3: no right wall, no bottom wall

have_exit = False
want_exit = True
start_col = int(rnd() * width) + 1
end_col = 1

col = start_col
row = 1
filled = 1
work[col][row] = filled

while True:
    directions = available_directions(work, height, width, col, row, have_exit)
    if not directions:
        # Nowhere to go. Find a used pos on the board to proceed from
        col, row = find_used_pos(work, width, height, col, row)
        continue
    # randomly select one of the available directions
    direction = directions[int(rnd() * len(directions))]
    if direction == "LEFT":
        work[col - 1][row] = filled
        maze[col - 1][row] = 2  # remove right wall from left field
        col -= 1

        filled += 1
        if filled == width * height:
            break
        continue

    if direction == "RIGHT":
        work[col + 1][row] = filled
        if maze[col][row] == 0:
            # we have both walls
            maze[col][row] = 2  # remove right wall
        else:
            # we have no bottom wall
            maze[col][row] = 3  # remove bwalls
        col += 1

        filled += 1
        if filled == width * height:
            break
        continue

    if direction == "UP":
        work[col][row - 1] = filled
        maze[col][row - 1] = 1
        row -= 1

        filled += 1
        if filled == width * height:
            break
        continue

    if direction == "DOWN":
        if row == height:
            if int(rnd() * 3) == 1:
                end_col = col
                have_exit = 1
            continue
        work[col][row + 1] = filled

        if maze[col][row] == 0:
            # we have both walls
            maze[col][row] = 1  # remove bottom wall
        else:
            # we have no right wall
            maze[col][row] = 3  # remove both walls
        row += 1

        filled += 1
        if filled == width * height:
            break
        continue

# Remove bottom wall
maze[end_col][height] |= 1

print_maze(maze, width, height, start_col)
