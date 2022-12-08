import pandas as pd
import numpy as np

data = []

data = []
with open("./data/day8.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        data.append(line.strip())

matrix = np.empty((len(data), len(data[0])))

for row, line in enumerate(data):
    for column, value in enumerate(line):
        matrix[row][column] = value 
test_matrix = [[3,0,3,7,3], 
                [2,5,5,1,2], 
                [6,5,3,3,2], 
                [3,3,5,4,9], 
                [3,5,3,9,0]]
#matrix = test_matrix

#Must be hidden from all sides 
outside_trees = 99*4 - 4
counter_blocked = 0 #times a tree is hidden from all angles
counter = 0 #if the tree is viewable from any angle
for row, line in enumerate(matrix):
    for column, value in enumerate(line):
        if row > 0 and column > 0 and row < len(matrix)-1 and column < len(line)-1:
           
            col_pre, col_aft, row_pre, row_aft = False, False, False, False
            for count, row_value in enumerate(line[0:column]):
                if row_value >= value:
                    col_pre = True
                    break

            for count2, row_value2 in enumerate(line[column+1:]):
                
                if row_value2 >= value:
                    col_aft = True
                    break

            for count3, line2 in enumerate(matrix[0:row]):
                
                if line2[column] >= value:
                    row_pre = True
                    break

            for count4, line3 in enumerate(matrix[row+1:]):
                
                if line3[column] >= value:
                    row_aft = True
                    break

            if row_aft == True and row_pre == True and col_aft == True and col_pre == True:
                counter_blocked += 1
            else:
                counter += 1
                

print("trees on the edge: " + str(outside_trees))
print("Visable Trees inside:" +str(counter))
print("Part 1: total visable trees: " + str(counter + outside_trees))



#----------------Part 2----------------
scenic_value = 0
for row, line in enumerate(matrix):
    for column, value in enumerate(line):
        if row > 0 and column > 0 and row < len(matrix)-1 and column < len(line)-1:
           
            scen_col_pre, scen_col_aft, scen_row_pre, scen_row_aft = 0, 0, 0, 0
            col_pre, col_aft, row_pre, row_aft = False, False, False, False
            for count, row_value in enumerate(np.flip(line[0:column])):
                scen_row_pre += 1
                if row_value >= value:
                    col_pre = True
                    break
                

            for count2, row_value2 in enumerate(line[column+1:]):
                scen_row_aft += 1
                if row_value2 >= value:
                    col_aft = True
                    break
                

            for count3, line2 in enumerate(np.flip(matrix[0:row], axis= 0)):
                scen_col_pre += 1
                if line2[column] >= value:
                    row_pre = True
                    break
                

            for count4, line3 in enumerate(matrix[row+1:]):
                scen_col_aft += 1
                if line3[column] >= value:
                    row_aft = True
                    break
                
            if row_aft == True and row_pre == True and col_aft == True and col_pre == True:
                counter_blocked += 1
            else:
                counter += 1
            
            current_scenic_value = scen_col_aft*scen_col_pre*scen_row_aft*scen_row_pre
            if  current_scenic_value > scenic_value:
                scenic_value = current_scenic_value
                
print("Part 2: Scenic Value: " + str(scenic_value))



