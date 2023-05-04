import sys
sys.setrecursionlimit(10**5)


def set_graph(total, edges):
    result = [[] for _ in range(total+1)]

    for a, b in edges:
        result[a].append(b)
        result[b].append(a)

    return result

def dfs(graph, visited, start, result, depth):
    depth += 1 # 노드의 깊이

    for node in graph[start]:
        if node not in visited:
            visited.add(node) # 현재 노드 방문 처리
            result[node - 1] = depth * len(visited)
            dfs(graph, visited, node, result, depth)

    return result

def multiply_of_depth_and_traversal_order(total, start, edges):
    depth = 0 # 노드의 탐색 깊이
    result = [0] * total

    visited = set()
    visited.add(start) # 시작 노드 방문 처리

    graph = set_graph(total, edges) # 연결 그래프 생성
    dfs_result = dfs(graph, visited, start, result, depth)
    result = sum(dfs_result)
    
    return result

if __name__ == '__main__':
    N, M, R = map(int, sys.stdin.readline().split()) # 노드의 수, 간선의 수, 시작 노드
    edges = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(M)], reverse=True) # 간선 정보
    answer = multiply_of_depth_and_traversal_order(N, R, edges)
    print(answer)