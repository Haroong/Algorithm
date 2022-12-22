import sys

n, c = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))

# 딕셔너리에 각 숫자에 대한 인덱스, 빈도수 추가
num_dict = dict()
count = 1

for index, value in enumerate(sequence):
    if value not in num_dict:
        num_dict[value] = [index, count]
    else:
        num_dict[value][1] += 1 # count 1 증가
    
# 정렬
num_dict = dict(sorted(num_dict.items(), key=lambda x: (-x[1][1], x[1][0])))

# 정답 리스트 생성
answer = []
for key in num_dict.keys():
    loop = num_dict[key][1]
    [answer.append(key) for _ in range(loop)]

# 정답 출력
print(*answer)