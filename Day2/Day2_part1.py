# Load input file
text_file = open("input.dat", "r")
box_id = text_file.read().split('\n')
text_file.close()

# Letters
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Variables
count_2 = 0
count_3 = 0

# Looping over all ID's
for i in box_id:
    check_2 = False
    check_3 = False
    
    for letter in alphabet:
        occ = i.count(letter)
        
        if occ == 2 and not check_2:
            check_2 = True
            count_2 += 1
        elif occ == 3 and not check_3:
            check_3 = True
            count_3 += 1
            
        if check_2 and check_3:
            break

print(count_2 * count_3)
