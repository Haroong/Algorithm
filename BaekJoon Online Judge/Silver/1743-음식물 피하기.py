import sys
sys.setrecursionlimit(100000)

# 쓰레기가 존재함
TRASH_EXIST = 1

# 결과
result, answer = 0, 0

# 지도 정보 입력 받기
n, m, k = map(int, sys.stdin.readline().split())


# 음쓰 좌표 입력 받기
coordinate =  [[0] * m for _ in range(n)]

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    
    coordinate[x-1][y-1] = TRASH_EXIST # 현재 좌표에 쓰레기가 떨어져 있음


# 음쓰 크기 계산
def dfs(x, y):

    # 탐색 가능한 범위를 벗어남
    if x < 0 or y < 0 or x >= n  or y >= m:
        return 

    # 현재 좌표가 아직 미방문한 상태
    if coordinate[x][y] == TRASH_EXIST:
        coordinate[x][y] = 0 # 현재 좌표 방문 완료
        global result # 전역 변수인 result 사용을 위함
        result += 1 # 쓰레기 크기 1 증가시킴

        # 현재 좌표에서 네 방향 탐색
        dfs(x-1, y) # 왼쪽
        dfs(x+1, y) # 오른쪽
        dfs(x, y+1) # 아래쪽
        dfs(x, y-1) # 위쪽

    return result


# 음쓰 크기 계산
for i in range(n):
    for j in range(m):
        if coordinate[i][j] == TRASH_EXIST:
            result = 0
            answer = max(answer, dfs(i, j))

# 정답 출력
print(answer)
