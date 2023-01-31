import sys

# 절단 가능한 랜선의 최대 길이
def max_lan_cable_length(cables, target):
    start = 0
    end = max(cables)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if mid == 0:
            return end
        
        count = 0 # 잘라낸 랜선의 개수
        for cable in cables:
            if cable == mid:
                count += 1
            elif cable > mid:
                cut = cable // mid
                count += cut
        if count < target: # 필요 개수보다 부족한 개수
            end = mid - 1 
        else: # 필요 개수보다 초과해서 랜선을 절단함
            start = mid + 1
            result = mid
        
    return result


# main
if __name__ == '__main__':
    K, N = map(int, sys.stdin.readline().split()) # 보유한 랜선 개수, 필요한 랜선 개수
    lan_cables = sorted([int(sys.stdin.readline().rstrip()) for _ in range(K)]) # 보유한 랜선의 길이 리스트
    answer = max_lan_cable_length(lan_cables, N)
    print(answer)