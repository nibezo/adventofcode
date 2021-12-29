# https://adventofcode.com/2021/day/2

f = open('input2.txt', 'r')

# convert the file to the list "data" line by line
data = f.readlines()
f.close()
# list with all commands
commands = []
horizontal_position, depth = 0, 0

# delete \n
for line in data:
    commands.append(line.strip())

for command in commands:
    if command.startswith("down"):
        depth += int(command[-1])
    elif command.startswith("up"):
        depth -= int(command[-1])
    elif command.startswith("forward"):
        horizontal_position += int(command[-1])

print(f"Result is {horizontal_position * depth}")

