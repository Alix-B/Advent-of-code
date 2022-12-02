# -------------------- INPUT PROCESSING --------------------

print(" PROCESSING INPUT ".center(32, '-'))

inp = []

with open("./test.txt", 'r') as file:
    for line in file.readlines():
        inp.append(line.strip())

file.close()

print(inp)

# -------------------- PART 1 --------------------

print(" PART 1 ".center(32, '-'))
