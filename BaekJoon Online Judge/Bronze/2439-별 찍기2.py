import sys

# 오른쪽 정렬된 n줄의 별 찍기
def print_stars(n):
    for i in range(n):
        row_stars = ''

        for j in range(n):
            if j < n - i - 1:
                row_stars += ' '
            else:
                row_stars += '*'

        print(row_stars)


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    print_stars(N)