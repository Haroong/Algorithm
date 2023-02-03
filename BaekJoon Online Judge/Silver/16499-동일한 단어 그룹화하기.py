import sys
from collections import defaultdict

# 동일한 단어 그룹화
def grouping_word(words):
    word_dictionary = defaultdict(int)

    for w in words:
        if w not in word_dictionary:
            word_dictionary[w] = 1
        else:
            word_dictionary[w] += 1

    return word_dictionary


# 단어 딕셔너리의 키 개수 반환
def count_word_group(dictionary):
    return len(dictionary)


# main
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 단어의 개수
    words = sorted(''.join(sorted(sys.stdin.readline().rstrip())) for _ in range(N)) # 단어 목록
    answer = count_word_group(grouping_word(words))
    print(answer)