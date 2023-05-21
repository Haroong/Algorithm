import sys

# 수열에서 두 수의 차이가 target 이상인 값 중에서 최소값을 반환한다
def get_minimum_diff(numbers, target):
    result = sys.maxsize
    start, end = 0, 0 # 같은 수를 골라도 됨
    loop = len(numbers)

    while start < loop and end < loop: 
        diff = numbers[end] - numbers[start]
        
        if diff < target:
            end += 1
        else:
            result = min(result, diff) # 최소값 갱신
            start += 1
        
    return result


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split()) # N개의 정수, 두 수의 차이 M
    numbers = sorted(list(int(sys.stdin.readline().rstrip()) for _ in range(N))) # 수열
    answer = get_minimum_diff(numbers, M)
    print(answer)