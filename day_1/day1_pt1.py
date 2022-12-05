"""
Prompt:
Write a Python 3 script to solve the following problem and write the answer as derived by the script: <AoC Day 1 pt 1 prompt>

Response:
This script reads the input from a file called "input.txt" and expects each line to contain a single integer representing 
the number of Calories of each food item. It then groups the Calories by Elf using an empty line as a delimiter, finds 
the group with the most Calories, and prints the result in the format "Elf X is carrying the most calories: Y".
...
Note that this solution assumes that the input is well-formed and that each line containing an integer is followed by 
an empty line, except for the last line. It also assumes that the numbers in the input file are separated by a newline character.
---

"""

with open("input.txt", "r") as f:
  groups = [[int(line.strip()) for line in g if line.strip()] for k, g in itertools.groupby(f, lambda x: x == "\n") if not k]
most_calories = max(sum(group) for group in groups)
most_caloric_elf = groups.index(most_calories)
print("Elf %d is carrying the most calories: %d" % (most_caloric_elf, most_calories))
