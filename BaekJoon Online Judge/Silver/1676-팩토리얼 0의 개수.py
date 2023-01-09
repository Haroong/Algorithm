import sys

# 특정 숫자열의 맨 마지막 숫자 체크
def checkLastNumber(number):
    count = 0
    digits = [int(x) for x in str(number)]

    for n in digits[::-1]:
        if n == 0:
            count += 1
        else:
            break

    return count            


# 0의 개수 계산
def factorial(number):
    if number > 1: 
        return number * factorial(number-1)
    else: # 팩토리얼 연산 종료
        return 1


# main
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    number = factorial(N)
    print(checkLastNumber(number))