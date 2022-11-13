import sys

sys.setrecursionlimit(100000)

# 배추가 존재함
CABBAGE_EXIST = 1

# 정답
answer = []

# 테스트 케이스
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    # 배추밭 정보 입력 받기
    n, m, k = map(int, sys.stdin.readline().split())

    # 필요한 벌레 마리 수
    bugs = 0

    # 배추 좌표 입력 받기
    coordinate = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        coordinate[x][y] = CABBAGE_EXIST  # 현재 좌표에 배추가 있음


    # 필요한 벌레 수 계산
    def dfs(x, y):
        # 탐색 가능한 범위를 벗어남
        if x < 0 or y < 0 or x >= n or y >= m:
            return

        # 현재 좌표가 아직 미방문 상태
        if coordinate[x][y] == CABBAGE_EXIST:
            coordinate[x][y] = 0  # 현재 좌표 방문 완료

            # 현재 좌표에서 네 방향 탐색
            dfs(x - 1, y)  # 왼쪽
            dfs(x + 1, y)  # 오른쪽
            dfs(x, y + 1)  # 아래쪽
            dfs(x, y - 1)  # 위쪽

        return


    # 배추흰지렁이 마리 수 계산
    for i in range(n):
        for j in range(m):
            if coordinate[i][j] == CABBAGE_EXIST:
                dfs(i, j)
                bugs += 1
                

    # 현재 테스트 케이스에 대한 결과
    answer.append(bugs)

# 정답 출력
print(*answer, sep='\n')
