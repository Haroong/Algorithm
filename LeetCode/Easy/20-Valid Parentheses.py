def isValid(s):
    stack = []
    match_parentheses = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for i in s:
        if i not in match_parentheses:  # open parentheses
            stack.append(i)
        elif not stack or stack.pop() != match_parentheses[i]:
            return False

    # check if stack is emtpy
    if stack:
        return False
    else:
        return True
