import sys

# fibonacci(n)이 실행되는 동안 0과 1이 출력되는 횟수를 반환
def get_printed_count_of_zero_and_one(n):
    fibonacci = [[1, 0], [0, 1]] # 0가 1에 대한 카운팅 횟수

    for i in range(2, n + 1):
        sum_of_last_fibonacci_zero = fibonacci[i-1][0] + fibonacci[i-2][0]
        sum_of_last_fibonacci_one = fibonacci[i-1][1] + fibonacci[i-2][1]
        fibonacci.append([sum_of_last_fibonacci_zero, sum_of_last_fibonacci_one])

    return fibonacci[n]

# 정답 형식 출력
def print_answer(counting_list):
    for c in counting_list:
        print(*c)

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip()) # 테스트 케이스의 개수
    answer = []
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip()) # fibonacci(N)
        counting_tuple = get_printed_count_of_zero_and_one(N)
        answer.append(counting_tuple)

    print_answer(answer)