"""
Prompt: Using the previous problem as context, write the code that will answer the question posed in the following 
problem in Python 3 in as few lines as possible: <AoC prompt>

Response: Here is a possible solution to the problem using Python 3 that uses as few lines as possible: <code>

This script reads the input from a file called "input.txt" and expects each line to contain a single integer 
representing the number of Calories of each food item. It then groups the Calories by Elf using an empty
line as a delimiter, sorts the groups by their total Calories in descending order, and prints the total
Calories carried by the top three Elves.

For example, given the input: <input>

The script would output:
The top three Elves are carrying a total of 45000 calories

Note that this solution assumes that the input is well-formed and that each line containing an integer 
is followed by an empty line, except for the last line. It also assumes that the numbers in the input 
file are separated by a newline character. Additionally, this solution requires the itertools module,
which is not included in the Python standard library but can be installed using pip.

NOTE from the human: itertools is indeed a part of the Python standard library. This also won't run because
ChatGPT again omitted the import statement for itertools.
"""

with open("input.txt", "r") as f:
  groups = [[int(line.strip()) for line in g if line.strip()] for k, g in itertools.groupby(f, lambda x: x == "\n") if not k]
most_calories = sorted(groups, key=sum, reverse=True)[:3]
total_calories = sum(sum(group) for group in most_calories)
print("The top three Elves are carrying a total of %d calories" % total_calories)

