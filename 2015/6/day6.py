"""
You've decided to deploy one million lights in a 1000x1000 grid.

Lights in your grid are numbered from 0 to 999 in each direction;

The lights at each corner are at [0, 0], [0, 999], [999, 999], and [999, 0].

The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs.

Each coordinate pair represents opposite corners of a rectangle, inclusive;
a coordinate pair like [0, 0] through [2, 2] therefore refers to 9 lights in a 3x3 square.

The lights all start turned off.

After following the instructions, how many lights are lit?
"""

# -------------------- INPUT PROCESSING --------------------

print(" PROCESSING INPUT ".center(32, '-'))

inp = []

with open("./input.txt", 'r') as file:
    for line in file.readlines():
        cleaned = []

        if "toggle" in line:
            cleaned.append("toggle")
            coords = line.split("toggle")[1].strip()
            cleaned.append(list(map(lambda cc: list(map(int, cc.strip().split(','))), coords.split("through"))))
        elif "turn off" in line:
            cleaned.append("turn off")
            coords = line.split("turn off")[1].strip()
            cleaned.append(list(map(lambda cc: list(map(int, cc.strip().split(','))), coords.split("through"))))
        elif "turn on" in line:
            cleaned.append("turn on")
            coords = line.split("turn on")[1].strip()
            cleaned.append(list(map(lambda cc: list(map(int, cc.strip().split(','))), coords.split("through"))))

        inp.append(cleaned)

file.close()

# print(inp)

lights = {}

for x in range(0, 999 + 1):
    for y in range(0, 999 + 1):
        lights[x, y] = "OFF"

# -------------------- PART 1 --------------------

print(" PART 1 ".center(32, '-'))

# inp = [["turn on", [[0, 0], [999, 999]]], ["turn off", [[499, 499], [500, 500]]], ["toggle", [[0, 0], [999, 999]]]]

for count, [instruction, coordinates] in enumerate(inp):
    if (count + 1) % 50 == 0:
        print("Currently on instruction", count + 1, '/', len(inp))

    bottomLeft = coordinates[0]
    topRight = coordinates[1]

    for x in range(bottomLeft[0], topRight[0] + 1):
        for y in range(bottomLeft[1], topRight[1] + 1):
            if instruction == "toggle":
                if lights[x, y] == "OFF":
                    lights[x, y] = "ON"
                elif lights[x, y] == "ON":
                    lights[x, y] = "OFF"
            elif instruction == "turn off":
                lights[x, y] = "OFF"
            elif instruction == "turn on":
                lights[x, y] = "ON"

print("There are", list(lights.values()).count("ON"), "lights turned on.")

# -------------------- PART 2 --------------------
"""
The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. 

The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?
"""

print(" PART 2 ".center(32, '-'))

lights = {}

for x in range(0, 999 + 1):
    for y in range(0, 999 + 1):
        lights[x, y] = 0

for count, [instruction, coordinates] in enumerate(inp):
    if (count + 1) % 50 == 0:
        print("Currently on instruction", count + 1, '/', len(inp))

    bottomLeft = coordinates[0]
    topRight = coordinates[1]

    for x in range(bottomLeft[0], topRight[0] + 1):
        for y in range(bottomLeft[1], topRight[1] + 1):
            if instruction == "toggle":
                lights[x, y] += 2
            elif instruction == "turn off":
                if lights[x, y] > 0:
                    lights[x, y] -= 1
            elif instruction == "turn on":
                lights[x, y] += 1

print("The total brightness is", sum(lights.values()))
