import sys

# number가 한 자리 수인지 여부 반환
def is_one_digit(number):
    if number < 10:
        return True
    else:
        return False

# number가 두 자리 수인지 여부 반환
def is_two_digits(number):
    if number > 9:
        return True
    else:
        return False

# 원래 숫자와 동일한지 확인
def is_equal_to_original_number(generated, original):
    if generated == original:
        return True
    else:
        return False

# 더하기 사이클의 길이를 반환한다
def length_of_plus_cycle(original_number):
    count = 1
    number = original_number

    while True:
        if is_one_digit(number):
            left = 0

        left, right = number // 10, number % 10
        temp_sum = left + right

        if is_two_digits(temp_sum): # 두 자리 수인지 확인
            new_right = temp_sum % 10
            number = int(f'{right}{new_right}')     
        else:
            number = int(f'{right}{temp_sum}')     
        
        if is_equal_to_original_number(number, original_number): 
            return count
        
        count += 1

if __name__== '__main__':
    N = int(sys.stdin.readline().rstrip())
    answer = length_of_plus_cycle(N)
    print(answer)