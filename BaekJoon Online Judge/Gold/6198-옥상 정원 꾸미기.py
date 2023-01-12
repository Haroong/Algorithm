import sys

def observing_next_building(n, building_heights):
    stack = []
    result = 0 # 각 건물에서 관찰 가능한 건물 개수

    for i in range(n):
        current_height = building_heights[i]

        while stack and stack[-1] <= current_height:
            stack.pop() # 현재 높이보다 낮은 빌딩
        
        stack.append(current_height)
        result += len(stack) -1 # 자기 자신 제외
    
    return result


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 빌딩의 개수
    building_heights = [int(sys.stdin.readline().rstrip()) for _ in range(N)] # 각 빌딩의 높이

    answer = observing_next_building(N, building_heights)
    print(answer)
