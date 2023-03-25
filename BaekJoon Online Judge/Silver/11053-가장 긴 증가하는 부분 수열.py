import sys

# 가장 긴 증가하는 부분 수열의 길이 반환
def get_longest_increasing_subsequence(sequence):
    dp = []

    for index, value in enumerate(sequence):
        length = 1 # 자기 자신

        for j in range(0, index):
            if sequence[j] < value: # 현재 탐색의 기준이 되는 값보다 작은 수
                length = max(length, dp[j] + 1) # 지금까지의 길이와 d[j]에 자기 자신 길이를 더한 값 비교

        dp.append(length)
    
    return max(dp)

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 수열의 크기
    sequence = list(map(int, sys.stdin.readline().split())) # 수열의 원소
    answer = get_longest_increasing_subsequence(sequence)
    print(answer)