import sys
from collections import deque
from collections import defaultdict

# 입력 받기
f, s, g, u, d = map(int, sys.stdin.readline().split())

floor_info = defaultdict(int)
TOP_FLOOR = f
BOTTOM_FLOOR = 1

# d층 아래로 내려가는 버튼
def pressDownButton(floor, count, queue):
    move = floor - d

    if move < BOTTOM_FLOOR: # 최저층보다 더 낮음
        return
    
    if move not in floor_info:
        floor_info[move] = count # 현재 층에 도달하기 까지 누른 버튼 횟수
        queue.append(move)


# u층 위로 올라가는 버튼
def pressUpButton(floor, count, queue):
    move = floor + u

    if move > TOP_FLOOR: # 최고층보다 더 높음
        return
    
    if move not in floor_info:
        floor_info[move] = count # 현재 층에 도달하기 까지 누른 버튼 횟수
        queue.append(move)

        
# 목표층인지 확인
def isTargetFloor():
    if g in floor_info:
        return True
    else:
        return False        

    
# 정답 출력
def printAnswer(res):
    if res != -1:
        print(res)
    else:
        print('use the stairs')

        
# 목표 층수까지 눌러야 하는 횟수 계산
def findButtonPressCount(start):
    queue = deque()
    queue.append(start)

    count = 1

    while queue:
        loop = len(queue)

        for _ in range(loop):
            current = queue.popleft()

            pressDownButton(current, count, queue)
            pressUpButton(current, count, queue)

            if isTargetFloor(): # 목표 층 발견
                return count
            
        count += 1
        
    return -1 # 엘리베이터로 이동 불가능


# 정답 찾기
if s == g: # 현재 층과 목표 층이 동일
    print(0)
else:
    floor_info[s] = 0

    result = findButtonPressCount(s)
    printAnswer(result)