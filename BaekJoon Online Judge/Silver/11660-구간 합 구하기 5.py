import sys

# 2차원 배열에서 (x1, y1)부터 (x2, y2) 까지의 합을 반환한다
def get_prefix_sum_in_list(prefix_sum, x1, y1, x2, y2):
    result = 0

    for i in range(x1, x2 + 1):
        if y1 == 0: # 행의 시작 인덱스
            result += prefix_sum[i][y2]
        else:
            result += prefix_sum[i][y2] - prefix_sum[i][y1 - 1]

    return result

# 2차원 배열의 행을 기준으로 누적합을 계산한다 
def sum_list_element_by_row(grid):
    result = []

    for i in range(len(grid)):
        row = []

        for j in range(len(grid)):
            if j == 0: # 첫번째 원소의 누적합은 자기 자신임
                row.append(grid[i][j])
            else:
                row.append(sum(grid[i][:j + 1]))

        result.append(row)

    return result


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split()) # 2차원 배열의 크기, 테스트 케이스의 개수
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 배열에 적힌 숫자
    prefix_sum = sum_list_element_by_row(grid)

    answer = []

    for _ in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split()) # 구간합을 구할 좌표

        if x1 == x2 and y1 == y2:
            answer.append(grid[x1 - 1][y1 - 1])
        else:
            result = get_prefix_sum_in_list(prefix_sum, x1 - 1, y1 - 1, x2 - 1, y2 - 1) # 인덱스를 맞추기 위해
            answer.append(result)

    print(*answer,sep='\n')