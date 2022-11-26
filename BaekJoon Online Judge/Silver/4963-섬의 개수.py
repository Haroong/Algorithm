import sys

LAND = 1
VISITED = -1

# 가로, 세로, 대각선 좌표
dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0,0, 1, -1, -1, 1, -1, 1]

# 섬의 개수
count = 0
answer = []

def dfs(x, y):
    graph[x][y] = VISITED # 현재 칸 탐색 완료

    # 현재 칸에서 가로, 세로, 대각선으로 연결된 다른 칸 탐색
    for d in range(8):
        new_x = x + dx[d]
        new_y = y + dy[d]

        # 탐색 불가능한 좌표
        if new_x < 0 or new_y < 0 or new_x == h or new_y == w:
            continue

        # 연결된 땅 발견
        if graph[new_x][new_y] == LAND:
            dfs(new_x, new_y)

    return

# 각각의 테스트 케이스
while True:
    # 입력 받기
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0: # 입력 종료
        break

    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

    # 섬의 개수 초기화
    count = 0

    # 한 칸 지도
    if w == 1 and h == 1:
        if graph[0][0] == LAND:
            count = 1
    else:
        # 현재 지도 상의 섬의 개수 탐색
        for i in range(h):
            for j in range(w):
                if graph[i][j] == LAND:
                    dfs(i, j)
                    count += 1

    answer.append(count)

# 정답 출력
print(*answer, sep='\n')