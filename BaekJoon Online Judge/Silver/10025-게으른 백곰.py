import sys

MAX_ICE_BUCKET_COUNT = 1000001

# k만큼 떨어진 거리 내에 있는 얼음의 최대합
def find_maximum_ice(ice_bucket, last_index, k):
    size = 2*k+1 # 빽곰의 위치에서 좌우로 k만큼 떨어진 곳까지 닿음
    amount = sum(ice_bucket[:size]) # 초기 탐색 범위의 얼음 양
    result = amount

    for i in range(size, last_index+1):
        amount += ice_bucket[i] - ice_bucket[i-size] # 슬라이딩 윈도우의 크기만큼 움직이면서 맨 앞의 원소 빼고 맨 뒤의 원소 더함
        result = max(result, amount)

    return result


# main
if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split()) # 얼음 양동이의 개수, 빽곰의 위치
    bucket_info = [0] * MAX_ICE_BUCKET_COUNT
    last_bucket_index = 0 # 탐색 종료 인덱스

    for _ in range(N): 
        ice, position = map(int, sys.stdin.readline().split())
        bucket_info[position] = ice # 양동이의 위치에 얼음의 양을 표시
        last_bucket_index = max(last_bucket_index, position)

    answer = find_maximum_ice(bucket_info, last_bucket_index, K) # 얼음을 최대로 가질 수 있는 최적의 자리 찾기
    print(answer)