import sys
from collections import defaultdict

# 이름별로 참가자 명단 정리
def marathon_participants(participants):
    participant_dict = defaultdict(int)

    for p in participants:
        if p not in participant_dict:
            participant_dict[p] = 1
        else:
            participant_dict[p] += 1 # 동명이인이 존재 할 수 있음
    
    return participant_dict

# 마라톤을 완주하지 못한 참가자
def find_give_up_member(participants, finisher):
    for f in finisher:
        if f in participants:
            participants[f] -= 1 # 마라톤 완주

    for p in participants:
        if participants[p] == 1: # 완주를 못한 참가자
            return p


# main
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 참가자의 수
    participant = [sys.stdin.readline().rstrip() for _ in range(N)] # 참가자 명단
    finisher = [sys.stdin.readline().rstrip() for _ in range(N-1)] # 완주자 명단
    res = find_give_up_member(marathon_participants(participant), finisher)
    print(res)