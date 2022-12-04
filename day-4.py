import pandas as pd

data = pd.read_csv("./data/day4.txt", delimiter=",",header=None)

counter = 0
counter2 = 0
for count, i in enumerate(data[0]):
    elv1 = i.split("-")
    elv2 = data[1][count].split("-")

    if int(elv1[0]) <= int(elv2[0]) and int(elv1[1]) >= int(elv2[1]):
        counter += 1
    
    elif int(elv1[0]) >= int(elv2[0]) and int(elv1[1]) <= int(elv2[1]):
        counter += 1
        

    #part 2
    if int(elv1[0]) >= int(elv2[0]) and int(elv1[0]) <= int(elv2[1]):
        counter2 += 1
    
    elif int(elv1[1]) <= int(elv2[1]) and int(elv1[1]) >= int(elv2[0]):
        counter2 += 1
    
    elif int(elv1[0]) < int(elv2[0]) and int(elv1[1]) > int(elv2[1]):
        counter2 += 1

    elif int(elv2[0]) < int(elv1[0]) and int(elv2[1]) > int(elv1[1]):
        counter2 += 1

    else:
        print(elv1 + elv2)

print(counter)
print(counter2)
