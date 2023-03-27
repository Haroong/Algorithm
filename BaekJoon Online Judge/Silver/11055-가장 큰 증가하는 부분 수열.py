import sys

# 증가하는 부분 수열 중 가장 큰 합계 반환
def largest_sum_of_increasing_subsequence(sequence):
    dp = [1] * len(sequence)
    
    for index, value in enumerate(sequence):
        partial_sum = 0

        for loop_i, loop_v in enumerate(sequence[:index]): # 현재 인덱스 전까지의 작은 값을 탐색
            if loop_v < value:
                partial_sum = max(dp[loop_i], partial_sum)
        
        dp[index] = partial_sum + value
    
    return max(dp)


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 수열의 크기
    sequence = list(map(int, sys.stdin.readline().split())) # 수열
    answer = largest_sum_of_increasing_subsequence(sequence)
    print(answer)