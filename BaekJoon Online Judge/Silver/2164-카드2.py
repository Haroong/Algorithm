import sys
from collections import deque

N = int(sys.stdin.readline().rstrip()) # 카드 N장
cards = deque(range(1, N+1)) # 1부터 N까지의 카드 번호

def shuffle_card():
    while True:
        if len(cards) == 1:
            break
        
        cards.popleft() # 제일 위에 있는 카드 버림
        
        top_card = cards[0] # 제일 위에 있는 카드를 가장 아래로 이동
        cards.append(top_card)
        cards.popleft()

shuffle_card()
print(*cards)