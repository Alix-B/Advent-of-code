"""
He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis means he should go up one floor, and a closing parenthesis means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

To what floor do the instructions take Santa?
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

floor = 0

for bracket in inp:
    if bracket == '(':
        floor += 1
    elif bracket == ')':
        floor -= 1
    else:
        print("INVALID CHARACTER ENCOUNTERED:", bracket)

print("The final floor is:", floor)

# -------------------- PART 2 --------------------

"""
Find the position of the first character that causes him to enter the basement (floor -1). 

The first character in the instructions has position 1, the second character has position 2, and so on.
"""

print(" PART 2 ".center(32, '-'))

floor = 0

for index in range(len(inp)):

    if inp[index] == '(':
        floor += 1
    elif inp[index] == ')':
        floor -= 1
    else:
        print("INVALID CHARACTER ENCOUNTERED:", inp[index])

    if floor == -1:
        print("BASEMENT ENCOUNTERED", index + 1)  # Plus one to account for positioning starting at 1
        break
