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

        if sum(dist) < 10000:
            grid[i,j] = 1

area = np.count_nonzero(grid == 1)
print(area)
