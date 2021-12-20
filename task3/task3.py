data = open('input3.txt', 'r')

# convert the file to the list "binaries" line by line
data = data.readlines()

# list with all
binaries = []
i, result = 0, 0
gamma_rate, epsilon_rate = '0', '0'

# delete \n
for line in data:
    binaries.append(line.strip())

for rows in binaries:
    for column in binaries:
        pass


gamma_rate = int(gamma_rate)
epsilon_rate = int(epsilon_rate)

print(f"Result is {gamma_rate * epsilon_rate}")
print(len(binaries[1]))
