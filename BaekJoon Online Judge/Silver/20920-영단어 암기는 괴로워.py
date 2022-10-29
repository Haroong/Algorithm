import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().rstrip() for _ in range(n)]

# 길이 m 이상인 단어만 추출
words = list(filter(lambda x: len(x) >= m, words))

# 단어장 딕셔너리
word_dictionary = dict()
for word in words:
    if word not in word_dictionary:
        word_dictionary[word] = 1
    else:
        word_dictionary[word] += 1

# 단어장 우선 순위 적용
words = sorted(word_dictionary.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

# 정답 출력
for index, value in enumerate(words):
    print(value[0])


