import sys
from collections import defaultdict

# 각 번호의 첫 번째 값을 키로 갖는 딕셔너리 생성
def seperate_by_first_digit(numbers):
    num_dict = defaultdict(int)

    for n in numbers:
        first_digit = n[0] # 번호의 첫 번째 숫자로 값을 구분하여 딕셔너리에 추가
        if not num_dict[first_digit]:
            num_dict[first_digit] = [n]
        else:
            num_dict[first_digit] += [n]

    return num_dict


# 일관성 있는 전화번호 목록인지 여부 반환
def is_consistent_list(number_list, dictionary):
    for number in number_list:
        first_digit = number[0]

        for registered_number in dictionary[first_digit]: # 전화번호부 탐색
            if number != registered_number and registered_number == number[:len(registered_number)]: # 기존에 등록된 번호와 현재 번호가 겹침
                return 'NO'
            
    
    return 'YES'



# main
if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip()) # 테스트 케이스의 수
    answer =[] # 각 테스트 케이스에 대한 정답

    for _ in range(t):
        n = int(sys.stdin.readline().rstrip()) # 전화번호의 수
        phone_numbers = [sys.stdin.readline().rstrip() for _ in range(n)]  # 전화번호 목록
        digit_dictionary = seperate_by_first_digit(phone_numbers)
        result = is_consistent_list(phone_numbers, digit_dictionary)
        answer.append(result)

    print(*answer, sep='\n')