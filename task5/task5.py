# https://adventofcode.com/2021/day/5
data = open('input5.txt', 'r').readlines()
lines = {}

# make a list from data in a format [[x, y] [x1, y1] ... ]
for i in range(len(data)):
    data[i] = data[i].replace(" -> ", ' ')
    data[i] = data[i].replace("\n", '')
    data[i] = data[i].replace(",", '.')
    data[i] = list(data[i].split(" "))

for i in range(len(data)):
    for k in range(1):
        lines[float(data[i][k])] = float(data[i][k+1])

