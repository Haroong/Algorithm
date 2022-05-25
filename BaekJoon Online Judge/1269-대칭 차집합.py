a, b = map(int, input().split())
setA, setB = set(map(int, input().split())), set(map(int, input().split()))

count = 0
count += len(setA.symmetric_difference(setB))

print(count)
