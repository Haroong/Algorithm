import sys
from collections import deque

def is_valid_coordinate(x, y, row, col):
    if 0 <= x < row and 0 <= y < col:
        return True
    else:
        return False


def can_percolate_or_not(figure, start):
    queue = deque([[0, start]])
    result = False

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        current = queue.popleft()

        for i in range(4): # 현재 좌표에서 상하좌우 탐색
            nx = dx[i] + current[0]
            ny = dy[i] + current[1]

            if is_valid_coordinate(nx, ny, len(figure), len(figure[0])):
                if figure[nx][ny] == WHITE: # 침투 가능한 영역
                    if nx == len(figure) - 1: # 안쪽 영역까지 침투 가능(가장 마지막 줄)
                        result = True
                        break

                    figure[nx][ny] = VISITED
                    queue.append([nx, ny])

    return result


if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split()) # 격자의 크기
    figure = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(M)] # 격자의 형태

    WHITE = 0
    VISITED = -1
    answer = 'NO'

    for i in range(N): # 바깥 영역(맨 윗줄)에서 탐색 시작
        if figure[0][i] == WHITE:
            figure[0][i] = VISITED
            if can_percolate_or_not(figure, i):
                answer = 'YES'
                break

    print(answer)