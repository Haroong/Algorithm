import sys
from collections import deque

# 입력으로 받은 배열의 문장부호 제거
def remove_punctuation_marks(elements):
    removed_bracket = elements[1:-1] # 괄호 제거

    if removed_bracket == '': # 빈 배열
        result = []
    else:
        elements = removed_bracket.split(',') # 쉼표 제거
        result = [int(e) for e in elements]

    return result

# 연속된 reverse 연산 제거
def remove_streak_reverse_command(command):
    stack = []

    for c in command:
        if stack and stack[-1] == 'R' and c == 'R':
            stack.pop()
        else:
            stack.append(c)

    return stack


# 입력된 명령어 수행
def execute_command(command, numbers):
    d = deque(numbers)
    last_index = len(numbers)-1
    first_index = 0
    is_reversed = False # 반전 상태
    element_count = len(d) # 원소 개수

    # 명령어에 따른 연산 실행
    for c in command:
        if c == 'R': # Reverse 연산
            is_reversed = not is_reversed
        elif c == 'D' and element_count != 0: # Delete 연산
            element_count -= 1
            if is_reversed:
                d[last_index] = -1 # 삭제 표시
                last_index -= 1
            else:
                d[first_index] = -1
                first_index += 1
        else: # Error
            return 'error'

    # 배열 반전시키기
    if is_reversed == True:
        d = reversed(d)

    # 삭제 표시된 원소 제거
    d = [x for x in d if x != -1]

    return list(d)

# 문자열로 변환
def convert_to_string(numbers):
    add_comma = ','.join(map(str,numbers)) # 쉼표를 넣은 문자열
    return f'[{add_comma}]' # 대괄호를 문자열의 처음과 끝에 추가

# main
if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip()) # 테스트 케이스의 개수
    answer = []

    for _ in range(T):
        p = sys.stdin.readline().rstrip() # 실행할 명령어
        n = int(sys.stdin.readline().rstrip()) # 배열의 원소 개수

        elements = remove_punctuation_marks(sys.stdin.readline().rstrip())  # 문장부호가 제거된 원소 목록
        number_list = execute_command(remove_streak_reverse_command(p), elements) # 명령어 실행
        if number_list != 'error':
            elements = convert_to_string(number_list)
        else:
            elements = 'error'
        
        answer.append(elements)

    print(*answer, sep='\n')