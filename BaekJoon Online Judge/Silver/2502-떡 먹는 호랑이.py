import sys

d, k = map(int, sys.stdin.readline().split())

# 비율 점화식 구하기
ratio = [[1, 0], [0, 1]] # 첫째 날: 떡의 개수 a개, 둘째 날: 떡의 개수 b개
for i in range(2, d):
    a = ratio[i-2][0] + ratio[i-1][0]
    b = ratio[i-2][1] + ratio[i-1][1]

    ratio.append([a, b])

# a, b 비율
a, b = ratio[-1][0], ratio[-1][1]

# 떡 개수 찾기
count = 1 # 1개부터 시작
while True:
    if (k - a * count) % b != 0:
        count += 1
    else:
        print(count)
        print((k - a * count) // b)
        break
