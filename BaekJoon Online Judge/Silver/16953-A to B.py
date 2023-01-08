import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

# 정수 A를 B로 바꾸기
def convertNumber(a, b):
    queue = deque()
    queue.append([a, 1]) # 초기 숫자와 연산 최솟값

    count = -1

    while queue:
        number, count = queue.popleft()
        
        if number == b:
            print(count)
            return
        
        if number * 2 <= b:
            queue.append([number*2, count+1])

        
        if number * 10 + 1 <= b:
            queue.append([number*10+1, count+1])


    print(-1) # 연산 불가능


# main
if __name__ == '__main__':
    convertNumber(A, B)
