import sys
from collections import defaultdict

# 기본 입력 받기
n, m = map(int, sys.stdin.readline().split())

# 걸그룹 정보 딕셔너리
d = defaultdict(list)
answer = []

# 각각의 걸그룹 정보를 집합에 추가
for _ in range(n):
    group_name = sys.stdin.readline().rstrip()
    member_cnt = int(sys.stdin.readline().rstrip())

    for _ in range(member_cnt):
        member = sys.stdin.readline().rstrip()
        d[group_name].append(member)

# 퀴즈 맞추기
for _ in range(m):
    quiz = sys.stdin.readline().rstrip()
    quiz_type = int(sys.stdin.readline().rstrip())

    if quiz_type == 0:
        for key, value in d.items():
            if key == quiz:
                member_list = sorted(value)
                for m in member_list:
                    answer.append(m)
    else:
        for key, value in d.items():
            if quiz in value:
                answer.append(key)
                break

# 정답 출력
print(*answer, sep='\n')