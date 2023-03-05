import sys

# 문제에서 주어진 코드의 시간 복잡도를 반환한다
# 이번 문제의 시간 복잡도는 상수 시간임
def get_time_complexity(n):
    execute_time = 1

    return execute_time

# 최고차항의 차수 반환
def get_degree(n):
    degree = 0

    return degree

# main
if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip()) # 입력의 크기
    print(get_time_complexity(n))
    print(get_degree(n))