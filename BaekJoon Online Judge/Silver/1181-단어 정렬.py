import sys

N = int(input())
word_list = list(input() for _ in range(N))

word_list = list(dict.fromkeys(word_list))  # remove duplicates
word_list.sort()
word_list.sort(key=len)

for word in word_list:
    print(word)
