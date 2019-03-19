import re
import numpy as np
import sys

# Load input file
text_file = open("input2.dat", "r")
poly = text_file.read()
text_file.close()

# Create pattern for regex

alphabet = 'abcdefghijklmnopqrstuvwxyz'
pattern = ''

for char in alphabet:
    combo = char + char.upper()
    pattern += combo + '|' + combo[::-1] + '|'

pattern = pattern[:-1]

done = 0
#print(poly)
while done == 0:
    # Find index of all matches
    ind = [m.span() for m in re.finditer(pattern, poly)]
    #print(ind)
    if not ind:
        done = 1
        break

    # Remove all matches except overlaps
    for i in range(len(ind)):
        poly = poly[:ind[i][0]-2*i] + poly[ind[i][1]-2*i:]
    #print(poly)

# Return length of final string
print(len(poly))
