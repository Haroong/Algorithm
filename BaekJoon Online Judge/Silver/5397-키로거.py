import sys

CURSOR_LEFT = '<'
CURSOR_RIGHT = '>'
DELETE = '-'

# 비밀번호 찾기
def decode_to_password(input_text):
    left, right = [], [] # 커서를 기준으로 문자열을 나눈다

    # 입력 문자열을 탐색
    for text in input_text:
        if text == CURSOR_LEFT:
            if left:
                right.append(left.pop())
        elif text == CURSOR_RIGHT:
            if right:
                left.append(right.pop())
        elif text == DELETE:
            if left:
                left.pop()
        else:
            left.append(text)

    if right:
        for r in right[::-1]:
            left.append(r)
    
    return left

# 문자열 합치기
def convert_to_string(text):
    str = ''.join(text)
    return str

# main
if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip()) # 테스트 케이스의 개수
    answer = []

    for _ in range(n):
        inp = sys.stdin.readline().rstrip()

        password = decode_to_password(inp) # 비밀번호 해킹!!
        result = convert_to_string(password)
        answer.append(result)
    
    print(*answer, sep='\n')