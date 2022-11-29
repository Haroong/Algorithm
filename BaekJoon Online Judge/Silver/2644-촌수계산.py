import sys
from collections import deque

# 입력 받기
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

depth = 1  # 촌수
relationship = False  # 친척 관계 없음
graph = [[] for _ in range(n + 1)]  # 부모 관계 그래프
checked = []  # 탐색 완료한 사람

# 부모, 자식 관계 그래프
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


# bfs
def bfs(v):
    checked.append(v)  # v 탐색 완료
    queue = deque([v])

    while queue:
        for _ in range(len(queue)):  # 현재 사람의 자식의 수 만큼 탐색
            parent = queue.popleft()

            for child in graph[parent]:
                if child == b:  # 촌수를 찾고 있는 사람
                    global relationship
                    relationship = True
                    return

                if child not in checked:  # 미탐색
                    checked.append(child)
                    queue.append(child)

        global depth
        depth += 1  # 촌수 1 증가


# a와 b의 촌수 계산
bfs(a)

# 정답 출력
if relationship == True:
    print(depth)
else:
    print(-1)  # 촌수 관계 없음