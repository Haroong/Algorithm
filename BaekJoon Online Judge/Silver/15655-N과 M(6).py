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
        back_tracking(i+1) # 현재 인덱스보다 큰 인덱스의 값만 수열에 추가
        result.pop()


back_tracking(0)