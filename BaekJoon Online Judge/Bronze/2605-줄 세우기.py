import sys

def student_order(s, numbers):
    order = [i for i in range(1, s+1)]

    for index, value in enumerate(numbers):
        student = index + 1

        if value >= 1: # 1이상의 번호를 뽑으면 그 숫자만큼 앞으로 이동
            forward = index - value
            del order[index] # 이동하려는 위치에 있는 학생 제거
            order.insert(forward, student)

    return order


if __name__ == '__main__':
    students = int(sys.stdin.readline().rstrip()) # 학생의 수
    numbers = list(map(int, sys.stdin.readline().split())) # 학생들이 뽑은 번호
    result = student_order(students, numbers)
    print(*result, sep=' ')