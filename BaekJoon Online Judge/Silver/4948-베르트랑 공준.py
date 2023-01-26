import sys
import math

LAST_NUMBER = 123456

# 모든 수에 대한 소수 판별
def check_prime_number(numbers):
    end = int(math.sqrt(LAST_NUMBER*2+1))
    for i in range(2, end):
        if numbers[i] == False:
            continue
        else:
            for j in range(2*i, LAST_NUMBER*2+1, i): # j의 모든 배수를 False 처리(소수 아님)
                numbers[j] = False
    
    return numbers

# n보다 크고, 2n보다 작거나 같은 소수의 개수 반환
def get_prime_number_count(n, numbers):
    count = 0

    for i in range(n+1, 2*n+1):
        if numbers[i] == True:
            count += 1
    
    return count

# 정답 출력
def print_answer(count):
    for c in count:
        print(c)


if __name__ == '__main__':
    # 범위 내의 모든 수에 대하여 미리 소수 판별을 해둔다
    prime_numbers = dict.fromkeys(range(2, LAST_NUMBER*2+1), True) 
    check_prime_number(prime_numbers)
    
    answer = []

    while True:
        n = int(sys.stdin.readline().rstrip())
        if n == 0: # 입력 종료
            break

        res = get_prime_number_count(n, prime_numbers)
        answer.append(res)

    print_answer(answer)