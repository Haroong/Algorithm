import sys

# 현재 숫자의 분해합을 구한다
def calculate_digits_sum(number):
    digits = [int(n) for n in str(number)]
    return number + sum(digits)

# 가장 작은 수를 반환한다
def get_small_number(list_number):
    if len(list_number) == 0:
        return 0
    else:
        return min(list_number)

# number의 가장 작은 생성자 반환
def find_smallest_constructor(target):
    result = []

    for i in range(1, target + 1):
        d_sum = calculate_digits_sum(i)

        if d_sum == int(target): # 분해합이 target 숫자와 같음
            result.append(i)

    constructor = get_small_number(result)
    return constructor

# main
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 자연수 N
    answer = find_smallest_constructor(N)
    print(answer)