N = input()
num_list = [n for n in N[:]]
num_list.sort(reverse=True)

result = ''.join(num_list)

print(result)
