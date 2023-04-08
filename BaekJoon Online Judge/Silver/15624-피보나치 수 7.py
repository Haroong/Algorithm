import sys

GIVEN_NUMBER = 1000000007

# n번째 피보나치 수를 상수로 나눈 나머지를 반환한다
def get_nth_fibonacci_remainder(n):
    dp = [1] * n
    
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        for i in range(2, n):
            dp[i] = (dp[i - 2] + dp[i - 1]) % GIVEN_NUMBER 
    
    return dp[n - 1]

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip()) 
    answer = get_nth_fibonacci_remainder(n)
    print(answer)