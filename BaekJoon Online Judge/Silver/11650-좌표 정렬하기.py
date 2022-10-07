# get input
n = int(input())
coords = [list(map(int, input().split())) for _ in range(n)]

# sorting
coords.sort()

# print answer
for coord in coords:
    print(*coord)
