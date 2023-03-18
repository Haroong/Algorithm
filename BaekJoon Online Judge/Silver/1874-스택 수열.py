import sys

# 스택 수열의 생성 순서를 반환한다
def get_sequence_order(numbers):
    result = [] # 연산 순서
    stack = []
    count = 1

    for number in numbers:
        while count <= number:
            stack.append(count)
            result.append('+')
            count += 1
        
        if number == stack[-1]: # 현재 숫자가 stack top과 동일함
            stack.pop()
            result.append('-')
        else:
            return -1 # 스택에 오름차순으로 삽입 불가능

    return result

# 정답 형식 출력
def print_answer(result):
    if result == -1:
        print('NO')
    else:
        print(*result, sep='\n')

# main
if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip()) # n개의 정수
    numbers = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    answer = get_sequence_order(numbers)
    print_answer(answer)