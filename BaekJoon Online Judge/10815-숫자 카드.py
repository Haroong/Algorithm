n = int(input())  # 보유한 숫자 카드의 개수
list_card = list(map(int, input().split()))  # 숫자 카드에 적힌 정수
m = int(input())
list_checker = list(map(int, input().split()))  # 판별해야 할 리스트 정수
set_checker = set(list_checker.copy())  # 판별해야 할 집합 정수

answer = []
isOwn = set_checker.intersection(list_card)

for card in list_checker:
    if card in isOwn:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)
