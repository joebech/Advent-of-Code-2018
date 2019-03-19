import re
import numpy as np
import sys

# Load input file
text_file = open("input2.dat", "r")
poly = text_file.read()
text_file.close()

# Remove 1 unit at a time
alphabet = 'abcdefghijklmnopqrstuvwxyz'
reduced = []

for ichar in alphabet:
    # Load again
    text_file = open("input2.dat", "r")
    poly = text_file.read()
    text_file.close()
    
    rem_pat = ichar + '|' + ichar.upper()

    # Find index of all matches
    ind = [m.span() for m in re.finditer(rem_pat, poly)]

    # Remove all matches except overlaps
    for i in range(len(ind)):
        poly = poly[:ind[i][0]-i] + poly[ind[i][1]-i:]
        
    # Create pattern for regex

    pattern = ''

    for char in alphabet:
        combo = char + char.upper()
        pattern += combo + '|' + combo[::-1] + '|'

    pattern = pattern[:-1]

    done = 0
    
    while done == 0:
        # Find index of all matches
        ind = [m.span() for m in re.finditer(pattern, poly)]
        
        if not ind:
            done = 1
            break

        # Remove all matches except overlaps
        for i in range(len(ind)):
            poly = poly[:ind[i][0]-2*i] + poly[ind[i][1]-2*i:]
        

    # Return length of final string
    print(len(poly))
    reduced.append(len(poly))

print(min(reduced))
