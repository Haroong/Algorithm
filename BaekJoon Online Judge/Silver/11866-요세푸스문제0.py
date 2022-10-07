from collections import deque

n, k = map(int, input().split())
deque_people = deque(list(range(1, n+1)))

cnt = 0
result = []

while deque_people:
    cnt += 1

    if cnt == k:
        result.append(deque_people.popleft())  # 원소 제거
        cnt = 0
    else:
        deque_people.append(deque_people.popleft())  # 가장 왼쪽에 있는 원소 삭제 및 추가

print(str(result).replace('[', '<').replace(']', '>'))  # 대괄호 변경
