import sys, math

def is_prime_number(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def is_palindrome(n):
    reversed_number = int((str(n))[::-1])

    if n == reversed_number:
        return True
    else:
        return False


def get_minimum_number(n):
    check_number = n

    while True:
        if is_palindrome(check_number):
            if is_prime_number(check_number):
                return check_number
            else:
                check_number += 1
        else:
            check_number += 1


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    if N == 1:
        print(2)
    else:
        answer = get_minimum_number(N)
        print(answer)