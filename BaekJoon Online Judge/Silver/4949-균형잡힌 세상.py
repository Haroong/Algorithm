import sys

# 균형잡힌 문자열인지 여부 반환
def is_balanced_string(sentence):
    stack = []

    for s in sentence:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack.pop() != '(':
                return False    
        elif s == ']':
            if not stack or stack.pop() != '[':
                return False   

    if stack:
        return False
    else:
        return True

# 각 케이스에 대한 결과 추가
def add_to_answer(balance, answer):
    if balance == True:
        answer.append('yes')
    else:
        answer.append('no')

    return answer

# main
if __name__ == '__main__':
    answer = []

    while True:
        sentence = sys.stdin.readline().rstrip()
        if sentence == '.': # 입력 종료
            break
        result = is_balanced_string(sentence)
        add_to_answer(result, answer)
    
    print(*answer, sep='\n')