import sys

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

# 수열
result = []

# back tracking
def back_tracking(index):
    if len(result) == M:
        print(*result, sep=' ')
        return

    for i in range(index, N):
        result.append(numbers[i])
        back_tracking(i)
        result.pop()


back_tracking(0)