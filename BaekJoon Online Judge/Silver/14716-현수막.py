import sys
from collections import deque

VISITED = -1 # 탐색된 좌표
DIRECTION_X = [0, 0, -1, 1, -1, 1, -1, 1] # 상하좌우 대각선 좌표
DIRECTION_Y = [-1, 1, 0, 0, -1, -1, 1, 1]

# 탐색 가능한 영역에 좌표가 존재하는지 확인
def is_valid_coordinate(x, y, col, row):
    if 0 <= x < col and 0 <= y < row:
        return True


# x, y 좌표를 기준으로 너비우선탐색
def bfs(x, y, binary):
    queue = deque()
    queue.append([x, y])
    binary[x][y] = VISITED # 현재 좌표 방문 완료

    col, row = len(binary), len(binary[0])

    while queue:
        current = queue.popleft()
        popped_x, popped_y = current[0], current[1]

        for i in range(8): # 주변 좌표 탐색
            new_x = popped_x + DIRECTION_X[i]
            new_y = popped_y + DIRECTION_Y[i]

            if is_valid_coordinate(new_x, new_y, col, row):
                if binary[new_x][new_y] == 1: # 아직 탐색 안 한 좌표
                    binary[new_x][new_y] = VISITED # 방문처리
                    queue.append([new_x, new_y])

    return binary

# main
if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split()) # 현수막 열, 행
    binary_values = [list(map(int, sys.stdin.readline().split())) for _ in range(M)] # 마스킹이 적용된 이진값
    
    answer = 0

    # 글자 개수 계산
    for i in range(M):
        for j in range(N):
            if binary_values[i][j] == 1: # 글자로 판별되는 부분
                binary_values = bfs(i, j, binary_values)
                answer += 1

    print(answer)