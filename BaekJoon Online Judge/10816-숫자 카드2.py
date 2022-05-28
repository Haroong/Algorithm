n = int(input())
list_card = list(map(int, input().split()))
m = int(input())
list_checker = list(map(int, input().split()))

dict = {}
answer = []

# 딕셔너리에 보유한 카드 개수 넣기
for card in list_card:
    if card in dict:
        count = dict.get(card)
        count += 1
        dict[card] = count
    else:
        dict[card] = 1

# 보유한 카드인지 판별
for card in list_checker:
    if card in dict:
        answer.append(dict.get(card))
    else:
        answer.append(0)

print(*answer)
