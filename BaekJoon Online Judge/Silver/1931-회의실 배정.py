import sys

# 입력 받기
n = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 정렬: 1) 종료 시간이 빠른 순, 2)시작 시간이 빠른 순
meetings.sort(key=lambda x:(x[1], x[0]))

# 사용 가능한 회의실 개수
count = 1
last_end_time = meetings[0][1] # 첫번째 회의의 종료 시간

for start, end in meetings[1:]:
    if start >= last_end_time:
        last_end_time = end
        count +=1

print(count)