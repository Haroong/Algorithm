import sys


# 중복으로 신청한 사람 삭제
def remove_duplicate(students):
    waiting_list = dict()

    for student in students:
        if student not in waiting_list:
            waiting_list[student] = True
        else:
            waiting_list.pop(student) # 이전에 신청한 내역 삭제
            waiting_list[student] = True

    return waiting_list


# 수강 신청이 승인된 학생 목록
def registered_list(waiting_list, fixed_number):
    count = 0

    for w in waiting_list:
        if count == fixed_number: # 인원 마감
            break

        count += 1
        print(w)

# main
if __name__ == '__main__':
    K, L = map(int, sys.stdin.readline().split()) # 수강 가능 인원, 대기 목록 길이
    students = [sys.stdin.readline().rstrip() for _ in range(L)] # 수강 신청한 학생 목록
    registered_list(remove_duplicate(students), K) # 최종으로 수강 신청이 승인된 학생들