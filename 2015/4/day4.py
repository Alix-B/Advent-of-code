"""
Santa needs help mining AdventCoins to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.

The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal.

To mine AdventCoins, you must find Santa the lowest positive number that produces such a hash.

For example:
    If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes
    (000001dbbfa...), and it is the lowest such number to do so.
"""

import hashlib

# -------------------- INPUT PROCESSING --------------------

print(" PROCESSING INPUT ".center(32, '-'))

inp = "iwrupvqb"

# -------------------- PART 1 --------------------

print(" PART 1 ".center(32, '-'))

count = 1

while True:
    if count % 100000 == 0:
        print("SEARCHED", count, "KEYS.")

    key = bytes(inp + str(count), encoding='UTF-8')

    if hashlib.md5(key).hexdigest()[0:5] == "00000":
        print(count)
        break
    else:
        count += 1

# -------------------- PART 2 --------------------
"""
Now find one that starts with six zeroes.
"""

print(" PART 2 ".center(32, '-'))

count = 1

while True:
    if count % 1000000 == 0:
        print("SEARCHED", count, "KEYS.")

    key = bytes(inp + str(count), encoding='UTF-8')

    if hashlib.md5(key).hexdigest()[0:6] == "000000":
        print(count)
        break
    else:
        count += 1
