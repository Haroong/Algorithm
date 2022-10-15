from collections import defaultdict
import sys

answer = []

# tree dictionary
tree_dict = defaultdict(int)
tree_count = 0

# get input
while True:
    tree = sys.stdin.readline().rstrip()

    # no more input data
    if not tree:
        break

    # add data to dictionary
    if tree not in tree_dict:
        tree_dict[tree] = 1
    else:
        tree_dict[tree] += 1

    tree_count += 1

# sort data
tree_list = sorted(tree_dict.items())

# calculate percent
for tree in tree_list:
    key, value = tree[0], tree[1]
    ratio = format(value / tree_count * 100, '.4f')
    answer.append([key, ratio])

# print answer
for ans in answer:
    print(*ans)
