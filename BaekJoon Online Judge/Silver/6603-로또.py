import sys

MAX_SELECT = 6
result, answer = [], []

# back tracking
def back_tracking(elements):
    if len(result) == MAX_SELECT: # 숫자 6개 선택 완료
        answer.append(result[:])
        return
    
    for e in elements:
        if not result or e not in result and e > result[-1]:
            result.append(e)
            back_tracking(elements)
            result.pop()


# 0이 입력될 때까지 반복
while True:
    inp = list(map(int, sys.stdin.readline().split()))
    k = inp[0]
    numbers = inp[1:]

    if k == 0: # 입력 종료
        break

    back_tracking(numbers)
    answer.append([]) # 현재 테스트 케이스 종료


# 정답 출력
for ans in answer[:-1]: # 마지막 줄 공백 제거
    print(*ans, sep=' ')