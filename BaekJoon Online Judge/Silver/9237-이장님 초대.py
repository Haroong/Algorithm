import sys

n = int(sys.stdin.readline().strip())
list_tree = list(map(int, sys.stdin.readline().split()))

PLANT_DAY = 1  # 묘목을 심는데 걸리는 기간(하루)

list_tree.sort(reverse=True)  # 생육 기간이 긴 나무 내림차순

for day in range(n):
    list_tree[day] = list_tree[day] + PLANT_DAY + (day+1)

print(max(list_tree))
