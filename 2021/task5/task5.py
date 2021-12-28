# https://adventofcode.com/2021/day/5
import numpy as np

data = open('input5.txt', 'r').readlines()
x1x2, y1y2, matrix = [], [], []
for i in range(len(data)):
    x1x2.append(int(data[i][0:data[i].find(',')]))
    x1x2.append(int(data[i][data[i].find(',')+1:data[i].find(' ')]))
    data[i] = data[i][data[i].find('>')+2:len(data)]
    data[i] = data[i].replace('\n', '')
    y1y2.append(int(data[i][0:data[i].find(',')]))
    y1y2.append(int(data[i][data[i].find(',')+1:len(data[i])]))
max_x, max_y = np.amax(x1x2), np.amax(y1y2)
for i in range(int(len(x1x2)/2)):
    matrix.append([])
print(max_y)
m = np.zeros(max_x, max_y)
print(m[1])
