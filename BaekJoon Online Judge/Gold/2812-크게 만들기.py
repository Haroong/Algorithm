import sys

def erase_number(numbers, k):
    stack = []
    elements = [int(i) for i in str(numbers)]
    removed_count = 0 # 지운 숫자 개수

    # 지워야 할 숫자 탐색
    for index, value in enumerate(elements):
        if stack and stack[-1] < value:
            while stack and stack[-1] < value:
                stack.pop()
                removed_count += 1 
                if removed_count == k: # k번 지우기 완료
                    for e in elements[index:]: # 현재 인덱스 뒤에 남은 숫자들을 스택에 추가
                        stack.append(e)
                    return stack

        stack.append(value)


    # 지워야 할 횟수가 남음
    if removed_count != k:
        remain = k - removed_count
        for _ in range(remain):
            stack.pop()

    return stack


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    numbers = int(sys.stdin.readline().rstrip())
    answer = erase_number(numbers, K)
    print(*answer,sep='')