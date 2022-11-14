import sys

# 입력 받기
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

houses, house = [], 0  # 특정 단지에 속하는 집 개수
apartment = 0  # 아파트 총 단지 수

# 아파트 단지 번호 붙이기
def dfs(x, y):
    # 지도 범위를 벗어남
    if x < 0 or y < 0 or x >= n or y >= n:
        return

    # 아직 방문하지 않은 집
    if graph[x][y] == 1:
        graph[x][y] = 0 # 현재 집 방문 완료
        global house
        house += 1 # 해당 단지에 속하는 집

        # 현재 집을 기준으로 상하좌우 탐색
        dfs(x-1, y) # 왼쪽 집
        dfs(x+1, y) # 오른쪽 집
        dfs(x, y+1) # 아랫집
        dfs(x, y-1) # 윗집

    return


# 지도 탐색
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house = 0
            dfs(i, j) # 아파트 단지 탐색
            apartment += 1 # 단지 수 1 증가
            houses.append(house)

# 정답 출력
print(apartment)
print(*sorted(houses), sep='\n') # 오름차순으로 출력