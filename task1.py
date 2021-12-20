data = open('input1.txt', 'r')

# convert the file to the list "nums" line by line
nums = data.readlines()

# list with all
numbers = []
i, result = 0, 0

# delete \n
for line in nums:
    numbers.append(line.strip())

# find the result
for element in numbers:
    previous = int(element)
    if previous > int(numbers[i-1]) and i >= 1:
        result += 1
    i += 1

print(f"Result is {result}")

data.close()
