import sys

# 모든 사람에게 같은 길이의 과자 분배
def divide_snack(snacks, people):
    start = 1
    end = snacks[-1]
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        given_count = 0 # 과자를 받은 사람의 수

        if mid == 0:
            return end

        # mid 길이만큼 과자 나누기
        for snack in snacks:
            if snack >= mid:
                given_count += snack // mid

        if given_count < people: # 목표한 인원만큼 나눠줬거나 과자가 부족한 경우
            end = mid - 1
        else:
            answer = mid # 과자가 남은 경우
            start = mid + 1

    return answer

# main
if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split()) # 사람의 수, 막대 과자의 수
    snacks = sorted(list(map(int, sys.stdin.readline().split()))) # 막대 과자의 길이
    answer = divide_snack(snacks, M)
    print(answer)