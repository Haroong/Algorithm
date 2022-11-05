import sys

# 입력 받기
n = int(sys.stdin.readline().rstrip()) # 컴퓨터의 수
pair = int(sys.stdin.readline()) # 네트워크 상에 연결된 컴퓨터 쌍의 수
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(pair)] # 서로 연결된 컴퓨터 번호

# 연결 그래프 생성
graph = [[] for _ in range(n+1)]
for a, b in numbers:
    graph[a].append(b)
    graph[b].append(a)

# 1번 컴퓨터와 연결된 다른 컴퓨터 정보
answer = []

# 특정 번호의 컴퓨터와 연결된 컴퓨터 찾기
def dfs(v):
    answer.append(v) # 현재 컴퓨터는 1번 컴퓨터와 연결된 상태

    for g in graph[v]: # v 노드와 연결된 컴퓨터 탐색
        if g not in answer:
            dfs(g)

    return answer

dfs(1) # 1번 컴퓨터와 연결된 모든 컴퓨터 탐색

print(len(answer) - 1) # 1번 컴퓨터를 제외한 개수
