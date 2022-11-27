import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

# 필요 변수
answer = 0
visited = []

# 그래프 연결 관계 생성
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 그래프의 연결 요소 찾기
def dfs(x):
    visited.append(x) # 현재 정점 탐색 완료

    for g in graph[x]: # 현재 정점과 연결된 다른 정점 탐색
        if g not in visited:
            dfs(g)

    return

# 모든 정점에 대해 dfs 탐색
for i in range(1, n+1):
    if i not in visited:
        dfs(i)
        answer += 1

# 정답 출력
print(answer)