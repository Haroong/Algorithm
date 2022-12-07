import sys
from collections import deque

MAXIMUM_INPUT = 100000

n, k = map(int, sys.stdin.readline().split())
distance_time = dict() # 특정 좌표에 도달하기까지 걸리는 최소 시간

# 걷기 또는 순간이동으로 이동 가능한 거리
def setMovingPosition(num, sec, queue):
    distance = [num-1, num+1, num*2]

    for d in distance:
        if d > MAXIMUM_INPUT: # 최대 입력 가능한 숫자를 넘어서면 무시
            continue
        
        if d not in distance_time: # 탐색하지 않은 원소만 삽입
            queue.append(d)
            distance_time[d] = sec

    return queue


# 동생이 있는 위치까지의 소요 시간 계산
def findTargetPosition(position):
    queue = deque()
    seconds = 0 # 소요 시간
    distance_time[n] = seconds # 현재 위치

    seconds += 1

    setMovingPosition(position, seconds, queue) # 현재 위치에서 걷거나 순간이동한 결과를 큐에 추가
    
    if k in distance_time: # 목표 위치 발견
        print(seconds)
        return

    while queue:
        seconds += 1 # 1초 증가

        loop = len(queue) # 반복 횟수

        for _ in range(loop): # 특정 시간에 큐에 삽입된 원소의 개수만큼 반복
            current = queue.popleft()
            setMovingPosition(current, seconds, queue)

            if k in distance_time: # 목표 위치 발견
                print(seconds)
                return

                    
# 정답 출력
if n == k: # 동일한 위치에 존재
    print(0)
else:
    
    findTargetPosition(n)