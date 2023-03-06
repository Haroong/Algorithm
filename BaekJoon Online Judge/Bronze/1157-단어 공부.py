import sys
from collections import defaultdict

# word의 알파벳을 카운팅한다
def count_alphabet(word):
    d = defaultdict(int)
    for w in word:
        ascii_code = ord(w)

        if w in d: # 딕셔너리에 해당 키가 존재
            d[w] += 1
        else:
            if ascii_code < 97: # 대문자
                if chr(ascii_code+32) not in d: # 현재 문자의 소문자가 딕셔너리에 있는지 확인
                    d[w] = 1
                else:
                    d[chr(ascii_code+32)] += 1
            else: # 소문자는 딕셔너리에 대문자로 저장
                if chr(ascii_code-32) not in d: # 현재 문자의 대문자가 딕셔너리에 있는지 확인
                    d[chr(ascii_code-32)] = 1
                else:
                    d[chr(ascii_code-32)] += 1


    return d

# word에서 가장 많이 사용된 알파벳을 반환한다
def most_used_alphabet(word):
    dictionary = count_alphabet(word)
    dictionary = sorted(dictionary.items(), key=lambda item:item[1], reverse=True) # 알파벳 카운팅 횟수를 기준으로 정렬
    
    if len(dictionary) == 1:
        return dictionary[0][0]
    else:
        if dictionary[0][1] == dictionary[1][1]:
            return -1
        else:
            return dictionary[0][0]

# 결과 형식 출력
def print_answer(res):
    if res == -1:
        print('?')
    else:
        print(res)

# main
if __name__ == '__main__':
    word = sys.stdin.readline().rstrip() # 입력 단어
    result = most_used_alphabet(word)
    print_answer(result)