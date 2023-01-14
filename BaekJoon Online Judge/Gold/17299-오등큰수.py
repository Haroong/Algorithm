import sys
from collections import defaultdict

# 각 숫자의 빈도수 계산
def get_frequency(numbers):
    number_dict = defaultdict(int)

    for n in numbers:
        if n not in number_dict:
            number_dict[n] = 1
        else:
            number_dict[n] += 1
    
    return number_dict


# 오등큰수 탐색
def next_greater_number(elements):
    stack = []
    result = []

    frequency = get_frequency(elements) # 숫자의 빈도수

    for e in elements[::-1]:
        if not stack:
            result.append(-1)
        else:
            if frequency[e] >= frequency[stack[-1]]:
                while stack and frequency[e] >= frequency[stack[-1]]:
                    stack.pop()
            
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
        
        stack.append(e)

    return result


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 수열의 크기
    elements = list(map(int, sys.stdin.readline().split())) # 수열의 원소
    answer = reversed(next_greater_number(elements))
    print(*answer, sep=' ')