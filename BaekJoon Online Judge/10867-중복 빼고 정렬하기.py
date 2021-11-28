# get input
n = int(input())
number = list(map(int, input().split()))

# remove duplicate
number_set = list(set(number))
number_set.sort()

# print answer
print(*number_set)
