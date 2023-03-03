import sys
from collections import deque

# 간식 수령 가능 여부 반환
def is_able_to_receive_snack(tickets):
    stack = deque() # 원소 하나만 들어갈 수 있음
    snack_receive = []

    for ticket in tickets:
        if snack_receive and snack_receive[-1] == ticket - 1:
            snack_receive.append(ticket)
        else:
            if stack and stack[-1] < ticket: # 현재 번호표 숫자가 더 큼
                while stack and stack[-1] < ticket:
                    snack_receive.append(stack.pop())

                    if len(snack_receive) >= 2:
                        if snack_receive[-2] != snack_receive[-1] - 1: # 간식 순서는 번호표 순서대로
                            return False
            
            stack.append(ticket)

    return True

# 정답 형식 출력
def print_answer(res):
    if res == True:
        print('Nice')
    else:
        print('Sad')

# main
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 앞에 서 있는 학생들의 수
    ticker_number = list(map(int, sys.stdin.readline().split())) # 번호표 순서
    result = is_able_to_receive_snack(ticker_number)
    print_answer(result)