from collections import deque

n, m = map(int, input().split())
list_target = list(map(int, input().split()))
d = deque(list(range(1, n + 1, 1)))

count = 0

for target in list_target:
    midIndex = len(d) // 2

    while True:
        if d[0] == target:
            d.popleft()
            break
        else:
            idx = d.index(target)  # 뽑아내려는 숫자가 위치한 덱의 인덱스
            if idx <= midIndex:
                d.rotate(-1)  # 왼쪽으로 회전
                count += 1
            else:
                d.rotate(1)  # 오른쪽으로 회전
                count += 1

print(count)
