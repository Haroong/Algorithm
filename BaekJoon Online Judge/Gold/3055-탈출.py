import sys
import copy
from collections import deque

WATER = '*'
DESTINATION = 'D'
START = 'S'
STONE = 'X'
EMPTY = '.'
VISITED = -1

DIRECTION_X = [0, 0, 1, -1]
DIRECTION_Y = [1, -1, 0, 0]

# 이동 가능한 좌표인지 확인
def is_valid_coordinate(x, y, col, row):
    if 0 <= x < row and 0 <= y < col:
        return True

# 다음번에 어느 곳이 물에 잠기는 영역인지 반환
def next_water_waves(water_map, water_hazard, row, col):
    queue = deque(water_hazard)

    while queue:
        cur = queue.popleft()
        x, y = cur[0], cur[1]

        for i in range(4): # 물이 찬 위치에서 상하좌우 탐색
            new_x = x + DIRECTION_X[i]
            new_y = y + DIRECTION_Y[i]

            if is_valid_coordinate(new_x, new_y, col, row):
                if water_map[new_x][new_y] != START and water_map[new_x][new_y] != DESTINATION and water_map[new_x][new_y] != STONE:
                    water_map[new_x][new_y] = WATER

    return water_map

# 고슴도치 이동!!
def move_to_safe_area(water_map, escape_area, row, col):
    queue = deque(escape_area)
    is_destination = False # 도착 좌표 발견 여부
    is_escapable = False # 다른 영역으로 탈출 가능 여부

    while queue:
        cur = queue.popleft()
        x, y = cur[0], cur[1]
        
        for i in range(4):
            new_x = x + DIRECTION_X[i]
            new_y = y + DIRECTION_Y[i]

            if is_valid_coordinate(new_x, new_y, col, row):
                if water_map[new_x][new_y] == DESTINATION: # 비버의 굴 발견
                    is_destination = True
                    break
                
                if water_map[new_x][new_y] == EMPTY:
                    water_map[new_x][new_y] = START # 다음 타임에 탐색할 좌표 표시
                    is_escapable = True

    return is_destination, is_escapable


# 고슴도치가 비버 굴까지 이동가능한 최소 시간 계산
def count_minimum_exit_time(wood_map, row, col):
    time = 0 # 소요 시간
    water_map = copy.deepcopy(wood_map) # 새롭게 그려지는 지도

    while True:
        time += 1

        # 현재 숲의 상태를 각 리스트에 저장한다
        water_hazard, escape_area = [], []
        for i in range(row):
            for j in range(col):
                if water_map[i][j] == WATER:
                    water_hazard.append([i, j])
                elif water_map[i][j] == START:
                    escape_area.append([i, j])
                    water_map[i][j] = VISITED # 이제 이 좌표 방문 안 함
        
        water_map = next_water_waves(water_map, water_hazard, row, col) # 물에 잠기는 영역 체크
        res = move_to_safe_area(water_map, escape_area, row, col) # 이동 가능한 위치 탐색
        
        is_destination, is_escapable = res[0], res[1]
        if is_destination:
            break
        elif not is_escapable: # 탈출 불가능
            time = -1
            break

    return time

# 정답 출력 형식
def print_answer(time):
    if time == -1:
        print('KAKTUS')
    else:
        print(time)

# main
if __name__ == '__main__':
    R, C = map(int, sys.stdin.readline().split()) # 숲의 지도 크기
    wood_map = [list(sys.stdin.readline().rstrip()) for _ in range(R)] # 숲의 초기 상태
    time = count_minimum_exit_time(wood_map, R, C)
    print_answer(time)