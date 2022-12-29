import math

TEST_INPUT = """
30373
25512
65332
33549
35390
"""


def count_visible_trees(grid: str) -> int:
    rows = grid.split()
    columns = ["".join(x) for x in zip(*rows)]
    # Initialize count to count all the outer trees of the grid
    count = len(rows[0]) * 2 + (len(rows) - 2) * 2

    for row_idx, row in enumerate(rows[1:-1]):
        row_idx += 1
        for col_idx, value in enumerate(row[1:-1]):
            col_idx += 1
            # Get subcolumns and subrows non-inclusive of value in question
            above_subcolumn = columns[col_idx][:row_idx]
            below_subcolumn = columns[col_idx][row_idx + 1 :]
            row_behind = row[:col_idx]
            row_ahead = row[col_idx + 1 :]
            # Check column above
            if value > max(above_subcolumn):
                count += 1
                continue
            # Check column below
            elif value > max(below_subcolumn):
                count += 1
                continue
            # Check row behind
            elif value > max(row_behind):
                count += 1
                continue
            # Check row ahead
            elif value > max(row_ahead):
                count += 1
                continue
    return count


def get_best_scenic_score(grid: str) -> int:
    """
    Answers part 2
    """
    rows = grid.split()
    columns = ["".join(x) for x in zip(*rows)]
    scenic_scores = []
    for row_idx, row in enumerate(rows[1:-1]):
        row_idx += 1
        for col_idx, value in enumerate(row[1:-1]):
            col_idx += 1
            """
            Get subcolumns and subrows non-inclusive of value in question
            Reversing the list normalizes the above subcolumn and row_behind
            to be from the perspective of the tree (value) we're examining.
            This allows us to use a single index ([0]) when getting the nearest
            taller tree.
            """
            scenic_score = []
            above_subcolumn = list(reversed(columns[col_idx][:row_idx]))
            below_subcolumn = columns[col_idx][row_idx + 1 :]
            row_behind = list(reversed(row[:col_idx]))
            row_ahead = row[col_idx + 1 :]
            for direction in (above_subcolumn, below_subcolumn, row_behind, row_ahead):
                if value > max(direction):
                    scenic_score.append(len(direction))
                else:
                    distance = [
                        direction.index(tree) for tree in direction if tree >= value
                    ][0] + 1
                    scenic_score.append(distance)
            scenic_scores.append(math.prod(scenic_score))
    return max(scenic_scores)


if __name__ == "__main__":
    print(f"Expected answer with test input: 21")
    print(f"Computed answer with test input: {count_visible_trees(grid=TEST_INPUT)}")
    print(f"Expected answer for part 2 with test input: 8")
    print(f"Part 2 with test input {get_best_scenic_score(TEST_INPUT)}")
    with open("input.txt", "r") as f:
        input_string = f.read()
        print(f"Part 1 count {count_visible_trees(grid=input_string)}")
        print(f"Part 2 best scenic score: {get_best_scenic_score(grid=input_string)}")
