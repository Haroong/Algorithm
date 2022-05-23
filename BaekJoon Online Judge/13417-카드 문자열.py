from collections import deque

testCase = int(input())
idx = 0
answer = []

while idx < testCase:
    n = int(input())
    result = deque()

    deque_card = deque(list(input().split()))
    result.append(deque_card.popleft())  # 처음 카드

    while deque_card:
        current = deque_card[0]  # 이번에 놓을 카드
        left = result[0]  # 가장 왼쪽에 놓인 카드

        if left < current:
            result.append(deque_card.popleft())
        else:
            result.appendleft(deque_card.popleft())

    answer.append(''.join(result))
    idx += 1

print('\n'.join(map(str, answer)))
