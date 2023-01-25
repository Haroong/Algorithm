import sys

# 숫자의 합
def sum_digits(number):
    digit = [int(x) for x in str(number)]
    result = sum(digit)

    return result

# main
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 숫자의 개수
    number = int(sys.stdin.readline().rstrip())
    answer = sum_digits(number)

    print(answer)