a, b, v = map(int, input().split())
answer = 0


def calculateDays(climb, slip, height):
    FIRST_DAY = 1
    step = - slip + climb  # 하루에 최종적으로 올라간 높이

    remainHeight = height - climb  # 첫째날 올라간 후 남은 높이

    if remainHeight % step == 0:
        day = remainHeight // step + FIRST_DAY  # 첫째날 일수 추가
    else:
        day = remainHeight // step + 1 + FIRST_DAY

    return day


answer = calculateDays(a, b, v)

print(answer)
