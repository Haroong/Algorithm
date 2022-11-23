import sys
from collections import  deque

NOT_VISITED = -1

# 입력 받기
n, m, k, x = map(int, sys.stdin.readline().split())

# 그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b) # a도시에서 b도시로 이동하는 단방향 그래프

distance = [NOT_VISITED] * (n+1) # 각 도시에 대한 최단 거리 초기화
distance[x] = 0 # 출발 도시의 거리

queue = deque([x]) # x도시에서 출발

# bfs
while queue:
    current_city = queue.popleft()

    for city in graph[current_city]: # 현재 도시와 연결된 다른 도시 탐색
        if distance[city] == NOT_VISITED: # 아직 방문 안 한 도시
            distance[city] = distance[current_city] + 1 # 현재 도시의 거리로부터 거리 1증가
            queue.append(city)

# 최단 거리가 k인 도시 찾기
answer = []
for i in range(1, n+1):
    if distance[i] == k:
        answer.append(i)

# 정답 출력
if not answer:
    print(-1)
else:
    print(*sorted(answer), sep='\n')