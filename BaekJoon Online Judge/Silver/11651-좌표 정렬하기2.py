# get input
n = int(input())
coords = [list(map(int, input().split())) for _ in range(n)]

# sorting
coords_sort = sorted(coords, key=lambda y: (y[1], y[0]))

# print answer
for coord in coords_sort:
    print(*coord)
