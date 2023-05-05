import sys

def get_cloud_passing_time(skyline):
    time = 0
    prev_cloud_exists = False
    result = []

    for i in range(len(skyline)):
        if skyline[i] == 'c':
            result.append(0)
            prev_cloud_exists = True
            time = 0 # 시간 초기화
        elif skyline[i] == '.':
            if prev_cloud_exists:
                time += 1 # 1분 경과
                result.append(time)
            else:
                result.append(-1) # 구름이 뜨지 않음
    
    return result
        

def print_answer(result):
    for res in result:
        print(*res, sep=' ')


if __name__ == '__main__':
    H, W = map(int, sys.stdin.readline().split()) # 마을 형태
    sky = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
    answer = []

    for i in range(H):
        answer.append(get_cloud_passing_time(sky[i]))

    print_answer(answer)