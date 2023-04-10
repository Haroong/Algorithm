import sys

# 재귀 호출의 시간 복잡도
def recursion_time_complexity(n, count):
    if n == 1 or n == 2:
        count += 1
        return count
    else:
        return recursion_time_complexity(n - 2, count) + recursion_time_complexity(n - 1, count)

# 다이나믹 프로그래밍의 시간 복잡도
def dp_time_complexity(n):
    return n - 2

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    
    answer = []
    answer.append(recursion_time_complexity(n, 0))
    answer.append(dp_time_complexity(n))

    print(*answer, sep=' ')
