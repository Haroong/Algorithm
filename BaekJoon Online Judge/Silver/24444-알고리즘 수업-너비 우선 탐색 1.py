import sys
from collections import deque

# 연결 그래프 생성
def draw_graph(nodes, edges):
    result = [[] for _ in range(nodes + 1)]

    for x, y in edges:
        result[x].append(y)
        result[y].append(x)
    
    return result

# 시작 정점에서 탐색 불가능한 좌표가 있는지 확인
def is_non_reachable_node_exists(bfs_order):
    for index, value in enumerate(bfs_order):
        if value == -1:
            bfs_order[index] = 0 

    return bfs_order


# bfs 탐색 결과를 반환한다
def bfs_order(nodes, start, edges):
    graph = draw_graph(nodes, edges)
    queue = deque()
    visited = set([start])
    queue.append(start) # 탐색 시작 노드
    result = [-1] * nodes
    result[start -1] = 1
    order = 1
    
    while queue:
        current = queue.popleft()
        for node in sorted(graph[current]): # 현재 노드와 연결된 다른 노드 탐색
            if node not in visited:
                queue.append(node)
                visited.add(node)
                order += 1
                result[node -1] = order # 현재 노드의 방문 순서

    is_non_reachable_node_exists(result)

    return result

if __name__ == '__main__':
    N, M, R = map(int, sys.stdin.readline().split()) # 정점의 수, 간선의 수, 시작 정점
    edges = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(M)]) # 간선 정보
    answer = bfs_order(N, R, edges)
    print(*answer, sep='\n')