import sys
from collections import defaultdict

# 좋은 친구가 몇 명인지 반환
def count_good_friends(my_length, dictionary):
    count = 0

    if my_length in dictionary:
        count += dictionary[my_length]

    return count

# 좋은 친구 쌍 찾기
def find_good_friends(name_length, size):
    d = defaultdict(int)
    count = 0

    # 슬라이딩 윈도우를 이용하여 초기 값을 구한다
    for i in range(1, size + 1):
        if name_length[i] not in d:
            d[name_length[i]] = 1
        else:
            d[name_length[i]] += 1

    # 첫번째 학생의 이름 길이와 동일한 친구가 존재하는지 찾는다
    count += count_good_friends(name_length[0], d)

    # 나머지 학생들도 동일한 방법으로 좋은 친구 계산
    for j in range(1, len(name_length)):
        d[name_length[j]] -= 1 # 내 이름 빼기
        
        if j + size <= len(name_length) - 1:
            if name_length[j + size] in d:
                d[name_length[j + size]] += 1 # 딕셔너리에 있는 현재 키에 대한 값 1 증가
            else:
                d[name_length[j + size]] = 1 # 현재값 딕셔너리에 추가     

        # 현재 학생의 이름 길이와 동일한 친구가 존재하는지 찾는다
        count += count_good_friends(name_length[j], d)

    return count

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split()) # n명의 학생, 등수 차이

    name_length = [] # 각 학생의 이름 길이
    for _ in range(N):
        name = sys.stdin.readline().rstrip()
        name_length.append(len(name)) # 학생의 이름 길이를 리스트에 추가

    answer = find_good_friends(name_length, K)
    print(answer)