import sys
from collections import deque

def is_possible_sentence(sentence_list, target):
    loop = len(sentence_list)

    for target_word in target: # 받아쓴 문장의 단어 탐색
        found = False

        for i in range(loop):
            if sentence_list[i] and sentence_list[i][0] == target_word: # 문장의 첫 번째 단어가 일치
                sentence_list[i].popleft()
                found = True
                break

        if found == False:
            return False # 불가능한 단어를 받아 씀

    for s in sentence_list: # 앵무새가 말 할 단어가 남음
        if len(s) != 0:
            return False

    return True


def print_answer(result):
    if result == True:
        print('Possible')
    else:
        print('Impossible')


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 앵무새의 수
    spoken_by_parrot = [deque(sys.stdin.readline().split()) for _ in range(N)]  # 앵무새가 말한 문장
    written_sentence = sys.stdin.readline().split() # 받아적은 문장

    res = is_possible_sentence(spoken_by_parrot, written_sentence)
    print_answer(res)