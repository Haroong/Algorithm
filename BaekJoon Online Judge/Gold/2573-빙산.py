import sys
import copy
from collections import deque

WATER = 0
VISITED = -1

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
arctic = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 탐색 방향 위치
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 바다
pure_ocean = [[WATER] * m for _ in range(n)]

# 탐색 가능한 좌표인지 확인
def is_valid_coordinate(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True


# 다음 해의 빙하 높이 계산
def next_year_height(coord, x, y, melting):
    h = coord[x][y] - melting

    if h < WATER: # 음수는 0으로 변경
        h = WATER

    return h


# 빙산의 개수 계산
def is_one_iceberg():
    iceberg_cnt = 0

    for i in range(n):
        for j in range(m):
            if iceberg_cnt > 1:
                return False

            if arctic[i][j] != WATER:
                iceberg_cnt += 1

    if iceberg_cnt == 1:
        return True

# bfs
def bfs(ocean, visit, x, y):
    next_year_arctic = copy.deepcopy(ocean) # 내년의 북극 상태
    
    queue = deque()
    queue.append([x, y])
    visit[x][y] = VISITED

    while queue:
        current_iceberg = queue.popleft()
        decrease_height = 0

        for k in range(4): # 빙하와 인접한 네 방향 탐색
            nx = current_iceberg[0] + dx[k]
            ny = current_iceberg[1] + dy[k]

            if is_valid_coordinate(nx, ny):

                if ocean[nx][ny] != WATER and visit[nx][ny] != VISITED: # 방문 안 한 빙하
                    queue.append([nx, ny]) # 현재 빙하와 붙어있는 빙하
                    visit[nx][ny] = VISITED

                if ocean[nx][ny] == WATER: # 바다
                    decrease_height += 1
        
        height = next_year_height(ocean, current_iceberg[0], current_iceberg[1], decrease_height)
        next_year_arctic[current_iceberg[0]][current_iceberg[1]] = height

    return next_year_arctic


# 빙산이 분리되는 최초의 시간
year = 0

if is_one_iceberg(): # 하나의 빙산만 존재
    print(year)
else:
    while True:
        bfs_cnt = 0 # bfs 반복 횟수

        this_year_arctic = copy.deepcopy(arctic) # 올해의 북극 상태
        visited_state = copy.deepcopy(arctic) # 좌표 방문 상태

        for i in range(n):
            for j in range(m):
                if bfs_cnt > 1:  # bfs가 두 번 이상 실행되면 빙산이 분리된 상태
                    break

                if this_year_arctic[i][j] != WATER and visited_state[i][j] != VISITED: # 빙하이면서 아직 방문 안 한 좌표
                    next_year_arctic = bfs(this_year_arctic, visited_state, i, j)
                    arctic = next_year_arctic
                    bfs_cnt += 1
                    

        if bfs_cnt > 1: # 빙산이 분리됨
            break

        if arctic == pure_ocean: # 모든 빙산이 다 녹을 때까지 빙산 분리가 일어나지 않음
            year = 0
            break    

        year += 1

    print(year)