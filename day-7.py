
data = []
with open("./data/day7.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        data.append(line.strip())


dir = [["name"], ["size"]]


