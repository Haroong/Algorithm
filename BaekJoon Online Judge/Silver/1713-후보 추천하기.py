import sys
from collections import defaultdict

# 현재 후보를 사진틀에 신규로 게시 가능한지 여부 반환
def is_able_to_add_frame(limit):
    if len(frames) < limit:
        return True
    else:
        return False

# 현재 후보가 이미 게시된 상태인지 여부 반환
def is_candidate_exists_in_photo_frame(candidate):
    if candidate in frames:
        return True
    else:
        return False

# 추천수가 가장 작은 횟수를 반환
def get_count_of_least_recommendation():
    count = MAX_RECOMMENDATION

    for key, value in frames.items():
        count =  min(count, value)

    return count

# 기존 사진틀의 후보자 중 한명을 제거하고 현재 후보자로 교체함
def replace_to_current_candidate(candidate):
    count = get_count_of_least_recommendation()

    for key, value in frames.items():
        if value == count:
            frames[candidate] = frames[key] # 현재 후보로 교체
            del frames[key]
            break
        
# 사진틀에 게시될 최종 후보 리스트를 반환한다
def get_final_candidates(n, candidates):
    for candidate in candidates:
        if is_candidate_exists_in_photo_frame(candidate):
            frames[candidate] += 1 # 추천 수 1 증가
        else:
            if is_able_to_add_frame(n): # 사진틀에 현재 후보를 추가 가능
                frames[candidate] = 1
            else:
                replace_to_current_candidate(candidate)
    
    return sorted(frames.keys())

# main
if __name__ == '__main__':
    frames = defaultdict(int) # 후보 이름, 추천 수를 저장하는 딕셔너리
    MAX_RECOMMENDATION = 1000

    N = int(sys.stdin.readline().rstrip()) # 사진틀의 개수
    M = int(sys.stdin.readline().rstrip()) # 총 추천 횟수
    recommendation_order = list(map(int, sys.stdin.readline().split())) # 추천받은 후보 순서
    ret = get_final_candidates(N, recommendation_order)
    print(*ret, sep=' ')