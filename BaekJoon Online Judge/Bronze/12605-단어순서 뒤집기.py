import sys

# 단어 순서 뒤집기
def reverse_order(sentence):
    stack = []
    temp = []

    for s in sentence:
        if s != ' ':
            temp.append(s) 
        else:
            stack.append(''.join(temp))
            temp = [] # 단어 초기화

    stack.append(''.join(temp)) # 마지막 단어 추가
    stack.reverse()

    return stack

# 각 케이스에 대한 결과 생성
def set_result(index, sentence):
    str = f'Case #{index}: {sentence}'
    return str 

# main
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    answer = []

    for i in range(N):
        case = sys.stdin.readline().rstrip()
        reversed_sentence = reverse_order(case)
        answer.append(set_result(i+1, ' '.join(reversed_sentence)))

    print(*answer, sep='\n')