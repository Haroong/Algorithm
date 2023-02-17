import sys

def find_liquid_combination(values):
    left_idx, right_idx = 0, len(values)-1
    ans_1, ans_2 = 0, 0
    liquid_sum = sys.maxsize

    while left_idx < right_idx:
        left, right = values[left_idx], values[right_idx]
        temp_sum = left + right

        if temp_sum == 0: # 두 용액의 특성값이 0
            return left, right
        
        if abs(temp_sum) < abs(liquid_sum): # 기존 합산값보다 현재의 절댓값이 더 작음
            liquid_sum = temp_sum
            ans_1, ans_2 = left, right
        elif temp_sum > 0:
            right_idx -= 1
        else:
            left_idx += 1

    return ans_1, ans_2


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 전체 용액의 수
    liquid_value = list(map(int, sys.stdin.readline().split())) # 용액의 특성값
    answer = find_liquid_combination(liquid_value)
    print(*answer)