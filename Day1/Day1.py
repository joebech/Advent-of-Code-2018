import sys
# Load input file
text_file = open("Day1_Input.dat", "r")
lines = text_file.read().split('\n')
text_file.close()

# Convert str to int
lines = [int(i) for i in lines[:-1]]

# Calculate sum - Answer 1
print(sum(lines))


freq = []
count = 0
i = 0

while i < 1000:
    for change in lines:
        count += change
        if count in freq:
            print(count)
            sys.exit()
        freq.append(count)
    i += 1
