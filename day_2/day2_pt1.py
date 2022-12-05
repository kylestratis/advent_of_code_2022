TEST_INPUT = """
A Y
B X
C Z
"""

MODIFIER = {
    "X": 1,
    "Y": 2,
    "Z": 3,
        }

STRATEGY = {
        "X": {
            "A": 3,
            "B": 0,
            "C": 6
            },
        "Y": {
            "A": 6,
            "B": 3,
            "C": 0
            },
        "Z": {
            "A": 0,
            "B": 6,
            "C": 3
            }
}

def score_rounds(input_string: str) -> int:
    rounds = [line.split() for line in input_string.strip().split("\n")]
    score = 0
    for rnd in rounds:
        score += STRATEGY[rnd[1]][rnd[0]] + MODIFIER[rnd[1]]
    return score

def score_rounds_unreadable(input_string: str) -> int:
    return sum([STRATEGY[rnd[1]][rnd[0]] + MODIFIER[rnd[1]] for rnd in [line.split() for line in input_string.strip().split("\n")]])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_string = f.read()
        print(score_rounds(input_string))
        print(score_rounds_unreadable(input_string))
