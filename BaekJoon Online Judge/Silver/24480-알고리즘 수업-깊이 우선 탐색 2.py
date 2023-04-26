import sys
sys.setrecursionlimit(100000)


def set_graph(total, edges):
    result = [[] for _ in range(total+1)]

    for a, b in edges:
        result[a].append(b)
        result[b].append(a)

    return result

def dfs(graph, visited, start, dfs_order):
    for node in graph[start]:
        if node not in visited:
            global count
            count += 1
            visited.add(node) # 현재 노드 방문 처리
            dfs_order[node - 1] = count
            dfs(graph, visited, node, dfs_order)

    return dfs_order

def get_traversal_order(total, start, edges):
    order = [0] * total
    order[start - 1] = count # 시작 정점은 첫번째로 방문

    graph = set_graph(total, edges) # 연결 그래프 생성

    visited = set()
    visited.add(start) # 시작 노드 방문 처리

    result = dfs(graph, visited, start, order)
    
    return result

if __name__ == '__main__':
    N, M, R = map(int, sys.stdin.readline().split()) # 정점의 수, 간선의 수, 시작 정점
    edges = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(M)], reverse=True) # 간선 정보
    count = 1
    answer = get_traversal_order(N, R, edges)
    print(*answer, sep='\n')