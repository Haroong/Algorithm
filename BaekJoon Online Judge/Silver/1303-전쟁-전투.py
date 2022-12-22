import sys
from collections import deque

CHECKED = -1

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
warriors = [list(sys.stdin.readline().rstrip()) for _ in range(m)]

# 변수 설정
team_blue, team_white = 0, 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0] * n  for _ in range(m)] # 0으로 초기화

# bfs
def bfs(x, y, visit_info):
    queue = deque()
    queue.append([x, y])
    count = 1 # 인원 수

    team_color = warriors[x][y] # 현재 팀 정보

    while queue:
        current = queue.popleft()

        for k in range(4): # 현재 좌표에서 상하좌우 탐색
            new_x = current[0] + dx[k]
            new_y = current[1] + dy[k]

            if not is_valid_coordinate(new_x, new_y):
                continue

            if warriors[new_x][new_y] == team_color and visit_info[new_x][new_y] != CHECKED:
                queue.append([new_x, new_y])
                visit_info[new_x][new_y] = CHECKED # 현재 노드 방문 완료
                count += 1 # 병사 인원 1 증가

    return count


# 팀의 파워 계산
def calculate_power(num):
    return num**2


# 탐색 가능한 좌표인지 확인
def is_valid_coordinate(x, y):
    if 0 <= x < m and 0 <= y < n:
        return True


# 전체 리스트 탐색
for i in range(m):
    for j in range(n):
        if visited[i][j] != CHECKED:
            visited[i][j] = CHECKED # 현재 좌표 방문 완료
            temp_sum = bfs(i, j, visited)

            if warriors[i][j] == 'W':
                team_white += calculate_power(temp_sum)
            else:
                team_blue += calculate_power(temp_sum)    


# 정답 출력
print(team_white, team_blue)