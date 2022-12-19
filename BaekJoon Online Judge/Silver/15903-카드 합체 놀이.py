import sys
from collections import deque

# 입력 받기
n, m =  map(int, sys.stdin.readline().split())
cards = deque(map(int, sys.stdin.readline().split()))

# 최저 합산 점수 계산
for _ in range(m):
    cards = deque(sorted(cards))
    
    min1, min2 = cards.popleft(), cards.popleft()

    cards.append(min1 + min2)
    cards.append(min1 + min2)

# 정답 출력
print(sum(cards))
