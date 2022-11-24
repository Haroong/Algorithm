import sys
from collections import deque

WALL = 0 # 벽
VISITED = True # 방문한 칸

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

# 모든 칸에 미방문으로 표시
check_visit = [[False for _ in range(m)] for _ in range(n)]

# 큐
queue = deque([[0, 0]]) # 시작 위치 삽입
check_visit[0][0] = VISITED

# 탐색 위치
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 시작 위치에서 도착 위치까지 탐색
while queue:
    current = queue.popleft()

    for i in range(4): # 현재 위치에서 이동 가능한 칸 탐색
        x = current[0] + dx[i]
        y = current[1] + dy[i]

        if x < 0 or y < 0 or x == n or y == m: # 탐색 가능한 범위를 벗어남
            continue

        if maze[x][y] != WALL and check_visit[x][y] != VISITED:
            maze[x][y] = maze[current[0]][current[1]] + 1 # 거리 1 증가
            check_visit[x][y] = VISITED # 방문 완료     
            queue.append([x, y])       


# 정답 출력
print(maze[n-1][m-1])