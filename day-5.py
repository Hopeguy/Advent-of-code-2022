import pandas as pd

#            [C]         [N] [R]    
#[J] [T]     [H]         [P] [L]    
#[F] [S] [T] [B]         [M] [D]    
#[C] [L] [J] [Z] [S]     [L] [B]    
#[N] [Q] [G] [J] [J]     [F] [F] [R]
#[D] [V] [B] [L] [B] [Q] [D] [M] [T]
#[B] [Z] [Z] [T] [V] [S] [V] [S] [D]
#[W] [P] [P] [D] [G] [P] [B] [P] [V]
# 1   2   3   4   5   6   7   8   9 

crates = [["W","B", "D", "N", "C", "F", "J"], ["P", "Z", "V", "Q", "L", "S", "T"], 
            ["P", "Z", "B", "G", "J", "T"], ["D", "T", "L", "J", "Z", "B", "H", "C"],
            ["G", "V", "B", "J", "S"], ["P", "S", "Q"],
            ["B", "V", "D", "F", "L", "M", "P", "N"], ["P", "S", "M", "F", "B", "D", "L", "R"],
            ["V", "D", "T", "R"]]

Moves = pd.read_csv("./data/day5.txt", header=None)

Moves_fixed = [] #first is number of boxes to move, second is from where, and last is to where

for move in Moves[0]:
    specific_move = []
    for value in move:
        try: 
            int(value)
            specific_move.append(value)
            
        except: ValueError
    Moves_fixed.append(specific_move)


for count, move in enumerate(Moves_fixed):
    if len(move) == 4:
        new_value = move[0] + move[1]
        Moves_fixed[count].pop(0)
        Moves_fixed[count][0] = new_value


for move in Moves_fixed:
    to_move = crates[int(move[1])-1][-int(move[0]):]
    to_move.reverse()
    crates[int(move[1])-1] = crates[int(move[1])-1][0:len(crates[int(move[1])-1]) -int(move[0])]
    for i in to_move:
        crates[int(move[2])-1].append(i)

word = ""
for i in crates:
    word += i[-1]

#part 2 remove line 43 (to_move.reverse())

print(word)
