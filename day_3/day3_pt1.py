"""
Note from the human:
    This actually looks really good. Cleaner than my solution, and it gives the correct answer for the given input.
    Normally I would wonder if it had seen solutions to this problem now that I'm 9 days behind, but ChatGPT was
    trained on data that stops at 2021 (unless this isn't a brand new problem). This one was impressive. And just a reminder
    that I only ask ChatGPT the exact question as it comes from Advent of Code. I was on a new session and didn't even
    specify writing in Python, but ChatGPT did (although context may be saved per user between sessions).
    Another run I did with the same prompt just gave a nested for loop and comments for the heavy lifting.
"""

# Parse the input
lines = [line.strip() for line in open("input.txt")]

# The sum of the priorities of the item types that appear in both compartments
# of each rucksack
result = 0

# For each rucksack
for line in lines:
  # Split the rucksack contents into two compartments
  first_compartment = line[:len(line)//2]
  second_compartment = line[len(line)//2:]

  # Find the item type that appears in both compartments
  common_type = set(first_compartment).intersection(set(second_compartment)).pop()

  # Compute the priority of the common item type
  if common_type.islower():
    priority = ord(common_type) - ord("a") + 1
  else:
    priority = ord(common_type) - ord("A") + 27

  # Add the priority to the result
  result += priority

# Print the result
print(result)
