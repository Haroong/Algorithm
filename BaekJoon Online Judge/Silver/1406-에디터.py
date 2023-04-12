import sys

# 명령어 L 실행
def execute_command_L():
    if cursor_left:
        cursor_right.append(cursor_left.pop()) # 커서 왼쪽의 마지막 문자를 오른쪽으로 이동
    
    return

# 명령어 D 실행
def execute_command_D():
    if cursor_right:
        cursor_left.append(cursor_right.pop()) # 커서 오른쪽의 마지막 문자를 왼쪽으로 이동
    
    return

# 명령어 B 실행
def execute_command_B():
    if cursor_left:
        cursor_left.pop() # 커서 왼쪽의 마지막 문자 제거
    
    return

# 명령어 P 실행
def execute_command_P(text):
    return cursor_left.append(text) # 커서 왼쪽에 text 문자열을 추가함

# 에디터에 내장된 각 명령어를 호출한다
def run_editor_commands(input_command):
    command = input_command[0]

    if command == 'L':
        execute_command_L()
    elif command == 'D':
        execute_command_D()
    elif command == 'B':
        execute_command_B()
    else:
        text = input_command[2] # 한 칸 띄어쓰기 때문
        execute_command_P(text)

    return

# 초기 문자열을 왼쪽 커서에 삽입한다
def insert_init_text_into_left_cursor(init_text):
    for text in init_text:
        cursor_left.append(text)

    return cursor_left

# 최종으로 편집된 문자열을 반환한다
def get_edited_text():
    if cursor_right:
        cursor_left.extend(reversed(cursor_right))

    return ''.join(cursor_left)  

# main
if __name__ == '__main__':
    cursor_left = []
    cursor_right = []

    init_text = sys.stdin.readline().rstrip() # 에디터에 입력된 초기 문자열
    insert_init_text_into_left_cursor(init_text) # 초기 문자열을 왼쪽 커서에 삽입
    M = int(sys.stdin.readline().rstrip()) # 명령어의 개수
    
    # 명령어의 길이만큼 반복
    for _ in range(M):
        input_command = sys.stdin.readline().rstrip()
        run_editor_commands(input_command)

    answer = get_edited_text()
    print(answer)