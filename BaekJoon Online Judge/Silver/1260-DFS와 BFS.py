import sys
from collections import  deque

# 입력 받기
n, m, v = map(int, sys.stdin.readline().split())

# 연결 그래프
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 가능한 정점이 여러개인 경우, 번호가 작은 순으로 탐색하기 위함
for g in graph:
    g.sort()

# 탐색 결과
dfs_result, bfs_result = [], []

# DFS
def dfs(v):
    dfs_result.append(v) # 현재 노드 탐색 완료

    for g in graph[v]:
        if g not in dfs_result:
            dfs(g)

    return dfs_result

# BFS
def bfs(v):
    bfs_result.append(v) # 현재 노드 탐색 완료
    queue = deque(graph[v])

    while queue:
        c = queue.popleft()
        bfs_result.append(c)  # 현재 노드 탐색 완료

        for g in graph[c]: # 현재 노드와 연결된 다른 노드를 큐에 삽입
            if g not in queue and g not in bfs_result:
                queue.append(g)

# 그래프 탐색
dfs(v)
bfs(v)

# 정답 출력
print(*dfs_result, sep=' ')
print(*bfs_result, sep=' ')