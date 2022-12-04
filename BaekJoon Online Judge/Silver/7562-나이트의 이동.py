import sys
from collections import deque

NOT_VISITED = -1

# 입력 받기
t = int(sys.stdin.readline().rstrip())

answer = []
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

# 탐색 가능한 좌표인지 확인
def isSearchableCoordiante(x, y, len):
    if 0 <= x < len and 0 <= y < len:
        return True


# 체스판의 이동 거리 계산
def getChessboardDistance(x, y, l, board):
    queue = deque([[x, y]])
    dist = 0

    board[x][y] = dist # 현재 위치의 거리는 0

    while queue:
        dist += 1 # 거리 1 증가
        
        for _ in range(len(queue)):
            cur = queue.popleft()

            for k in range(8):
                new_x = cur[0] + dx[k]
                new_y = cur[1] + dy[k]

                if isSearchableCoordiante(new_x, new_y, l):
                    if board[new_x][new_y] == NOT_VISITED:
                        queue.append([new_x, new_y])
                        board[new_x][new_y] = dist
        

# 테스트 케이스만큼 반복
for _ in range(t):
    length = int(sys.stdin.readline().rstrip())
    current_x, current_y = map(int, sys.stdin.readline().split())
    target_x, target_y = map(int, sys.stdin.readline().split())

    chessboard = [[NOT_VISITED] * length for _ in range(length)]

    getChessboardDistance(current_x, current_y, length, chessboard)

    answer.append(chessboard[target_x][target_y])


# 정답 출력
print(*answer, sep='\n')