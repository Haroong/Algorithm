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
        if i not in result:
            result.append(i)
            back_tracking()
            result.pop() # 마지막에 추가한 숫자 제거

back_tracking()