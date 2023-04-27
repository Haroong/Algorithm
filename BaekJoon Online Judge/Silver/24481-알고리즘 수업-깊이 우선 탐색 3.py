import sys
sys.setrecursionlimit(100000)


def set_graph(total, edges):
    result = [[] for _ in range(total+1)]

    for a, b in edges:
        result[a].append(b)
        result[b].append(a)

    return result

def dfs(graph, visited, start, dfs_order, depth):
    depth += 1 # 노드의 깊이

    for node in graph[start]:
        if node not in visited:
            visited.add(node) # 현재 노드 방문 처리
            dfs_order[node - 1] = depth
            dfs(graph, visited, node, dfs_order, depth)

    return dfs_order

def get_traversal_order(total, start, edges):
    depth = 0
    order = [-1] * total
    order[start - 1] = depth # 시작 노드의 깊이는 0
    graph = set_graph(total, edges) # 연결 그래프 생성

    visited = set()
    visited.add(start) # 시작 노드 방문 처리

    result = dfs(graph, visited, start, order, depth)
    
    return result

if __name__ == '__main__':
    N, M, R = map(int, sys.stdin.readline().split()) # 노드의 수, 간선의 수, 시작 노드
    edges = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(M)]) # 간선 정보
    answer = get_traversal_order(N, R, edges)
    print(*answer, sep='\n')