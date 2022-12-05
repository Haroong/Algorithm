import sys
import copy
from collections import deque

FLOODING = -1
VISITED = -2

# 입력 받기
n = int(sys.stdin.readline().rstrip())

heights = set() # 높이 값 집합
villeage = [] # 지역의 모든 영역의 높이 값
safety_area = []

heights.add(1) # 초기 높이 1 추가


# 각 지역에 대한 높이값
for _ in range(n):
    inp = list(map(int, sys.stdin.readline().split()))
    villeage.append(inp)
    heights.update(set(inp))

heights = list(heights) # 리스트로 변환

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def isFloodingArea(h):
    if h <= n:
        True

        
def isValidCoordinate(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True


def bfs(x, y, area):
    queue = deque()
    queue.append([x, y])
    area[x][y] = VISITED

    while queue:
        current = queue.popleft()

        for k in range(4): # 위, 아래, 왼쪽, 오른쪽 탐색
            new_x = current[0] + dx[k]
            new_y = current[1] + dy[k]

            if not isValidCoordinate(new_x, new_y):
                continue

            if area[new_x][new_y] != VISITED and area[new_x][new_y] != FLOODING:
                queue.append([new_x, new_y])
                area[new_x][new_y] = VISITED # 현재 지역 방문 완료


if len(heights) == 1: # 한 개의 높이만 존재
    print(1)
else:
    # n * n 영역 탐색
    for height in heights:
        count = 0 # 현재 높이에 대한 안전 구역 개수
        temp_area = copy.deepcopy(villeage)

        # 현재 높이보다 같거나 낮은 지역 체크
        for i in range(n):
            for j in range(n):
                if temp_area[i][j] <= height:
                    temp_area[i][j] = FLOODING

        # 안전 영역 찾기
        for i in range(n):
            for j in range(n):
                if temp_area[i][j] != FLOODING and temp_area[i][j] != VISITED:
                    bfs(i, j, temp_area)
                    count += 1

        safety_area.append(count)


    # 정답 출력
    print(max(safety_area))