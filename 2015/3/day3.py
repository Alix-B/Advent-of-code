"""
Santa is delivering presents to an infinite two-dimensional grid of houses.

Moves are always exactly one house to the north (^), south (v), east (>), or west (<).

After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had too much eggnog, so Santa ends up visiting some houses more than once.

How many houses receive at least one present?
"""


# -------------------- INPUT PROCESSING --------------------

print(" PROCESSING INPUT ".center(32, '-'))

inp = []

with open("./input", 'r') as file:
    for char in file.readline():
        inp.append(char)

file.close()

# -------------------- PART 1 --------------------

print(" PART 1 ".center(32, '-'))

houses = [(0, 0)]
x = 0
y = 0

for direction in inp:
    if direction == '>':
        x += 1
        # print("RIGHT")
    elif direction == '<':
        x += -1
        # print("LEFT")
    elif direction == '^':
        y += 1
        # print("UP")
    elif direction == 'v':
        y += -1
        # print("DOWN")
    else:
        print("DIRECTION INVALID:", direction)
        break

    houses.append((x, y))

uniqHouses = set(houses)

print(len(uniqHouses), "houses receive at least one present.")

# -------------------- PART 2 --------------------
"""
The next year, to speed up the process, Santa creates a robot version of himself to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), 
then take turns moving based on instructions from the elf.

This year, how many houses receive at least one present?
"""

print(" PART 2 ".center(32, '-'))

houses = [(0, 0)]

x = 0
y = 0

roboX = 0
roboY = 0

for index in range(len(inp)):
    direction = inp[index]

    if direction == '>':
        if index % 2 == 0:
            x += 1
        else:
            roboX += 1
        # print("RIGHT")
    elif direction == '<':
        if index % 2 == 0:
            x -= 1
        else:
            roboX -= 1
        # print("LEFT")
    elif direction == '^':
        if index % 2 == 0:
            y += 1
        else:
            roboY += 1
        # print("UP")
    elif direction == 'v':
        if index % 2 == 0:
            y -= 1
        else:
            roboY -= 1
        # print("DOWN")
    else:
        print("DIRECTION INVALID:", direction)
        break

    if index % 2 == 0:
        houses.append((x, y))
    else:
        houses.append((roboX, roboY))

uniqHouses = set(houses)

print(len(uniqHouses), "houses receive at least one present.")
