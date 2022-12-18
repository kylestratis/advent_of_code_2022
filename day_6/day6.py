TEST_STRINGS_PT1 = [
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]

TEST_STRINGS_PT2 = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]


def detect_marker(data_stream: str) -> int:
    for idx, _ in enumerate(data_stream[:-3]):
        if len(set(data_stream[idx : idx + 4])) == len(data_stream[idx : idx + 4]):
            return idx + 4


# Part 2
def detect_message(data_stream: str) -> int:
    for idx, _ in enumerate(data_stream[:-13]):
        if len(set(data_stream[idx : idx + 14])) == len(data_stream[idx : idx + 14]):
            return idx + 14


if __name__ == "__main__":
    print("Part 1 tests")
    for s in TEST_STRINGS_PT1:
        print(detect_marker(s))
    print("Part 2 tests")
    for s in TEST_STRINGS_PT2:
        print(detect_message(s))
    print("Real input")
    with open("input.txt", "r") as f:
        input_string = f.read()
        print(f"Part 1 answer: {detect_marker(input_string)}")
        print(f"Part 2 answer: {detect_message(input_string)}")
