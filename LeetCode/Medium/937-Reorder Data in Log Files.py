from collections import deque


def reorderLogFiles(logs):
    # log list
    digitLog, letterLog = [], []

    # seperate logs
    for log in logs:
        if ''.join(log.split()[1:]).isnumeric():
            digitLog.append(log)
        else:
            letterLog.append(log)

    # sort letter
    letterLog = sorted(letterLog, key=lambda x: (
        x.split()[1:], x.split()[0]))

    # append digitLog to letterLog
    for d in digitLog:
        letterLog.append(d)

    return letterLog


reorderLogFiles(["j mo", "5 m w", "g 07", "o 2 0", "t q h"])
