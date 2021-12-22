# https://adventofcode.com/2021/day/6
lanternfish = open('input6.txt', 'r').readlines()

# make the list, delete ",", str -> int
lanternfish = [int(i) for i in lanternfish[0].translate({ord(","): " "}).split()]

for days in range(80):
    for fish in range(len(lanternfish)):
        if lanternfish[fish] == 0:
            lanternfish[fish] = 6
            lanternfish.append(8)
        elif lanternfish[fish] <= 8:
            lanternfish[fish] -= 1
print(len(lanternfish))
