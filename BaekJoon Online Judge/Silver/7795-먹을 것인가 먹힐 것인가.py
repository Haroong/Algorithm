import sys

def is_smallest(x, y):
    if x <= y:
        return True

def is_biggest(x, y):
    if y < x:
        return True

def binary_search(target, data):
    left, right = 0, len(data)-1 # 이분탐색 초기 값
    index = -1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] < target:
            index = mid
            left = mid + 1
        else:
            right = mid - 1

    return index


if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip()) # 테스트 케이스의 개수
    answer = []

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split()) # 각각의 생명체 종류의 수
        creature_a = sorted(list(map(int,sys.stdin.readline().split())))
        creature_b = sorted(list(map(int,sys.stdin.readline().split())))
        
        res = 0
        for a in creature_a:
            if not is_smallest(a, creature_b[0]): # 아무것도 못 먹음
                if is_biggest(a, creature_b[-1]):  # 모든 생명체를 다 먹을 수 있음
                    res += M
                else:
                    res += binary_search(a, creature_b) + 1# 인덱스는 0부터 시작하므로 1 더해줌

        answer.append(res)
    
    print(*answer, sep='\n')