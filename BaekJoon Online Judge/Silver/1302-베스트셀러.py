n = int(input())
list_book = [input() for _ in range(n)]

dictionary = {}

for book in list_book:
    if book in dictionary:
        cnt = dictionary.get(book) + 1  # 판매 부수 증가
        dictionary[book] = cnt
    else:
        dictionary[book] = 1

bestSeller = [key for key, value in dictionary.items() if value ==
              max(dictionary.values())]  # 베스트셀러 찾기
bestSeller.sort()  # 오름차순 정렬

answer = bestSeller[0]

print(answer)
