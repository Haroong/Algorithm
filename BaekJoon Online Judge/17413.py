str = input()

stack, answer = [], []
idx = 0


def convertToString(stack):
    str = ''.join(stack)  # 문자열로 변환
    addAnswer(str)


def addAnswer(str):
    answer.append(str)


while idx < len(str):
    if str[idx] == '<':  # 특수문자
        if stack:  # 스택에 이전 문자열이 존재
            stack.reverse()
            convertToString(stack)
            stack = []
        while str[idx] != '>':
            stack.append(str[idx])
            idx += 1
        stack.append('>')
        convertToString(stack)
        stack = []
    elif str[idx].isspace():  # 공백
        stack.reverse()
        convertToString(stack)
        answer.append('')
        stack = []
    else:  # 알파벳 소문자 또는 숫자
        stack.append(str[idx])

    idx += 1

stack.reverse() # 마지막 문자열 처리
convertToString(stack)  

for str in answer:
    if str != '':
        print(str, end='')
    else:
        print(' ', end='')
