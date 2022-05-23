from collections import deque

n = int(input())
deque_ballon = deque(list(map(int, input().split())))  # 종이에 적힌 숫자
deque_index = deque(list(range(1, n+1)))  # 풍선 번호

answer = [1]  # 1번 풍선을 첫번째로 터뜨림
paper = deque_ballon[0]  # 터뜨린 풍선에 적힌 숫자 확인

while deque_ballon:
    deque_ballon.popleft()  # 터뜨린 풍선 제거
    deque_index.popleft()  # 터뜨린 풍선 번호 제거

    if len(deque_ballon) == 1:
        answer.append(deque_index[0])
        break
    elif paper > 0:
        for i in range(paper-1):
            deque_ballon.append(deque_ballon.popleft())
            deque_index.append(deque_index.popleft())
    else:
        for i in range(abs(paper)):
            deque_ballon.appendleft(deque_ballon.pop())
            deque_index.appendleft(deque_index.pop())

    answer.append(deque_index[0])
    paper = deque_ballon[0]  # 터뜨린 풍선에 적힌 숫자 확인

print(*answer)
