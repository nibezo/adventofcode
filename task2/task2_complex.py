# https://adventofcode.com/2021/day/2

data = open('input2.txt', 'r')

# convert the file to the list "data" line by line
data = data.readlines()

# list with all commands
commands = []
aim, horizontal_position, depth = 0, 0, 0

# delete \n
for line in data:
    commands.append(line.strip())

for command in commands:
    if command[0:4] == "down":
        aim += int(command[-1])
    elif command[0:2] == "up":
        aim -= int(command[-1])
    elif command[0:7] == "forward":
        horizontal_position += int(command[-1])
        depth += aim * int(command[-1])

print(f"Result is {horizontal_position * depth}")
