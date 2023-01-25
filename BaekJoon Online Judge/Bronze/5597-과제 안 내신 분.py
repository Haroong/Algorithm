import sys
from collections import defaultdict

def find_unsubmit_students(elements):
    result = []

    for number in range(1, 31):
        if number not in elements:
            result.append(number)
    
    return result


if __name__ == '__main__':
    attendance = defaultdict(bool)
    
    for _ in range(28):
        student_number = int(sys.stdin.readline().rstrip())
        attendance[student_number] = True
    
    answer = find_unsubmit_students(attendance)
    print(*answer, sep='\n')