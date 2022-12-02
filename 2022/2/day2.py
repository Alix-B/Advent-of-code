"""
One Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win.

"The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score.

Your total score is the sum of your scores for each round.

The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

What would your total score be if everything goes exactly according to your strategy guide?
"""

# -------------------- INPUT PROCESSING --------------------

print(" PROCESSING INPUT ".center(32, '-'))

inp = []

with open("./input.txt", 'r') as file:
    for line in file.readlines():
        inp.append(line.strip().split(' '))

file.close()

print(inp)

# -------------------- PART 1 --------------------

print(" PART 1 ".center(32, '-'))

tot_score = 0

for hand in inp:
    # Opponent rock
    if hand[0] == 'A':
        # You rock
        if hand[1] == 'X':
            tot_score += 1  # For choosing rock
            tot_score += 3  # Draw
        # You Paper
        elif hand[1] == 'Y':
            tot_score += 2  # For choosing paper
            tot_score += 6  # Win
        # You scissors
        elif hand[1] == 'Z':
            tot_score += 3  # For choosing scissors
            tot_score += 0  # Lose
    # Opponent paper
    elif hand[0] == 'B':
        # You rock
        if hand[1] == 'X':
            tot_score += 1  # For choosing rock
            tot_score += 0  # Lose
        # You Paper
        elif hand[1] == 'Y':
            tot_score += 2  # For choosing paper
            tot_score += 3  # Draw
        # You scissors
        elif hand[1] == 'Z':
            tot_score += 3  # For choosing scissors
            tot_score += 6  # Win
    # Opponent scissors
    elif hand[0] == 'C':
        # You rock
        if hand[1] == 'X':
            tot_score += 1  # For choosing rock
            tot_score += 6  # Win
        # You Paper
        elif hand[1] == 'Y':
            tot_score += 2  # For choosing paper
            tot_score += 0  # Lose
        # You scissors
        elif hand[1] == 'Z':
            tot_score += 3  # For choosing scissors
            tot_score += 3  # Draw

print("Your total score is:", tot_score)


# -------------------- PART 2 --------------------

"""
The Elf finishes helping with the tent and sneaks back over to you. 

"Anyway, the second column says how the round needs to end: 
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
"""

print(" PART 2 ".center(32, '-'))

tot_score = 0

for hand in inp:
    # Opponent rock
    if hand[0] == 'A':
        # You need to lose
        if hand[1] == 'X':
            tot_score += 0  # Lose
            tot_score += 3  # For choosing scissors
        # You need to draw
        elif hand[1] == 'Y':
            tot_score += 3  # Draw
            tot_score += 1  # For choosing rock
        # You need to win
        elif hand[1] == 'Z':
            tot_score += 6  # Win
            tot_score += 2  # For choosing paper

    # Opponent paper
    elif hand[0] == 'B':
        # You need to lose
        if hand[1] == 'X':
            tot_score += 0  # Lose
            tot_score += 1  # For choosing rock
        # You need to draw
        elif hand[1] == 'Y':
            tot_score += 3  # Draw
            tot_score += 2  # For choosing paper
        # You need to win
        elif hand[1] == 'Z':
            tot_score += 6  # Win
            tot_score += 3  # For choosing scissors

    # Opponent scissors
    elif hand[0] == 'C':
        # You need to lose
        if hand[1] == 'X':
            tot_score += 0  # Lose
            tot_score += 2  # For choosing paper
        # You need to draw
        elif hand[1] == 'Y':
            tot_score += 3  # Draw
            tot_score += 3  # For choosing scissors
        # You need to win
        elif hand[1] == 'Z':
            tot_score += 6  # Win
            tot_score += 1  # For choosing rock

print("Your total score is:", tot_score)
