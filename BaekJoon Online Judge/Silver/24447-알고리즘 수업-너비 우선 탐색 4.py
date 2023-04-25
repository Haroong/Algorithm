import sys
from collections import deque

# 연결 그래프 생성
def draw_graph(nodes, edges):
    result = [[] for _ in range(nodes + 1)]

    for x, y in edges:
        result[x].append(y)
        result[y].append(x)
    
    return result

# bfs 탐색 결과를 반환한다
def bfs(nodes, start, edges):
    graph = draw_graph(nodes, edges)
    queue = deque()
    visited = set([start])
    queue.append(start) # 탐색 시작 노드
    result = [0] * nodes
    result[start -1] = 0 # 시작 노드의 깊이는 0
    depth = 0
    count = 1 # 방문 순서
    
    while queue:
        depth += 1
        loop = len(queue)

        for _ in range(loop):
            current = queue.popleft()
            for node in sorted(graph[current], reverse=True): # 현재 노드와 연결된 다른 노드 탐색
                if node not in visited:
                    queue.append(node)
                    visited.add(node)
                    count += 1
                    result[node -1] = depth * count # 현재 노드의 깊이*방문 순서

    return sum(result)

if __name__ == '__main__':
    N, M, R = map(int, sys.stdin.readline().split()) # 정점의 수, 간선의 수, 시작 정점

    edges = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(M)]) # 간선 정보
    answer = bfs(N, R, edges)
    print(answer)