import sys

def receive_laser(heights):
    stack = []
    result = []

    for index, value in enumerate(heights):
        if stack and stack[-1][1] < value: # 스택 top의 값보다 현재 값이 더 크다
            while stack and stack[-1][1] < value:
                stack.pop()
        
        if not stack:
            result.append(0)
        else:
            result.append(stack[-1][0] + 1) # 스택 top의 인덱스를 저장
        
        stack.append([index, value])

    return result


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 탑의 개수
    tower_heights = list(map(int, sys.stdin.readline().split())) # 높이
    answer = receive_laser(tower_heights) # 왼쪽 방향으로 레이저 발사
    print(*answer)