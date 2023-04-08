import sys

MAX_CHARACTER_PER_LINE = 10

def get_splitted_line(word):
    mod = len(word) % MAX_CHARACTER_PER_LINE
    line = len(word) // MAX_CHARACTER_PER_LINE

    if mod == 0:
        return line
    else: # 나머지가 존재하면 전체 줄 1 증가
        return line + 1        

def split_word_by_length(word):
    total_line = get_splitted_line(word) # 전체 줄 개수
    loop = 0
    splitted_word = []

    while loop < total_line:
        splitted_word.append(word[loop * MAX_CHARACTER_PER_LINE: (loop + 1) * MAX_CHARACTER_PER_LINE])
        loop += 1
    
    return splitted_word

def print_answer(word_list):
    for words in word_list:
        print(words, sep='\n')

if __name__ == '__main__':
    input_word = sys.stdin.readline().rstrip() # 입력 단어
    result = split_word_by_length(input_word)
    print_answer(result)