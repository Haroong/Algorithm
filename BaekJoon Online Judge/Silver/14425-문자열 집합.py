n, m = map(int, input().split())
input_string = set(input() for _ in range(n))  # 집합에 포함된 문자열
check_string = list(input() for _ in range(m))  # 검사해야 할 문자열

count = 0

for str in check_string:
    if str in input_string:
        count += 1

print(count)
