TEST_INPUT = """
A Y
B X
C Z
"""


MODIFIER = {"A": 1, "B": 2, "C": 3}

TRANSFORMER = {"X": (-1, 0), "Y": (0, 3), "Z": (1, 6)}


def score_rounds(input_string: str) -> int:
    rounds = [line.split() for line in input_string.strip().split("\n")]
    score = 0
    for rnd in rounds:
        modifier = MODIFIER["ABC"[("ABC".index(rnd[0]) + TRANSFORMER[rnd[1]][0]) % 3]]
        result = TRANSFORMER[rnd[1]][1]
        score += modifier + result
    return score


def score_rounds_unreadable(input_string: str) -> int:
    return sum(
        [
            MODIFIER["ABC"[("ABC".index(rnd[0]) + TRANSFORMER[rnd[1]][0]) % 3]]
            + TRANSFORMER[rnd[1]][1]
            for rnd in [line.split() for line in input_string.strip().split("\n")]
        ]
    )


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_string = f.read()
        print(score_rounds(input_string))
        print(score_rounds_unreadable(input_string))
