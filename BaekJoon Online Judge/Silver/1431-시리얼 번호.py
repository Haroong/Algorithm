import sys

guitars = []

# 입력 받기
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    inp = sys.stdin.readline().rstrip()
    temp_sum = 0

    for i in inp:
        if i.isdigit():
            temp_sum += int(i)

    guitars.append([inp, temp_sum])


# 시리얼 번호 정렬 조건
guitars = sorted(guitars, key=lambda x:(len(x[0]), x[1], x[0]))

# 정답 출력
for guitar in guitars:
    print(guitar[0])