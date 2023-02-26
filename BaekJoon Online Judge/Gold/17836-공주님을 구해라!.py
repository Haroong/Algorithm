import sys
from collections import deque

EMPTY = 0
WALL = 1
SWORD = 2
VISITED = -1
MAX_TIME = 10000

DIRECTION_X = [0, 0, 1, -1]
DIRECTION_Y = [1, -1, 0, 0]


# 탐색 가능한 좌표인지 확인
def is_valid_coordinate(x, y, row, col):
    if 0 <= x < row and 0 <= y < col:
        return True
    else:
        return False

# 용사의 위치에서 공주가 있는 위치까지의 거리 반환
def calculate_direct_distance(x, y, col, row):
    dist = (col - x) + (row - y)
    return dist


# 공주 구출에 성공했는지 여부 반환
def is_rescue_success(is_found):
    if is_found:
        return True
    else:
        return False
    

# 공주를 구출할 수 있는 최단 시간 반환
def get_minimum_rescue_time(castle, limit):
    queue = deque([[0, 0]]) # 용사의 시작 위치
    time_not_using_sword = 0
    time_using_sword = MAX_TIME

    castle[0][0] = VISITED
    row, col = len(castle), len(castle[0])
    
    while queue:
        time_not_using_sword += 1 # 구출 시간 1 증가
        if time_not_using_sword > limit: # 제한 시간 종료
            break

        for _ in range(len(queue)):
            popped = queue.popleft()
            x, y = popped[0], popped[1]

            for i in range(4): # 용사의 현재 위치에서 이동 가능한 좌표 탐색
                new_x = x + DIRECTION_X[i]
                new_y = y + DIRECTION_Y[i]
                
                if is_valid_coordinate(new_x, new_y, row, col):
                    if castle[new_x][new_y] == SWORD: # 전설의 검 발견
                        dist = calculate_direct_distance(new_x, new_y, col - 1, row - 1)
                        sword_time = dist + time_not_using_sword

                        if sword_time <= limit:
                            time_using_sword = sword_time
                            castle[new_x][new_y] = VISITED
                    else:
                        if new_x == row - 1 and new_y == col - 1: # 공주 발견
                            time = min(time_not_using_sword, time_using_sword)
                            return time
                        if castle[new_x][new_y] == EMPTY and castle[new_x][new_y] != VISITED: # 이동 가능
                            queue.append([new_x, new_y])
                            castle[new_x][new_y] = VISITED

    # 공주 구출 실패 
    if time_using_sword != MAX_TIME:
        time = time_using_sword
    else:
        time = -1

    return time

# 정답 형식 출력
def print_answer(time):
    if time == -1:
        print('Fail')
    else:
        print(time)

# main
if __name__ == '__main__':
    N, M, T = map(int, sys.stdin.readline().split()) # 성의 크기(N x M), 제한 시간
    magic_castle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 성의 구조
    result = get_minimum_rescue_time(magic_castle, T)
    print_answer(result)