import sys
from collections import deque

NOT_VISITED = -1 # 방문 안 함

# 데스나이트가 이동가능한 좌표
DIRECTION_X = [-2, -2, 0, 0, 2, 2]
DIRECTION_Y = [-1, 1, -2, 2, -1, 1]

# 체스판 생성
def set_chess_board(size):
    return [[NOT_VISITED]*size for _ in range(size)]

# 이동 가능한 좌표인지 확인
def is_valid_coordinate(x, y, board_size):
    if 0 <= x < board_size and 0 <= y < board_size:
        return True
    
# 목표 좌표까지 최소한의 이동 횟수 계산
def count_minimum_move(start_x, start_y, target_x, target_y, board_size):
    board = set_chess_board(board_size)
    count = 0
    queue = deque([[start_x, start_y]])
    board[start_x][start_y] = 0

    while queue:
        count += 1 # 현재 좌표에서 이동 횟수 1 증가
        for _ in range(len(queue)):
            current = queue.popleft()
            x, y = current[0], current[1]
            
            for i in range(6): # 현재 좌표 주변 탐색
                new_x = x + DIRECTION_X[i]
                new_y = y + DIRECTION_Y[i]

                if is_valid_coordinate(new_x, new_y, board_size):
                    if board[new_x][new_y] == NOT_VISITED:
                        if new_x == target_x and new_y == target_y: # 목표 좌표 도달
                            return count
                        else:
                            board[new_x][new_y] = count
                            queue.append([new_x,new_y])

    return NOT_VISITED



if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 체스판의 크기
    start_x, start_y, target_x, target_y = map(int, sys.stdin.readline().split()) # 시작 위치, 목표 위치
    answer = count_minimum_move(start_x, start_y, target_x, target_y, N)
    print(answer)