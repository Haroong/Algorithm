from collections import defaultdict


def twoSum(nums, target):
    num_dict = dict()

    # check if subtract value in dictionary
    for index, num in enumerate(nums):
        need_number = target - num

        if need_number in num_dict:
            return [num_dict[need_number], index]
        else:
            num_dict[num] = index
