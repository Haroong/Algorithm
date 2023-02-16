import sys

def count_unique_substring(str):
    result = set()

    # 문자열의 길이만큼 반복
    for i in range(len(str)):
        for j in range(i, len(str)):
            result.add(str[i:j+1])

    return len(result)


if __name__ == '__main__':
    s = sys.stdin.readline().rstrip() # 문자열
    answer = count_unique_substring(s)
    print(answer)