import sys

def find_next_greater_number(numbers):
    stack = [numbers[-1]]
    result = [-1] # 오큰수
    numbers.pop() # 가장 마지막 원소 제거

    for i in range(len(numbers)-1, -1, -1):
        top = stack[-1]
        num = numbers[i]

        if num < top:
            stack.append(num)
            result.append(top)
        else: # 현재 원소가 스택 top보다 큼
            while stack:
                if num < stack[-1]:
                    break

                stack.pop()
            
            if not stack: # 스택이 빌 떄까지 더 큰 원소를 찾지 못함
                result.append(-1)

                if i != 0:
                    stack.append(num)
            else:
                result.append(stack[-1])
                stack.append(num)

    return result


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    elements = list(map(int, sys.stdin.readline().split()))
    
    res = find_next_greater_number(elements) # 오큰수 찾기

    answer = reversed(res) # 결과 리스트 반전
    print(*answer, sep=' ') # 정답 출력