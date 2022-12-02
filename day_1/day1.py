TEST_INPUT = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def compute_calories(input_string: str) -> int:
    splits = [num.split("\n") for num in input_string.split("\n\n")]
    max_cals = 0
    for elf in splits:
        total = sum([int(x) for x in elf if x])
        max_cals = max(total, max_cals)
    return max_cals


def compute_calories_unreadable(input_string: str) -> int:
    return max(
        sum([int(x) for x in split if x])
        for split in [num.split("\n") for num in input_string.split("\n\n")]
    )


def compute_calories_top_three(input_string: str) -> int:
    return sum(
        sorted(
            [
                sum([int(x) for x in split if x])
                for split in [num.split("\n") for num in input_string.split("\n\n")]
            ],
            reverse=True,
        )[:3]
    )


if __name__ == "__main__":
    # TODO: open file and read into string
    with open("input.txt", "r") as f:
        input_string = f.read()
        print(compute_calories_unreadable(input_string))
        assert compute_calories_unreadable(input_string) == compute_calories(
            input_string
        )
        print(compute_calories_top_three(input_string))
        assert compute_calories_top_three(TEST_INPUT) == 45000
