import sys

def is_equal_diff(number):
    digits =  [int(n) for n in str(number)]

    if len(digits) > 2: # 세자리수부터 판별
        diff = digits[1] - digits[0]

        for i in range(2, len(digits)):
            if digits[i] - digits[i-1] != diff:
                return False

    return True


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    answer = 0

    for i in range(1, N+1):
        if is_equal_diff(i):
            answer += 1

    print(answer)