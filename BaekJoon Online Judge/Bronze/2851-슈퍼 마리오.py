import sys

MUSHROOMS = 10 # 버섯의 개수
TARGET_SCORE = 100 # 최대 점수

# 각 버섯의 점수
score = list(int(sys.stdin.readline().rstrip()) for _ in range(MUSHROOMS))

prev_sum = 0 # 이전 버섯까지의 점수 합계
prefix_sum = [] # 누적합 리스트
isCalculateCompleted = False

# 누적 점수 계산
for index, value in enumerate(score):
    prev_sum += value
    prefix_sum.append(prev_sum)

    if prefix_sum[-1] == TARGET_SCORE:
        print(TARGET_SCORE)
        isCalculateCompleted = True
        break
    elif prefix_sum[-1] > TARGET_SCORE:
        # 절댓값 비교
        prev_abs = abs(TARGET_SCORE - prefix_sum[-2])
        cur_abs = abs(TARGET_SCORE - prefix_sum[-1])

        if prev_abs == cur_abs:
            print(prefix_sum[-1]) # 더 큰 숫자로 출력
            isCalculateCompleted = True
            break
        elif prev_abs > cur_abs: # 절댓값이 더 작은 값으로 출력
            print(prefix_sum[-1])
            isCalculateCompleted = True
            break
        else:
            print(prefix_sum[-2])
            isCalculateCompleted = True
            break
    else:
        continue

# 모든 버섯을 다 먹음    
if isCalculateCompleted == False:
    print(prefix_sum[-1])