import sys

# 소인수분해
def prime_factorization(number):
    factor = 2
    factors = []

    while number != 1:
        count = 0
        while number % factor == 0:
            number //= factor
            count += 1 # 인수가 곱해진 횟수

        if count > 0:
            factors.append([factor, count])
            
        factor += 1
    
    return factors


def print_answer(elements):
    for factor, cnt in elements:
        print(factor, cnt)


if __name__ == '__main__':
    testcase = int(sys.stdin.readline().rstrip())
    answer = []

    for _ in range(testcase):
        N = int(sys.stdin.readline().rstrip())
        result = prime_factorization(N)
        answer.extend(result)

    print_answer(answer)