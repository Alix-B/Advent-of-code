"""
Find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.

The elves also need a little extra paper for each present: the area of the smallest side.

How many total square feet of wrapping paper should they order?
"""

# -------------------- INPUT PROCESSING --------------------

print(" PROCESSING INPUT ".center(32, '-'))

inp = []

# Even though we sort the dimensions by size, we can reassign them to Length, Width, Height order W.O.G.
with open("./input", 'r') as file:
    for line in file.readlines():
        dim = list(map(int, line.strip().split('x')))
        dim.sort()
        inp.append(dim)

file.close()

# -------------------- PART 1 --------------------

print(" PART 1 ".center(32, '-'))

totalWrapping = 0

for box in inp:
    length = box[0]
    width = box[1]
    height = box[2]

    extra = length * width  # Length x width is smallest size due to ordering

    surface = 2 * length * width + 2 * width * height + 2 * height * length

    totalWrapping += surface + extra

print("The total amount of wrapping paper needed is", totalWrapping, "feet.")

# -------------------- PART 2 --------------------
"""
The ribbon required to wrap a present is the smallest perimeter of any one face. 

The feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present.

How many total feet of ribbon should they order?
"""

print(" PART 2 ".center(32, '-'))

totalRibbon = 0

for box in inp:
    length = box[0]
    width = box[1]
    height = box[2]

    wrap = 2 * length + 2 * width

    bow = length * width * height

    totalRibbon += wrap + bow

print("The total amount of ribbon needed is", totalRibbon, "feet.")
