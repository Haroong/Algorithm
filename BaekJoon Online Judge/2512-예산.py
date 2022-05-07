n = int(input())
list_budget = list(map(int, input().split()))
maximum = int(input())

min = maximum // n  # 최소로 지급 가능한 예산

while True:
    list_budget_copy = list_budget.copy()

    for i in range(n):
        if list_budget_copy[i] > min:
            list_budget_copy[i] = min

    if sum(list_budget_copy) > maximum:  # 예산 초과
        print(min - 1)
        break
    elif sum(list_budget_copy) == maximum:  # 최대 지급 가능
        print(min)
        break
    else:
        if (max(list_budget)) == min:
            print(min)
            break
        else:
            min += 1
