import sys

# 최소의 길이로 줄일 수 있는 길이 반환
def find_shortest_length(numbers):
    unique_number = len(numbers)

    for i in range(1, unique_number + 1):
        s = set() # 길이를 자른 학번 목록을 집합에 저장
        
        for j in range(unique_number):
            splitted_number = numbers[j][-i::]
            s.add(splitted_number) # 특정 길이만큼 뒤에서부터 잘라서 집합에 add
            if len(s) < j: # 중복된 숫자가 존재해서 집합에 추가되지 못함
                break
        
        if len(s) == unique_number:
            return i
    
    return len(numbers[0])

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 학생의 수
    student_number = [sys.stdin.readline().rstrip() for _ in range(N)] # 학번 목록
    answer = find_shortest_length(sorted(student_number, key=lambda x:x[-1]))
    print(answer)