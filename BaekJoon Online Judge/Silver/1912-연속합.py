import sys

def get_maximum_sum_of_sub_array(sequence):
    current_max = -sys.maxsize
    result = -sys.maxsize

    for number in sequence:
        current_max = max(current_max + number, number) # 이전까지의 값을 더할지 말지 결정
        result = max(result, current_max) # 지금까지의 최댓값과 현재의 최댓값을 비교

    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip()) # 수열의 길이
    sequence = list(map(int, sys.stdin.readline().split())) # 수열의 원소
    answer = get_maximum_sum_of_sub_array(sequence)
    print(answer)