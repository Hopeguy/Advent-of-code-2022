import pandas as pd
import numpy as np
import time

start = time.time()
data = pd.read_csv("./Data/Day-1-1.csv", delimiter=" ", header = None, skip_blank_lines=False)

elv_list = []

combined = 0
for elv in data[0]:
    if pd.isna(elv) == False:
        combined += elv
    if pd.isna(elv) == True:
        elv_list.append(combined)
        combined = 0
elv_list.sort(reverse=True)
print(sum(elv_list[0:3]))


end = time.time()

print(abs(end-start))

