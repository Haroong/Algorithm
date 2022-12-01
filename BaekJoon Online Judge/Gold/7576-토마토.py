import sys
from collections import deque

RIPEN = 1 # 익은 토마토
NOT_RIPEN = 0 # 덜익은 토마토

box = list() # 토마토 박스
queue = deque()

days = 0 # 경과된 날짜
all_ripen = False

# 입력 받기
row, col = map(int, sys.stdin.readline().split())
for c in range(col):
    tomatoes = list(map(int, sys.stdin.readline().split()))
    
    for index, value in enumerate(tomatoes):
        if value == RIPEN: # 익은 토마토의 위치를 큐에 삽입
            queue.append([c, index])
    
    box.append(tomatoes) # 박스에 토마토 한 줄 넣기

    
# 왼쪽, 오른쪽, 앞, 뒤에 위치한 토마토 좌표
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


# bfs
def searchNearbyTomatoes(x, y):
    # 현재 토마토와 인접한 다른 위치의 토마토 탐색
    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]

        # 탐색 불가능한 좌표
        if new_x < 0 or new_y < 0 or new_x >= col or new_y >= row:
            continue

        # 덜익은 토마토
        if box[new_x][new_y] == NOT_RIPEN:
            box[new_x][new_y] = RIPEN
            queue.append([new_x, new_y])

            
# 상자에 든 모든 토마토 상태 판별
def checkTomatoesCondition():
    if all(NOT_RIPEN not in tomatoes for tomatoes in box): # 덜 익은 토마토가 없음
        global all_ripen
        all_ripen = True

        print(days)

        return all_ripen

        
# 완숙 일자 찾기 
while queue:
    if checkTomatoesCondition():
        break

    day_queue = len(queue) # 하루에 익을 수 있는 모든 토마토

    for _ in range(day_queue): 
        position = queue.popleft()
        searchNearbyTomatoes(position[0], position[1])

    days += 1 # 하루 경과


# 모든 토마토가 익을 수 없음
if not all_ripen:
    print(-1)