import sys

# 입력 받기
n = int(sys.stdin.readline().rstrip())
rainbow_dancer = [] # 무지개 댄스를 추는 곰곰이 목록

# 무지개 댄스를 추는 곰곰이 마리수 찾기
for _ in range(n):
    a, b = sys.stdin.readline().split()
    if a == 'ChongChong' or b == 'ChongChong' or a in rainbow_dancer or b in rainbow_dancer: # 무지개 댄스 전파자
        if a not in rainbow_dancer:
            rainbow_dancer.append(a)
        if b not in rainbow_dancer:
            rainbow_dancer.append(b)

# 정답 출력
print(len(rainbow_dancer))