import sys

# 연속으로 가장 따뜻한 날의 온도의 합 반환
def max_warm_days(temperature, k):
    result = sum(temperature[:k])
    temp_sum = result

    for s in range(k, len(temperature)):
        temp_sum += temperature[s] - temperature[s-k]
        result = max(result, temp_sum)
    
    return result


# main
if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split()) # 전체 날짜의 수, 연속된 날짜의 수
    temperature = list(map(int, sys.stdin.readline().split())) # 측정한 온도
    answer = max_warm_days(temperature, K)
    print(answer)