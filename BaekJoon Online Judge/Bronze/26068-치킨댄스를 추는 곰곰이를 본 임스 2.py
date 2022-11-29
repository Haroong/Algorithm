import sys

# 입력 받기
n = int(sys.stdin.readline().rstrip())
gifticon = [sys.stdin.readline().rstrip() for _ in range(n)]

# 정답
answer = 0

# 유효기간이 90일 이하로 남은 기프티콘 판별
for g in gifticon:
    date = g[2:]
    if int(date) <= 90:
        answer += 1

# 정답 출력
print(answer)