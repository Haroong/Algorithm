def containsNearbyDuplicate(nums, k):
    dict = {}

     # add index, number to dictionary
    for index, value in enumerate(nums):
        if value not in dict:
            dict[value] = [index]
        else:
            if index - dict[value][-1] <= k:
                return True
            if index - dict[value][-1] > k: # 계산 범위 초과
                dict[value] += [index] # 현재 인덱스를 딕셔너리 값에 추가
                continue

    return False