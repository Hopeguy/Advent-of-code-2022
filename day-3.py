import pandas as pd
import numpy as np


data = pd.read_csv("./data/day3.txt", header=None)


#Part 1
letters = []
for rucksac in data[0]:
        for letter in rucksac[0:int((len(rucksac)/2))]:
            if letter in rucksac[int((len(rucksac)/2)):len(rucksac)]:
                letters.append(letter)

                break
            


alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = alphabet_big.lower()
combined = alphabet + alphabet_big

let_dict = {}

for count, letter in enumerate(combined):
    let_dict[letter] = count +1

summed_prio = 0
for letter in letters:
    summed_prio += let_dict[letter]

print(summed_prio)


#part 2
counter = 0
groups = []
for length in range(int(len(data[0])/3)):
    groups.append([data[0][counter], data[0][counter +1],data[0][counter +2]])
    counter += 3

letter_groups = []

for group in groups:
    for letter in group[0]:
        if letter in group[1]:
            if letter in group[2]:
                letter_groups.append(letter)
                break

summed_group = 0
for letter in letter_groups:
    summed_group += let_dict[letter]


print(summed_group)