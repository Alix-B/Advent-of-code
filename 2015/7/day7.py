"""
Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535).

A signal is provided to each wire by a gate, another wire, or some specific value.

Each wire can only get a signal from one source, but can provide its signal to multiple destinations.

A gate provides no signal until all of its inputs have a signal.

For example:
    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift).

What signal is ultimately provided to wire a?
"""
# -------------------- INPUT PROCESSING --------------------

print(" PROCESSING INPUT ".center(32, '-'))

inp = []

with open("./input.txt", 'r') as file:
    for line in file.readlines():
        cleaned = line.strip().split(' -> ')

        if "AND" in cleaned[0]:
            cleaned.append("AND")
            cleaned[0] = cleaned[0].split(" AND ")
        elif "OR" in cleaned[0]:
            cleaned.append("OR")
            cleaned[0] = cleaned[0].split(" OR ")
        elif "NOT" in cleaned[0]:
            cleaned.append("NOT")
            cleaned[0] = cleaned[0].split("NOT ")[1]
        elif "RSHIFT" in cleaned[0]:
            cleaned.append("RSHIFT")
            cleaned[0] = cleaned[0].split(" RSHIFT ")
            cleaned[0][1] = int(cleaned[0][1])
        elif "LSHIFT" in cleaned[0]:
            cleaned.append("LSHIFT")
            cleaned[0] = cleaned[0].split(" LSHIFT ")
            cleaned[0][1] = int(cleaned[0][1])
        else:
            cleaned.append("ASSIGN")

        inp.append(cleaned)

file.close()

# -------------------- PART 1 --------------------

print(" PART 1 ".center(32, '-'))

wires = {}

for command in inp:
    values = command[0]
    wire = command[1]
    instruction = command[2]

    print(command)

    if instruction == "ASSIGN":
        if values.isnumeric():
            wires.update({wire: int(values)})
        else:
            wires.update({wire: wires[values]})
    elif instruction == "OR":
        wires.update({wire: wires[values[0]] | wires[values[1]]})
    elif instruction == "AND":
        if values[0].isnumeric():
            wires.update({wire: int(values[0]) & wires[values[1]]})
        else:
            wires.update({wire: wires[values[0]] & wires[values[1]]})
    elif instruction == "RSHIFT":
        wires.update({wire: wires[values[0]] >> values[1]})
    elif instruction == "LSHIFT":
        wires.update({wire: wires[values[0]] << values[1]})
    elif instruction == "NOT":
        # print(command)
        wires.update({wire: ~wires[values] & 0xFFFF})

print(wires['a'])
