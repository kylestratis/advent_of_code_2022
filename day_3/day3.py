TEST_INPUT = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

TEST_RESULT = 157

SCORING = [chr(i) for i in range(97, 123)]
SCORING.extend([chr(i) for i in range(65, 92)])


# Part 1
def compartmentalize(input_string: str) -> int:
    rucksacks = [line for line in input_string.strip().split("\n")]
    score = 0
    for rucksack in rucksacks:
        first_half, second_half = (
            rucksack[: len(rucksack) // 2],
            rucksack[len(rucksack) // 2 :],
        )
        recombined = sorted(list(set(first_half)) + list(set(second_half)))
        for idx, item in enumerate(recombined[:-1]):
            if item == recombined[idx + 1]:
                score += SCORING.index(item) + 1
    return score

# Part 2
def score_uniques(input_string: str) -> int:
    rucksacks = [line for line in input_string.strip().split("\n")]
    score = 0
    group = []
    for idx, rucksack in enumerate(rucksacks):
        group.append(set(rucksack))
        if (idx + 1) % 3 == 0:
            unique = group[0].intersection(group[1]).intersection(group[2])
            score += SCORING.index(unique.pop()) + 1
            group.clear()
    return score


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_string = f.read()
        print(f"Part 1 score {compartmentalize(input_string)}")
        print(score_uniques(TEST_INPUT))
        print(f"Part 2 score {score_uniques(input_string)}")
