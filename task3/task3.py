# https://adventofcode.com/2021/day/3
data = open('input3.txt', 'r')

# convert the file to the list "binaries" line by line
data = data.readlines()

# list with all
binaries_old = []
binaries_new = []
result, row = 0, ''
gamma_rate, epsilon_rate = '', ''

# delete \n
for line in data:
    binaries_old.append(line.strip())

# replace rows to columns
for i in range(0, 12):
    for bit in binaries_old:
        row += bit[i]
    binaries_new.append(row)
    row = ''


for i in range(0, 12):
    # count the number of zero bits and one bits
    zero = binaries_new[i].count('0')
    one = binaries_new[i].count('1')

    # create gamma_rate and epsilon_rate
    # gamma_rate is the most used "1" bits
    # epsilon_rate is the most used "0" bits
    if one > zero:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

# convert binary to decimal with int(x, 2) function
gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print(f"Result is {gamma_rate * epsilon_rate}")
