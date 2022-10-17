import sys

n = sys.stdin.readline().rstrip()
criteria = sorted(list(map(int, sys.stdin.readline().split())))
m = sys.stdin.readline().rstrip()
numbers = list(map(int, sys.stdin.readline().split()))

# check if number exists
for n in numbers:
    if n in criteria:
        print('1')
    else:
        print('0')