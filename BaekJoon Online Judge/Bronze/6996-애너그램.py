import sys

t = sys.stdin.readline()
test_word = [sys.stdin.readline().split() for _ in range(int(t))]
answer = []

for w in test_word:
    word_a, word_b = w[0], w[1]

    if sorted(word_a) != sorted(word_b):
        msg = f'{word_a} & {word_b} are NOT anagrams.'
    else:
        msg = f'{word_a} & {word_b} are anagrams.'

    answer.append(msg)

print(*answer, sep='\n')
