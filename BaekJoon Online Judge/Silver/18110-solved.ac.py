import sys


def round_number(number):
    if number - int(number) >= 0.5:
        return int(number) + 1
    else:
        return int(number)


def remove_extreme_values(numbers):
    removed = round_number(len(numbers) * 15 / 100)
    result = numbers[removed:len(numbers)-removed]

    return result


def get_question_difficulty(n, opinions):
    opinions = remove_extreme_values(opinions)
    result = round_number(sum(opinions) / len(opinions))

    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        answer = 0
    else:
        opinions = [int(sys.stdin.readline().rstrip()) for x in range(n)]
        answer = get_question_difficulty(n, sorted(opinions))
    print(answer)
