def arrayPairSum(nums):
    pair = []
    answer = 0

    # sort ascending order
    nums.sort()

    # get minimum pair value
    for num in nums:
        pair.append(num)

        # pair completed
        if len(pair) == 2:
            answer += min(pair)
            pair = []

    return answer
