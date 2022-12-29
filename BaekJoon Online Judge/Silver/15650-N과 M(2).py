import sys

# 입력 받기
N, M = map(int, sys.stdin.readline().split())

# 결과
result = []

# back tracking
def back_tracking():
    if len(result) == M: # 길이가 M인 수열 생성 완료
        print(*result, sep=' ')
        return
        
    for i in range(1, N+1): # 1부터 N+1까지 탐색
        if not result or i not in result and i > result[-1]: # 빈 수열이거나 현재 원소가 수열의 맨 마지막 원소보다 큼
            result.append(i)
            back_tracking()
            result.pop() # 마지막에 추가한 숫자 제거

back_tracking()