import sys
sys.setrecursionlimit(10**6)

# 색칠된 그림
PAINTED = 1

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
picture = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 결과 변수
count, max_picture, dfs_sum = 0, 0, 0

# dfs
def dfs(x, y):
    # 탐색 가능 범위를 벗어남
    if x < 0 or y < 0 or x >= n or y >= m:
        return

    # 현재 그림을 처음 방문함
    if picture[x][y] == PAINTED:
        picture[x][y] = 0 # 현재 그림 방문 처리
        global dfs_sum
        dfs_sum += 1

        # 현재 그림과 가로, 세로로 연결된 그림 탐색
        dfs(x-1, y) # 왼쪽 그림
        dfs(x+1, y) # 오른쪽 그림
        dfs(x, y-1) # 위쪽 그림
        dfs(x, y+1) # 아래쪽 그림

    return

# 가장 넓은 넓이의 그림 찾기
for i in range(n):
    for j in range(m):
        if picture[i][j] == PAINTED: # 색칠된 그림
            dfs_sum = 0
            dfs(i, j)
            count += 1 # 그림의 개수 1 증가시킴
            max_picture = max(max_picture, dfs_sum)

# 정답 출력
print(count)
print(max_picture)