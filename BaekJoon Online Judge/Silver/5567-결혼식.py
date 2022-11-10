import sys
from collections import deque

# 입력 받기
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 결혼식에 초대할 사람 목록
answer = []

# 친구 관계 그래프 생성
friends = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

# BFS
def bfs(v):
    answer.append(v) # 결혼식에 초대 할 사람으로 추가
    queue = deque(friends[v])

    while queue:
        c = queue.popleft()
        answer.append(c)  # 내 친구 추가

        # 친구의 친구 추가
        for p in friends[c]:
            if p not in answer and p not in queue:
                answer.append(p)

# 결혼식에 초대할 사람 찾기
bfs(1)

# 정답 출력
print(len(answer)-1) # 본인 제외