"""
Prompt: Read the following instructions and write code in clean, concise Python to answer the question at the end.

"<Prompt of both parts of day 2 with part 1 question area removed>"

NOTES from the human:
On the surface this looks like it makes sense, but upon closer inspection (or just running), the list comprehensions that are supposed to determine the shape_to_choose make no sense. There are two nearly identifical list comprehensions that are very convoluted ways to determine which shape to use. In the first case, the list comprehension at least works and correctly does what it's supposed to, even though it is far from ideal for readability.

The second case is a different story. It constructs the same list and gets the first (and only) value, but inexplicably tries to take the modulo 3 of that string, and then add 1 to it. This, naturally, leads to a TypeError.

Even with that strange bug, the broad ideas implemented show an "understanding" of the problem that is impressive. The bug, however, shows us it doesn't truly understand the problem.
"""

TEST_INPUT = """
A Y
B X
C Z
"""


def score_rounds(strategy_string):
    # Define the scores for each shape and outcome
    shape_scores = {"A": 1, "B": 2, "C": 3}
    outcome_scores = {"X": 0, "Y": 3, "Z": 6}

    # Split the strategy string into lines
    strategy_lines = strategy_string.strip().split("\n")

    # Initialize the total score to 0
    total_score = 0

    # Iterate over each line in the strategy string
    for line in strategy_lines:
        # Split the line into opponent's choice and desired outcome
        opponent_choice, desired_outcome = line.split()

        # Determine the shape to choose based on the desired outcome
        # If we need to win, we choose the shape that defeats the opponent's choice
        # If we need to lose, we choose the shape that is defeated by the opponent's choice
        # If we need to draw, we choose the same shape as the opponent
        if desired_outcome == "Z":
            shape_to_choose = [
                s
                for s in "ABC"
                if shape_scores[opponent_choice] % 3 + 1 == shape_scores[s]
            ][0]
        elif desired_outcome == "X":
            shape_to_choose = [
                s
                for s in "ABC"
                if shape_scores[opponent_choice] % 3 + 1 == shape_scores[s]
            ][0] % 3 + 1
        else:
            shape_to_choose = opponent_choice

        # Calculate the score for this round
        round_score = shape_scores[shape_to_choose] + outcome_scores[desired_outcome]

        # Add the round score to the total score
        total_score += round_score

    # Return the total score
    return total_score


if __name__ == "__main__":
    print(score_rounds(TEST_INPUT))
