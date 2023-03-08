import sys

RYAN = 1

# 라이언 인형이 위치한 인덱스를 저장한다
def set_ryan_index(dolls):
    ryan_index_list = []

    for index, value in enumerate(dolls):
        if value == RYAN:
            ryan_index_list.append(index)

    return ryan_index_list

# k개 이상의 라이언이 포함된 연속된 인형 개수의 최소값 반환
def smallest_streak_dolls(index_list, k):
    count = sys.maxsize

    for i in range(k - 1, len(index_list)):
        right = index_list[i]
        left = index_list[i - k + 1]
        count = min(count, right - left + 1)
    
    return count

# 정답 형식 출력
def print_answer(res):
    if res == sys.maxsize:
        print(-1)
    else:
        print(res)

# main
if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split()) # 전체 인형의 개수, 최소로 필요한 라이언 인형 개수
    kakao_dolls = list(map(int, sys.stdin.readline().split())) # 인형 배치 상태
    ryan_index = set_ryan_index(kakao_dolls) # 라이언 인형의 인덱스 저장
    answer = smallest_streak_dolls(ryan_index, K)
    print_answer(answer)