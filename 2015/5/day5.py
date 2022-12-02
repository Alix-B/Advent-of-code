"""
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:
    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
"""

import string

# -------------------- INPUT PROCESSING --------------------

print(" PROCESSING INPUT ".center(32, '-'))

inp = []

with open("./input", 'r') as file:
    for line in file.readlines():
        inp.append(line.strip())

file.close()

# -------------------- PART 1 --------------------

print(" PART 1 ".center(32, '-'))

vowels = ['a', 'e', 'i', 'o', 'u']

naughtySubStrs = ['ab', 'cd', 'pq', 'xy']

doubles = []

for char in string.ascii_lowercase:
    doubles.append(char * 2)

naughty = []

nice = []

# inp = ["dvszwmarrgswjxmb"]

for strings in inp:
    vowelCount = 0
    naughtySub = False

    for substr in naughtySubStrs:
        if substr in strings:
            naughtySub = True
            break

    if not naughtySub:
        for vowel in vowels:
            vowelCount += strings.count(vowel)

        if vowelCount >= 3:
            for double in doubles:
                if double in strings:
                    # print(strings, "IS NICE")
                    nice.append(strings)
                    break

naughty = set(inp).difference(nice)

print("Out of", len(inp), "strings, there are", len(nice), "nice strings and", len(naughty), "naughty strings.")


# -------------------- PART 2 --------------------
"""
Now, a nice string is one with all of the following properties:
    It contains a pair of any two letters that appears at least twice in the string without overlapping, 
    like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), 
    or even aaa. (Let's call them 'patterns')
"""

print(" PART 2 ".center(32, '-'))

pairs = []

patterns = []

nice = []

# inp = ["uurcxstgmygtbstg"]

for char1 in string.ascii_lowercase:
    for char2 in string.ascii_lowercase:
        pairs.append(char1 + char2)

for char1 in string.ascii_lowercase:
    for char2 in string.ascii_lowercase:
        patterns.append(char1 + char2 + char1)

for strings in inp:
    for pair in pairs:
        if strings.count(pair) >= 2:
            for pattern in patterns:
                if pattern in strings and strings not in nice:
                    # print(strings, "IS NICE")
                    nice.append(strings)
                    break

naughty = set(inp).difference(nice)

print("Out of", len(inp), "strings, there are", len(nice), "nice strings and", len(naughty), "naughty strings.")
