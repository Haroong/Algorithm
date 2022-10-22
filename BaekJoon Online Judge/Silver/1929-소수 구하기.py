import sys
import math

m, n = map(int, sys.stdin.readline().split())

if m == 1:
    numbers = set([*range(m+1, n+1,1)]) # 1제외
else:
    numbers = set([*range(m, n+1,1)]) # n부터 m까지의 자연수
    
notPrimeNumber = set() # 소수가 아닌 수

# 에라토스테네스의 체 사용
for prime in range(2, int(math.sqrt(n))+1):
    for j in range(prime * 2, n+1, prime): # prime 수의 2배인 수들은 소수가 아님
        notPrimeNumber.add(j)

print(*(numbers - notPrimeNumber), sep='\n') # 차집합