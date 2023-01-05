import sys

N = int(sys.stdin.readline().rstrip())
numbers = [x for x in range(1, N+1)]
result = []

def back_tracking():
    if len(result) == N:
        print(*result, sep=' ')
        return
    
    for i in range(N):
        if numbers[i] not in result:
            result.append(numbers[i])
            back_tracking()
            result.pop()

back_tracking()