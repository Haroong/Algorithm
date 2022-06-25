import sys

n = int(sys.stdin.readline().strip())
dp = [0] * (n+1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1  # 연산 3: 1 빼기

    if i % 2 == 0:  # 연산 2: 2로 나누기
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:  # 연산 1: 3으로 나누기
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])
