def maximumDifference(nums):
    min_num, gap = nums[0], -1

    for i in range(1, len(nums)):
        if nums[i] <= min_num:
            min_num = nums[i]
            continue

        gap = max(gap, nums[i] - min_num)

    return gap


maximumDifference([26, 126, 4])
