import sys

n = int(sys.stdin.readline().strip())
inp = [int(sys.stdin.readline()) for _ in range(n)]

flag = inp[0]  # 다솜이의 초기 득표 수
list_vote = sorted(inp[1:], reverse=True)
count = 0

while True:
    if not list_vote:
        break

    if flag > max(list_vote):  # 매수 완료, 당선 확정
        break

    if list_vote[0] >= flag:
        count += 1  # 매수한 인원
        flag += 1  # 조작된 득표 수
        list_vote[0] -= 1
        list_vote.sort(reverse=True)

print(count)
