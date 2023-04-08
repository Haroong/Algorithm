import sys

def award_cutline(score, limit):
    return score[limit -1]


if __name__ == '__main__':
    N, k = map(int, sys.stdin.readline().split()) # 응시자 수, 수상자 제한 수
    scores = sorted(list(map(int, sys.stdin.readline().split())), reverse=True) # 점수
    answer = award_cutline(scores, k)
    print(answer)