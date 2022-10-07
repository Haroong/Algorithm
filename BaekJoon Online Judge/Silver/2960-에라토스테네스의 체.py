# get input
n, k = map(int, input().split())
num_list = list(range(2, n + 1))
count = 0

while count < k:
    p = num_list[0]
    count += 1
    if count == k:
        print(p)
        break
    num_list.remove(p)

    for next_num in num_list:
        if next_num % p == 0:
            count += 1
            if count == k:
                print(next_num)
                break
            num_list.remove(next_num)
