import sys

# 왼쪽에서 보이는 트로피의 개수를 반환한다
def count_left_side(trophy):
    stack = []

    for t in trophy:
        if not stack or stack[-1] < t:
            stack.append(t)

    return len(stack)

# 오른쪽에서 보이는 트로피의 개수를 반환한다
def count_right_side(trophy):
    stack = []

    for t in trophy[::-1]:
        if not stack or stack[-1] < t:
            stack.append(t)

    return len(stack)

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 트로피의 개수
    trophy = [int(sys.stdin.readline().rstrip()) for _ in range(N)] # 트로피의 높이
    print(count_left_side(trophy))
    print(count_right_side(trophy))