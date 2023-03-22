import sys

STREAK_EMPTY_ZONE = 2

# 방에서 가로로 누울 수 있는 영역 찾기
def calculate_row(room):
    row = 0

    for i in range(len(room)):
        count = 0
        found_sleep_zone = True
        
        for index, value in enumerate(room):
            if room[i][index] == '.': # 빈 영역
                if found_sleep_zone:
                    count += 1
                    if count == STREAK_EMPTY_ZONE: # 가로로 눕기 가능
                        row += 1
                        count = 0
                        found_sleep_zone = False # 다음번 장애물이 나타날 때 까지 카운트 x
                else:
                    continue
            else: # 벽
                count = 0
                found_sleep_zone = True
    
    return row

# 방에서 세로로 누울 수 있는 영역 찾기
def calculate_col(room):
    col = 0

    for index, value in enumerate(room):
        count = 0
        found_sleep_zone = True

        for j in range(len(room)):
            if room[j][index] == '.': # 빈 영역
                if found_sleep_zone:
                    count += 1
                    if count == STREAK_EMPTY_ZONE: # 가로로 눕기 가능
                        col += 1
                        count = 0
                        found_sleep_zone = False # 다음번 장애물이 나타날 때 까지 카운트 x
                else:
                    continue
            else: # 벽
                count = 0
                found_sleep_zone = True
    
    return col

# 방에서 누울 수 있는 자리 수 반환
def count_comfort_zone(room):
    row = calculate_row(room)
    col = calculate_col(room)

    return row, col


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 방의 크기 N * N
    room = [sys.stdin.readline().rstrip() for _ in range(N)]
    answer = count_comfort_zone(room)
    print(*answer)