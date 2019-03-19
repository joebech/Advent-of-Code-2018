import re
import numpy as np
import sys

# Load input file
text_file = open("input.dat", "r")
instructions = text_file.read()
text_file.close()

# Getting coordinates
guide = re.findall(r'Step (\w) must be finished before step (\w)',instructions)

used_letters = []

for i in range(len(guide)): 
    used_letters.append(guide[i][0])
    used_letters.append(guide[i][1])

used_letters = list(set(used_letters))
rules = used_letters[:]
used_letters = ''.join(used_letters)

# Insert rules into a list
for i in range(len(guide)):
    letter_no = used_letters.index(guide[i][1])
    rules[letter_no] += guide[i][0]

#
order = []

for j in range(len(used_letters)):
    # Find unrestricted letters
    unrestricted = []
    for i in rules:
        if len(i) == 1:
            unrestricted.append(i)
      
    letter_next = sorted(unrestricted)[0]

    # Remove letter from everywhere in rules
    rules = [re.sub(letter_next, '', i) for i in rules]

    order.append(letter_next)
    
print(''.join(order))
