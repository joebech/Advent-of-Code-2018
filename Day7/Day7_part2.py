import re
import numpy as np
import sys

# Load input file
text_file = open("inputtest.dat", "r")
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
done = []
no_workers = 2
workers = [0 for i in range(no_workers)]
workers_job = ['.' for i in range(no_workers)]
time = 0
fixed_dur = 0
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while len(done) < len(used_letters):
    # Find available workers
    workers_avail = workers.count(0)

    if workers_avail == 0:
        workers = [i-1 for i in workers]

        for i in range(len(workers)):
            if workers[i] == 0:
                done.append(workers_job[i])
                rules = [re.sub(workers_job[i], '', i) for i in rules]
                workers_job[i] = '.'
        time += 1
        continue
    
    # Find unrestricted letters
    unrestricted = []
    for i in rules:
        if len(i) == 1:
            unrestricted.append(i)

    unrestricted.sort()

    # Assign available workers unrestricted letters
    for i in range(len(unrestricted)):
        for j in range(len(workers)):
            if workers[j] == 0:
                workers[j] = fixed_dur + alphabet.index(unrestricted[i])
                workers_job[j] = unrestricted[i]

    # Work
    workers = [i-1 if i is not 0 else '.' for i in workers]

    for i in range(len(workers)):
        if workers[i] == 0 and workers_job[i] != '.':
            done.append(workers_job[i])
            rules = [re.sub(workers_job[i], '', i) for i in rules]
            workers_job[i] = '.'
    time += 1

print(time)
