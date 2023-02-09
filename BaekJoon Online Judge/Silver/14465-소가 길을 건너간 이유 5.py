import sys

# 전체 신호등의 고장 여부 체크
def check_all_traffic_lights_status(n, lights):
    broken_status = [False] * n

    for x in lights:
        broken_status[x-1] = True

    return broken_status 


# 고장난 신호등 개수 반환
def count_broken_traffic_lights(traffic_lights):
    count = 0 

    for v in traffic_lights:
        if v == True:
            count += 1

    return count


# 최소로 수리가 필요한 신호등 개수 반환
def get_minimum_traffic_light_to_fix(n, broken, streak):
    is_broken = check_all_traffic_lights_status(n, sorted(broken)) # 리스트에 고장난 신호등을 표시
    count = count_broken_traffic_lights(is_broken[:streak]) # 수리가 필요한 신호등
    result = count

    for j in range(streak, n): # 슬라이딩 윈도우의 크기로 전체 리스트 탐색
        count += count_broken_traffic_lights([is_broken[j]]) - count_broken_traffic_lights([is_broken[j-streak]])
        result = min(result, count)

    return result


# main
if __name__ == '__main__':
    N, K, B = map(int, sys.stdin.readline().split()) # 1부터 N번 까지의 신호등, 연속된 목표 신호등 개수, 고장난 신호등 개수
    broken_traffic_lights = [int(sys.stdin.readline().rstrip()) for _ in range(B)]
    answer = get_minimum_traffic_light_to_fix(N, broken_traffic_lights, K)
    print(answer)