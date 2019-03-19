import re
import sys

# Load input file
text_file = open("inputtest.dat", "r")
data = text_file.read()
text_file.close()

# Convert data into list of int
data = [int(i) for i in data.split(' ')]
meta_sum = 0
pos = []
i = 0

while i < len(data):
    if data[i] > 0:
        pos.append(data[i:i+2])
        i += 2
    else:
        meta_sum += sum(data[i+2 : i+2+data[i+1]])
        pos[-1][0] -= 1
        i += 2 + data[i+1]

    if pos[-1][0] == 0:
        meta_sum += sum(data[i : i + pos[-1][1]])
        del pos[-1]
        pos[-1][0] -= 1
        
        
    print(pos)
    print(meta_sum)

print(data)
print(meta_sum)
