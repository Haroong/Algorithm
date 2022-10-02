import re


def mostCommonWord(paragraph, banned):
    # dictionary
    wordDict = dict()

    # remove punctuation
    word = [w for w in re.sub(
        r'[\W]', ' ', paragraph).lower().split() if not w in banned]

    # count paragraph word except banned word
    for w in word:
        if w not in wordDict:
            wordDict[w] = 1
        else:
            wordDict[w] += 1  # increase count

    # sort dictionary by values
    wordDict = sorted(wordDict.items(), key=lambda x: x[1], reverse=True)

    return wordDict[0][0]
