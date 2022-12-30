from collections import defaultdict
from typing import Tuple

TEST_INPUT = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

DIR_MAP = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}


def count_visited(movements: str) -> int:
    instructions = [movement.split() for movement in movements.strip().splitlines()]
    visited = defaultdict(int)
    h_pos = t_pos = (0, 0)
    for instruction in instructions:
        moves = int(instruction[1])
        moves_made = 0
        while moves_made < moves:
            h_pos, t_pos = _move_knots(
                h_pos=h_pos, t_pos=t_pos, direction=instruction[0]
            )
            visited[t_pos] += 1
            moves_made += 1
    return len(visited.keys())


def _is_adjacent(h_pos: Tuple[int, int], t_pos: Tuple[int, int]) -> bool:
    return (abs(h_pos[0] - t_pos[0]) in [0, 1]) and (abs(h_pos[1] - t_pos[1]) in [0, 1])


def _move_knots(
    h_pos: Tuple[int, int], t_pos: Tuple[int, int], direction: str
) -> (Tuple[int, int], Tuple[int, int]):
    updated_h_pos = (h_pos[0] + DIR_MAP[direction][0], h_pos[1] + DIR_MAP[direction][1])
    updated_t_pos = list(t_pos)
    if not _is_adjacent(h_pos=updated_h_pos, t_pos=t_pos):
        # if pre-move position was diagonal + adjacent
        if h_pos[0] != t_pos[0] and h_pos[1] != t_pos[1]:
            updated_t_pos = h_pos
        elif h_pos[0] == t_pos[0]:
            # updated_t_pos[1] = updated_h_pos[1] + DIR_MAP[direction][1]
            updated_t_pos[1] = t_pos[1] + DIR_MAP[direction][1]
        elif h_pos[1] == t_pos[1]:
            # updated_t_pos[0] = updated_h_pos[0] + DIR_MAP[direction][0]
            updated_t_pos[0] = t_pos[0] + DIR_MAP[direction][0]
    return updated_h_pos, tuple(updated_t_pos)


if __name__ == "__main__":
    print(f"Expected part 1 answer with TEST_INPUT: 13")
    print(f"Computed visited coordinate count: {count_visited(TEST_INPUT)}")
    with open("input.txt", "r") as f:
        input_string = f.read()
        print(f"Part 1 - tail visited coordinate count: {count_visited(input_string)}")
