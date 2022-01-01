# https://adventofcode.com/2020/day/1

# read all expenses from file and make a list with them
expenses = open('input1.txt', 'r').readlines()
expenses = [int(i.translate({ord("\n"): ""})) for i in expenses]

for first in expenses:
    for second in expenses:
        if first + second == 2020:
            answer = first * second

print(f'Answer is {str()}')
