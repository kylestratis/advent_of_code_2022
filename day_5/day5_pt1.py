from collections import deque
import re
from typing import Tuple, List, Deque

TEST_INPUT = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def move_crates(input_string: str) -> Tuple[List[List], List[Tuple]]:
    stacks, directions = input_string.split("\n\n")
    built_stacks = _build_stacks(stacks)
    built_directions = _build_directions(directions)
    for idx, direction in enumerate(built_directions):
        # Move crates according to directions
        for _ in range(direction[0]):
            built_stacks[direction[2] - 1].appendleft(
                built_stacks[direction[1] - 1].popleft()
            )
    return "".join([stack[0] for stack in built_stacks])


def _build_stacks(stacks: str) -> List[Deque]:
    split_stacks = [
        split.replace("[", " ").replace("]", " ") for split in stacks.split("\n")
    ]
    num_stacks = int(
        split_stacks[-1].strip()[-1]
    )  # Get total number of stacks from last row of stacks
    parsed_stacks = [deque() for _ in range(num_stacks)]
    for row in split_stacks[:-1]:
        for idx, val in enumerate(row):
            # "Top" of each stack will be at the beginning of these
            if val != " ":
                parsed_stacks[int(split_stacks[-1][idx]) - 1].append(val)
    return parsed_stacks


def _build_directions(directions: str) -> List[Tuple]:
    """
    Builds list of tuples, 0th element is quantity to move, 1st is
    where to move qty from and 2nd where to move qty to
    """
    split_dirs = directions.strip().split("\n")
    direction_list = []
    for split_dir in split_dirs:
        direction_list.append(
            tuple([int(char) for char in split_dir.split() if char.isdigit()])
        )
    return direction_list


if __name__ == "__main__":
    print(move_crates(TEST_INPUT))
    with open("input.txt", "r") as f:
        input_string = f.read()
        print(move_crates(input_string))
