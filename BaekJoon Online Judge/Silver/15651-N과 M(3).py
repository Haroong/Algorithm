import sys

# 입력 받기
N, M = map(int, sys.stdin.readline().split())

result = []

# backtracking
def back_tracking():
    if len(result) == M: # 길이가 M인 수열 완성
        print(*result, sep=' ')
        return

    for i in range(1, N+1): # 1부터 N까지 탐색
        result.append(i)
        back_tracking()
        result.pop()


back_tracking()