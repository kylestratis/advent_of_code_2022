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
    print(f"Initial outer count: {count}")

    for row_idx, row in enumerate(rows[1:-1]):
        row_idx += 1
        for col_idx, value in enumerate(row[1:-1]):
            col_idx += 1
            # Get subcolumns and subrows non-inclusive of value in question
            above_subcolumn = columns[col_idx][:row_idx]
            below_subcolumn = columns[col_idx][row_idx + 1:]
            row_behind = row[:col_idx]
            row_ahead = row[col_idx + 1:]
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
        

if __name__ == "__main__":
    print(f"Expected answer with test input: 21")
    print(f"Computed answer with test input: {count_visible_trees(grid=TEST_INPUT)}")
    with open("input.txt", "r") as f:
        input_string = f.read()
        print(f"Part 1 count {count_visible_trees(grid=input_string)}")
