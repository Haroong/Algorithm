import sys

# 문제에서 주어진 코드의 시간 복잡도를 반환한다
# 이번 문제의 시간 복잡도는 O(n^3)
def get_execute_count(n):
    res = pow(n, 3)
    return res

# 최고차항의 차수 반환
def get_degree():
    degree = 3
    return degree

# main
if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip()) # 입력의 크기
    print(get_execute_count(n))
    print(get_degree())