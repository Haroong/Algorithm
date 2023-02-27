import sys

# 부분 문자열에 대해서 알파벳 종류별로 개수를 계산한다
def count_substring_alphabet(substring):
    alphabet = [0] * 4

    for s in substring:
        if s == 'A':
            alphabet[0] += 1
        elif s == 'C':
            alphabet[1] += 1
        elif s == 'G':
            alphabet[2] += 1
        else:
            alphabet[3] += 1
    
    return alphabet

# 각 알파벳의 최소 개수를 만족하는지 확인한다
def is_acceptable(alphabet_count, constraints):
    if alphabet_count[0] >= constraints[0] and alphabet_count[1] >= constraints[1] and alphabet_count[2] >= constraints[2] and alphabet_count[3] >= constraints[3]:
        return True
    else:
        return False

# 리스트에서 str에 해당하는 값을 뺀다
def subtract_element(counting_list, str):
    if str == 'A':
        counting_list[0] -= 1
    elif str == 'C':
        counting_list[1] -= 1
    elif str == 'G':
        counting_list[2] -= 1
    else:
        counting_list[3] -= 1

    return counting_list 

# 리스트에서 str에 해당하는 값을 더한다
def add_element(counting_list, str):
    if str == 'A':
        counting_list[0] += 1
    elif str == 'C':
        counting_list[1] += 1
    elif str == 'G':
        counting_list[2] += 1
    else:
        counting_list[3] += 1

    return counting_list 

# 생성 가능한 비밀번호 개수 반환
def get_password_count(DNA, size, constraints):
    result = 0

    counting_list = count_substring_alphabet(DNA[:size]) # 초기 슬라이딩 윈도우 사이즈의 결과
    if is_acceptable(counting_list, constraints):
        result += 1

    for i in range(size, len(DNA)):
        counting_list = subtract_element(counting_list, DNA[i - size]) # 슬라이딩 윈도우의 맨 첫번째 값 빼기
        counting_list = add_element(counting_list, DNA[i]) # 현재 값 더하기
        if is_acceptable(counting_list, constraints): # 비밀번호 생성 조건을 만족하는지 확인
            result += 1
    
    return result

# main
if __name__ == '__main__':
    S, P = map(int, sys.stdin.readline().split()) # DNA 문자열의 길이, 비번으로 사용할 부분 문자열의 길이
    DNA = sys.stdin.readline().rstrip() # 임의로 만든 DNA 문자열
    constraints = list(map(int, sys.stdin.readline().split())) # 비번에 필요한 최소 개수
    answer = get_password_count(DNA, P, constraints) # 생성 가능한 비밀번호 개수 찾기
    print(answer)