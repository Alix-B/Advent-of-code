"""
One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc.
that they've brought with them, one item per line.

Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask:
they'd like to know how many Calories are being carried by the Elf carrying the most Calories.
"""

# -------------------- INPUT PROCESSING --------------------

print(" PROCESSING INPUT ".center(32, '-'))

inp = []

with open("./input.txt", 'r') as file:
    itm = []
    for line in file.readlines():
        if line.strip() == '':
            inp.append(sum(itm))
            itm = []
        else:
            itm.append(int(line.strip()))

    inp.append(sum(itm))

file.close()

inp.sort()

print(inp)

# -------------------- PART 1 --------------------

print(" PART 1 ".center(32, '-'))

print("The maximum total Calories that an Elf carrying is:", inp[-1])


# -------------------- PART 2 --------------------

print(" PART 2 ".center(32, '-'))

"""
By the time you calculate the answer to the Elves' question, 
they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three 
Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.
"""


print("The total Calories that the top 3 elves are carrying is:", sum([inp[-3], inp[-2], inp[-1]]))
