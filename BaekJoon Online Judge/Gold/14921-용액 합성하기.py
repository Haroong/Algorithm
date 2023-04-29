import sys

# 두 용액의 합이 0과 가장 가까운 값을 반환
def get_value_of_minimum_sum(solutions):
    result = sys.maxsize
    left, right = 0, len(solutions) - 1 # 포인터 초기값

    while left < right:
        temp_sum = solutions[left] + solutions[right]
        if temp_sum == 0:
            return 0
        
        if abs(result) > abs(temp_sum):
            result = temp_sum # 최소값 갱신

        if temp_sum > 0:
            right -= 1
        else:
            left += 1

    return result

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 용액의 개수
    solutions = list(map(int, sys.stdin.readline().split())) # 용액의 특성값
    answer = get_value_of_minimum_sum(solutions)
    print(answer)