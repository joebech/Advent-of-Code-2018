import re
import numpy as np
import sys

# Load input file
text_file = open("input.dat", "r")
coordinates = text_file.read()
text_file.close()

# Getting coordinates
pos_x = [int(i) for i in re.findall(r'(\d+),',coordinates)]
pos_y = [int(i) for i in re.findall(r', (\d+)',coordinates)]

xy = list(zip(pos_x,pos_y))

# Create grid
grid = np.zeros((max(pos_y)+1,max(pos_x)+1), dtype = int)

# Calculate distance to all points for each grid point
for i in range(max(pos_y)+1):
    for j in range(max(pos_x)+1):
        dist = [abs(xy[ind][1]-i)+abs(xy[ind][0]-j) for ind in range(len(pos_x))]

        # Check if two points are equally close
        if sorted(dist)[0] == sorted(dist)[1]:
            continue
                
        # Find the nearest point
        min_value = min(dist)
        min_index = dist.index(min_value)
        grid[i,j] = min_index + 1

# Filter to only keep finite areas (Not on edge)
finite = set(range(1,len(pos_x) + 1))

top = set(grid[:1].flatten())
bot = set(grid[-1:].flatten())
left = set(grid[:,:1].flatten())
right = set(grid[:,-1:].flatten())
infinite = top.union(bot, left, right)

finite = list(finite-infinite)

area = [np.count_nonzero(grid == i) for i in finite]
print(max(area))
