import sys

n = sys.stdin.readline().rstrip()
numbers = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().rstrip())

number_dict = {}
count = 0

# convert to dictionary
for i, v in enumerate(numbers):
    number_dict[v] = i

# check if number in dictionary
for i, v in enumerate(numbers):
    need_number = x - v

    if need_number in number_dict.keys() and number_dict[need_number] > i:
        count += 1

print(count)
