import sys
import copy
import time

N = int(sys.stdin.readline().rstrip()) # 사용 가능한 문자의 개수
rome_str = [] # 생성된 로마 숫자
string_result = []

ROME_NUMBER = ['I', 'V', 'X', 'L']


# 로마 숫자 문자열 생성
def create_rome_string(depth, start):
    if depth == N:
        string_result.append(copy.deepcopy(rome_str))
        return
        
    for i in range(start, 4):
        rome_str.append(ROME_NUMBER[i])
        create_rome_string(depth+1, i)
        rome_str.pop()


# 문자열 계산
def calculate_rome_number():
    answer = set()

    for i in range(len(string_result)):
        temp_sum = 0

        for s in string_result[i]:
            if s == 'I':
                temp_sum += 1
            elif s == 'V':
                temp_sum += 5
            elif s == 'X':
                temp_sum += 10
            else:
                temp_sum += 50
        
        answer.add(temp_sum)
    
    count = len(answer)

    return count
        

if __name__ == '__main__':
    create_rome_string(0, 0)
    count = calculate_rome_number()
    print(count) # 정답 출력