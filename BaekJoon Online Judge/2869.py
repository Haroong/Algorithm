a, b, v = map(int, input().split())
answer = 0


def calculateDays(climb, slip, height):
    FIRST_DAY = 1
    step = - slip + climb  # 하루에 최종적으로 올라간 높이

    remainHeight = height - climb  # 첫째날 올라간 후 남은 높이

    if remainHeight % step == 0:
        day = remainHeight // step + FIRST_DAY
    else:
        day = remainHeight // step + 1 + FIRST_DAY  # 소요 일수 하루 추가

    return day


answer = calculateDays(a, b, v)

print(answer)
