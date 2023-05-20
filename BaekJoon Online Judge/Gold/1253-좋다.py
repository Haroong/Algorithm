import sys

# 투 포인터의 탐색 시작/종료 인덱스를 설정한다
def set_two_pointer_index(current_index, total_length):
    start, end = 0, len(numbers) - 1

    if current_index == 0: # 첫번째 숫자
        start = 1
    elif current_index == total_length: # 마지막 숫자
        end = total_length - 1

    return start, end

# 좋은 숫자 개수 찾기
def count_good_numbers(numbers):
    result = 0

    # 각 숫자에 대해 좋은 수인지 판별   
    for index, value in enumerate(numbers): 
        start, end = set_two_pointer_index(index, len(numbers) - 1)

        while start < end:
            if start == index: # 시작 인덱스와 현재 인덱스가 일치
                start += 1
                if start == end: break

            if end == index: # 종료 인덱스와 현재 인덱스가 일치
                end -= 1
                if end == start: break

            if numbers[start] + numbers[end] == value:
                result += 1
                break
            elif numbers[start] + numbers[end] > value:
                end -= 1
            else:
                start += 1

    return  result


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 수의 개수
    numbers = sorted(list(map(int, sys.stdin.readline().split()))) # 숫자 리스트
    answer = count_good_numbers(numbers)
    print(answer)