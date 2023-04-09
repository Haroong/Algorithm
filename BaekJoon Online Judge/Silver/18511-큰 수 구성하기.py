import sys
from itertools import product

# 중복 순열 구하기
def find_number_permutation(numbers, length):
    permutation = []
    
    while length > 0:
        for i in product(numbers, repeat=length):
            permutation.append(int(''.join(map(str, i))))
        length -= 1

    return permutation

# n보다 같거나 작은 자연수 반환
def get_largest_number(elements, n):
    result = 0
    permutation = sorted(find_number_permutation(elements, len(str(n))))

    start, end = 0, len(permutation) - 1
    while start <= end:
        mid = (start + end) // 2
        if permutation[mid] <= n:
            result = max(permutation[mid], result)
            start = mid + 1
        else:
            end = mid -1
    
    return result

# main
if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    elements = list(map(int, sys.stdin.readline().split())) # 집합 K의 원소
    answer = get_largest_number(elements, N)
    print(answer)