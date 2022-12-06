import pandas as pd

data = pd.read_csv("./data/day6.txt", header=None)

# part 1
for count, char in enumerate(data[0][0]):
    if count > 3:
        if char != data[0][0][count - 1] and char != data[0][0][count - 2] and char != data[0][0][count - 3]:
            if data[0][0][count - 1] != data[0][0][count - 2] and data[0][0][count - 1] != data[0][0][count - 3]:
                if data[0][0][count - 2] != data[0][0][count - 3]:
                    break


print(count +1) #answer part 1



#part 2


def find_dup(char, string):
    if char in string:
        thing = False
    else: 
        thing = True
    return thing


for count, char in enumerate(data[0][0]):
    counter = 0
    if count > 13:
        for t in range(13):
            if find_dup(data[0][0][count-t], string= data[0][0][count-13:count - t]) == True:
                counter += 1    
    if counter == 13:
        break


print(count +1) #answer part  2