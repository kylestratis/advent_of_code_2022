TEST_INPUT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def find_overlaps(input_string: str) -> int:
    groups = [line.split(",") for line in input_string.strip().split("\n")]
    count = 0
    for group in groups:
        group = [list(map(int, num.split("-"))) for num in group]
        if (
            group[0][0] <= group[1][0]
            and group[0][1] >= group[1][1]
        ) or (
            group[0][0] >= group[1][0]
            and group[0][1] <= group[1][1]
        ):
            count += 1
    return count


def find_any_overlap(input_string: str) -> int:
    groups = [line.split(",") for line in input_string.strip().split("\n")]
    count = 0
    for group in groups:
        group = sum([list(map(int, num.split("-"))) for num in group], [])
        mindex = group.index(min(group))
        if group[mindex] <= group[(mindex + 2) % 4] <= group[mindex + 1]:
            count += 1
    return count
        


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_string = f.read()
        print(find_overlaps(input_string))
        print(find_any_overlap(input_string))
