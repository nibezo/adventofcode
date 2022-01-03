#  https://adventofcode.com/2020/day/2
passwords = open("input2.txt", 'r').readlines()
passwords = [str(i.translate({ord("\n"): ""})) for i in passwords]
count = 0

for password in passwords:
    min_count = int(password[0:password.find("-")])
    max_count = int(password[password.find("-")+1:password.find(" ")])
    letter = password[password.find(":")-1]
    check_password = password[password.find(":")+2:len(password)+1]
    print(check_password)
    if min_count <= check_password.count(letter) <= max_count:
        count += 1

print(f"Count of valid passwords: {count}")
