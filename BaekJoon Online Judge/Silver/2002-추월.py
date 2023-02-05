import sys

# 추월한 자동차 수 계산
def count_passsing_cars(in_order, out_order):
    enter = dict()
    count = 0

    # 터널에 들어간 차 번호와 들어간 순서를 딕셔너리에 저장
    for index, value in enumerate(in_order, 1):
        enter[value] = index

    # 추월한 차 확인
    for i in range(len(out_order)): # 터널을 나온 순서대로 탐색
        for j in range(i+1, len(out_order)): # 현재 인덱스보다 뒤에 위치한 차 탐색
            if enter[out_order[i]] > enter[out_order[j]]: # 현재 차보다 늦게 터널을 나온 차 중 먼저 터널에 들어간 차 존재
                count += 1
                break

    return count


# main
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 차 대수
    tunnel_in_order = [sys.stdin.readline().rstrip() for _ in range(N)] # 터널에 들어간 순서
    tunnel_out_order = [sys.stdin.readline().rstrip() for _ in range(N)] # 터널에 나온 순서
    answer = count_passsing_cars(tunnel_in_order, tunnel_out_order)
    print(answer)