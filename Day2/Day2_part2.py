import re
import sys

# Load input file
text_file = open("input.dat", "r")
box_id = text_file.read().split('\n')
text_file.close()

while box_id:
    for i in box_id[1:]:
        for letter in range(1,len(box_id[0])):
            pattern = box_id[0][:letter] + '\\w' + box_id[0][letter+1:]
            match = re.match(pattern, i)

            if match:
                print(box_id[0][:letter] + box_id[0][letter+1:])
                sys.exit()

    del box_id[0]
