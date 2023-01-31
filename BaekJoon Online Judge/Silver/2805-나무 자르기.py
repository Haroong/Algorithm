import sys

# 필요한 길이만큼 절단할 수 있도록 절단기의 최대 높이를 설정
def cutting_trees(trees, target):
    start = 0 # 절단기 최소 높이
    end = max(trees) # 절단기 최대 높이
    result = 0

    while start <= end:
        count = 0 # 잘라낸 나무의 길이
        cutter_height = (start + end) // 2

        # 전체 나무 탐색
        for tree in trees:
            if tree > cutter_height: # 자를 수 있는 나무 발견
                cut_length = tree - cutter_height # 나무 베기
                count += cut_length
        if count == target:
            return cutter_height
        elif count > target: # 필요한 나무의 길이보다 초과됨
            start = cutter_height + 1 # 절단기 높이 1 증가
            result = cutter_height
        else:
            end = cutter_height - 1 # 절단기 높이 1 감소

    return result

# main
if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split()) # 나무 그루, 필요한 나무의 길이
    trees = sorted(list(map(int, sys.stdin.readline().split()))) # 나무의 높이
    answer = cutting_trees(trees, m)
    print(answer)