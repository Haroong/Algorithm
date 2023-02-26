import sys

def is_good_word(word):
    stack = []

    for w in word:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 단어의 개수
    word_list = [sys.stdin.readline().rstrip() for _ in range(N)] # 단어 목록
    answer = 0

    # 좋은 단어 찾기
    for word in word_list:
        res = is_good_word(word)
        if res == True:
            answer += 1
    
    print(answer)