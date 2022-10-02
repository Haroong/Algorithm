def groupAnagrams(strs):
    # sort each element in alphabetical order
    word_list = [[s, ''.join(sorted(s))] for s in strs]

    # flip dictionary
    flipped = dict()
    for key, value in word_list:
        if not value in flipped:
            flipped[value] = [key]
        else:
            flipped[value] += [key]

    return flipped.values()


groupAnagrams(["", ""])
