import sys

# 단어의 알파벳으로 딕셔너리 생성
def set_alphabet_dictionary(words):
    alphabet = dict()

    for index, value in enumerate(words):
        if value not in alphabet:
            alphabet[value] = [index]
        else:
            alphabet[value].append(index)

    return alphabet

# word가 그룹 단어인지 여부 반환
def is_group_word(word):
    d = set_alphabet_dictionary(word)

    # 각 알파벳에 대해 저장된 인덱스 순서를 확인한다
    for key, value in d.items():
        if len(value) > 1:
            for i in range(1, len(value)):
                if value[i] - value[i - 1] != 1: # 두 수의 인덱스 차이가 1을 초과
                    return False
                
    return True

# main
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 단어의 개수
    words = [sys.stdin.readline().rstrip() for _ in range(N)]
    answer = 0

    for word in words:
        if is_group_word(word):
            answer += 1

    print(answer)