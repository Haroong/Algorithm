import sys
sys.setrecursionlimit(10**5)

def is_valid_coordinate(x, y, row, col):
    if 0 <= x < row and 0 <= y < col:
        return True
    else:
        return False


def count_animals_inside_fence(x, y, row, col, frontyard):
    global sheep, wolf

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4): # 네 방향 탐색
        new_x = x + dx[i]
        new_y = y + dy[i]

        if is_valid_coordinate(new_x, new_y, row, col) and frontyard[new_x][new_y] != VISITED and frontyard[new_x][new_y] != FENCE:
            if frontyard[new_x][new_y] == SHEEP:
                sheep += 1
            elif frontyard[new_x][new_y] == WOLF:
                wolf += 1

            frontyard[new_x][new_y] = VISITED # 현재 좌표 방문처리
            count_animals_inside_fence(new_x, new_y, row, col, frontyard)

    return

def calculate_total_sheep(sheep, wolf):
    result = 0

    if sheep > wolf:
        result += sheep
    
    return result


def calculate_total_wolf(sheep, wolf):
    result = 0

    if wolf >= sheep:
        result += wolf
    
    return result


if __name__ == '__main__':
    R, C = map(int, sys.stdin.readline().split()) # 마당의 행, 열
    frontyard = [list(sys.stdin.readline().rstrip()) for _ in range(R)] # 마당의 초기 상태
    
    VISITED = -1
    FENCE = '#'
    SHEEP = 'o'
    WOLF = 'v'
    sheep, wolf = 0, 0
    answer_s, answer_w = 0, 0

    for i in range(R):
        for j in range(C):
            if frontyard[i][j] != FENCE and frontyard[i][j] != VISITED:
                if frontyard[i][j] == SHEEP:
                    sheep += 1
                elif frontyard[i][j] == WOLF:
                    wolf += 1

                frontyard[i][j] = VISITED # 현재 좌표 방문처리
                count_animals_inside_fence(i, j, R, C, frontyard)

                answer_s += calculate_total_sheep(sheep, wolf)
                answer_w += calculate_total_wolf(sheep, wolf)

                sheep, wolf = 0, 0 # 초기화
    
    print(answer_s, answer_w)