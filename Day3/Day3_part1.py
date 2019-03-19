import re
import numpy as np
import sys

# Load input file
text_file = open("input.dat", "r")
patches = text_file.read()
text_file.close()

# Regex to find values and convert to integer
patch_no = [int(i) for i in re.findall(r'#(\d+)',patches)]
pos_x = [int(i) for i in re.findall(r'@ (\d+)',patches)]
pos_y = [int(i) for i in re.findall(r',(\d+)',patches)]
size_x = [int(i) for i in re.findall(r': (\d+)',patches)]
size_y = [int(i) for i in re.findall(r'x(\d+)',patches)]

# Find size
max_x = max([x + y for x, y in zip(pos_x, size_x)])
max_y = max([x + y for x, y in zip(pos_y, size_y)])

# Making the fabric
fabric = np.zeros((max_x,max_y),dtype=np.int)

# Inserting all patches into the fabric
for i in range(len(patch_no)):
    claim = np.ones((size_x[i],size_y[i]),dtype=np.int)
    fabric[pos_x[i]:pos_x[i]+claim.shape[0], pos_y[i]:pos_y[i]+claim.shape[1]] += claim

# Makes matrix where the boolean below is true and counts all True values
print((1 < fabric).sum())

# Question 2. Which patch does not overlap
for i in range(len(patch_no)):
    claim = np.ones((size_x[i],size_y[i]),dtype=np.int)
    relevant_fab = fabric[pos_x[i]:pos_x[i]+claim.shape[0], pos_y[i]:pos_y[i]+claim.shape[1]]

    # Checking if all values are below 2.    
    if (relevant_fab < 2).sum() == size_x[i] * size_y[i]:
        print(patch_no[i])
        sys.exit()
