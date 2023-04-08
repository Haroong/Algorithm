import sys

def get_maximum_multiple_of_30(n):
    digits = sorted([int(x) for x in str(n)], reverse=True)
    
    if 0 not in digits:
        return -1
    else:
        number = int(''.join(map(str, digits)))
        if number % 30 == 0:
            return number
        else:
            return -1

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    answer = get_maximum_multiple_of_30(N)
    print(answer)