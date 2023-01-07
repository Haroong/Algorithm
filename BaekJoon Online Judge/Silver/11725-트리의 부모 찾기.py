import sys

sys.setrecursionlimit(10**5)

INITIAL_STATE = -1

N = int(sys.stdin.readline().rstrip()) # 노드의 개수
graph = [[] for _ in range(N+1)] # 그래프 정보

answer = [INITIAL_STATE for _ in range(N)] # 각 노드의 부모 노드 정보

# 그래프 연결 관계 생성
def set_graph(N, graph):
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split()) # 트리 상에서 연결된 두 정점
        graph[a].append(b)
        graph[b].append(a)


# 각 노드의 부모 노드 탐색
def dfs(node):
    for v in graph[node]: # 현재 노드와 연결된 자식 노드 개수만큼
        if answer[v-1] == INITIAL_STATE: # 아직 방문 안 함
            answer[v-1] = node
            dfs(v)

    return
    
    
set_graph(N, graph)
dfs(1) # 탐색 시작
print(*answer[1:], sep='\n') # 루트 노드 제외