players = 10
last_value = 1618

scores = players * [0]
circle = [0, 2, 1]
cur = 1
length = 3

for i in range(3,1618 + 1):
    player = i % players - 1
    
    if i % 23 == 0:
        
        scores[player] += i

    else:
        length += 1
        cur += 2
        
        if cur > length:
            
