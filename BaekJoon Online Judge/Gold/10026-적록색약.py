import sys
import copy
from collections import  deque

COLOR_CHECKED = 1
COLOR_BLIND = True # 정상 시야의 사람
NORMAL_EYE_SIGHT = False # 적록색약인 사람

# 입력 받기
n = int(sys.stdin.readline().rstrip())
picture = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

normal_people_picture = copy.deepcopy(picture)  # 일반 사람이 보이는 그림
color_blindness_picture = copy.deepcopy(picture) # 적록색약인 사람이 보이는 그림

normal_color, blindness_color = 0, 0  # 정답


# 특정 좌표와 인접한 구역
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


# 탐색 불가능한 좌표 확인
def isUnsearchableCoordinate(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return True

    
# 현재 좌표에 대한 탐색 여부 체크
def isVisitedCoordinate(x, y, picture):
    if picture[x][y] == COLOR_CHECKED:
        return True

    
# 시작 좌표의 색상과 현재 좌표의 색상이 동일한지 여부 반환
def isSameColor(x, y, picture, color, is_color_blind):
    if isColorBlindness(is_color_blind): # 적록색약인 사람
        if color == 'G' or color == 'R': # 초록색 또는 빨강색
            colors = ['G', 'R']
            if picture[x][y] in colors:
                return True
        else:
            if picture[x][y] == color: # 파란색
                return True
    else: # 일반 사람
        if picture[x][y] == color:
            return True
        
    return False
    
        
# 일반 사람/적록색약 사람 판별
def isColorBlindness(is_color_blind):
    if is_color_blind == True:
        return True
    else:
        return False    


# 그림에 칠해진 색상 구역 찾기
def findColors(x, y, picture, person_type):
    queue = deque([])
    
    queue.append([x, y])
    current_color = picture[x][y]
    
    while queue:
        index = queue.popleft()
        picture[index[0]][index[1]] = COLOR_CHECKED

        for k in range(4): # 현재 좌표에서 상하좌우에 있는 색상 탐색
            new_x = index[0] + dx[k]
            new_y = index[1] + dy[k]

            if isUnsearchableCoordinate(new_x, new_y): # 탐색 불가능한 좌표
                continue
            
            if isVisitedCoordinate(new_x, new_y, picture): # 이전에 방문한 좌표
                continue

            if isSameColor(new_x, new_y, picture, current_color, person_type): # 탐색하는 색상과 동일한 색상인지 확인
                queue.append([new_x, new_y])
                picture[new_x][new_y] = COLOR_CHECKED
                


# n * n 리스트 탐색
for i in range(n):
    for j in range(n):
        if normal_people_picture[i][j] != COLOR_CHECKED:
            findColors(i, j, normal_people_picture, NORMAL_EYE_SIGHT)
            normal_color += 1

        if color_blindness_picture[i][j] != COLOR_CHECKED:
            findColors(i, j, color_blindness_picture, COLOR_BLIND)
            blindness_color += 1
        

# 정답 출력
print(normal_color, blindness_color, sep=' ')