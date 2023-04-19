import sys, math

# n의 최대값 설정
def set_maximum_range(n):
    if n > 10000000:
        n = 10000000

    return n

# x에서 y까지인 자연수 중에서 팰린드롬인 수를 반환
def get_palindrome_number(start, end):
    result = []
    number = start

    while True:
        if number == 11 or (len(str(number)) % 2 == 1 and number == int(str(number)[::-1])): # 홀수 길이의 자연수거나 11이면 팰린드롬 목록에 넣어줌
            result.append(number)

        number += 1
        if number == end + 1:
            break

    return result

# 팰린드롬 숫자 집합에서 소수만 반환
def get_prime_numbers(numbers):
    end_number = max(numbers)
    result = set(numbers) # 삭제 연산의 시간 복잡도를 위해 집합으로 변환

    for i in range(2, int(math.sqrt(end_number))):
        for j in range(i * 2, end_number + 1, i):
            if j in result:
                result.remove(j) # i의 배수는 소수가 아님

    return result

# x부터 y까지인 자연수 중 소수이면서 팰린드롬인 목록 반환
def get_palindromic_primes(x, y):
    palindrome_numbers = get_palindrome_number(x, set_maximum_range(y))
    prime_numbers = []

    if len(palindrome_numbers) != 0:
        prime_numbers = sorted(list(get_prime_numbers(palindrome_numbers)))
    prime_numbers.append(-1) # 문제의 마지막 조건임

    return prime_numbers

# main
if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().split())
    answer = get_palindromic_primes(a, b)
    print(*answer, sep='\n')