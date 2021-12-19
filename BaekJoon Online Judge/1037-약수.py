n = input()
divisor = list(map(int, input().split()))
divisor.sort()

min = divisor[0]
max = divisor[-1]

print(min * max)
