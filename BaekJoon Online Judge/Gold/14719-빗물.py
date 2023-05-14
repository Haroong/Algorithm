import sys

def get_total_rainwater(blocks):
    result = 0

    for i in range(1, len(blocks) - 1): # 맨 왼쪽과 오른쪽 블록은 고려하지 않는다
        # 현재 인덱스를 기준으로 왼쪽의 max 높이, 오른쪽의 max 높이를 비교한다
        left = max(blocks[:i])
        right = max(blocks[i + 1:])

        water = min(left, right)

        if blocks[i] < water: # 현재 블록의 위치에 물이 고일 수 있음    
            result += water - blocks[i]

    return result

if __name__ == '__main__':
    H, W = map(int, sys.stdin.readline().split()) # 세로, 가로
    blocks = list(map(int, sys.stdin.readline().split())) # 블록의 높이
    answer = get_total_rainwater(blocks)
    print(answer)