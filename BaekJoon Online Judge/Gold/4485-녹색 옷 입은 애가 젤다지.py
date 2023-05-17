import sys
from collections import deque

# 탐색 가능한 좌표인지 확인
def is_valid_coordinate(x, y, size):
    if 0 <= x < size and 0 <= y < size:
        return True
    else:
        return False
    

# 목표 지점까지의 최소 비용 계산
def get_minimum_lost_rupee(cost, cave):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque([[0, 0]])

    while queue:
        x, y = queue.popleft()

        for i in range(4): # 현재 좌표에서 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if is_valid_coordinate(nx, ny, len(cave)):
                if cost[nx][ny] > cost[x][y] + cave[nx][ny]: # 이동하려는 좌표의 루피 소모 비용 비교
                    cost[nx][ny] = cost[x][y] + cave[nx][ny] # 최소 비용으로 갱신
                    queue.append([nx, ny])

    return cost
        

# 정답 출력 형식 설정
def set_answer_form(count, cost):
    result = f'Problem {count}: {cost}'
    return result


if __name__ == '__main__':
    testcase = 1
    answer = []

    while True:
        N = int(sys.stdin.readline().rstrip()) # 동굴의 크기
        if N == 0: # 입력 종료
            break
    
        cave = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 도둑루피의 크기
        cost = [[sys.maxsize] * len(cave) for _ in range(len(cave))] # 루피 소모 비용
        cost[0][0] = cave[0][0] # 시작 지점
        result = get_minimum_lost_rupee(cost, cave) 
        answer.append(set_answer_form(testcase, result[N-1][N-1]))
        testcase += 1

    for ans in answer:
        print(ans)