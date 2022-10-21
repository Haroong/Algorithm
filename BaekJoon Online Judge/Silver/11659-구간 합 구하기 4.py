import sys
import pprint

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
scope = [list(map(int, sys.stdin.readline().split())) for _ in range(int(m))]

accumulatation = [numbers[0]]

# 누적합 계산
for index, value in enumerate(numbers[1:], 1):
    total_sum = accumulatation[index-1] + value
    accumulatation.append(total_sum)

# 구간합 계산
for a, b in scope:
    if a == 1:
        result = accumulatation[b-1]
    else:
        result = accumulatation[b-1] - accumulatation[a-2]

    print(result)
