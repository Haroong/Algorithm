def containsDuplicate(nums):
    dict = {}

    # add numbers to dictionary
    for n in nums:
        if n not in dict:
            dict[n] = False
        else:
            dict[n] = True

    # check if dictionary contains True
    if True in dict.values():
        return True
    else:
        return False
