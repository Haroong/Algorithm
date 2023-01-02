import sys

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

result = []

# back tracking
def back_tracking(elements, depth):
    if depth == M:
        print(*result, sep=' ')
        return

    for index, value in enumerate(elements):
        if not result or result[0] != value and value not in result: # 자기 자신 제외, 중복 제외
            result.append(value)
            back_tracking(elements, depth+1)
            result.pop()

back_tracking(numbers, 0)