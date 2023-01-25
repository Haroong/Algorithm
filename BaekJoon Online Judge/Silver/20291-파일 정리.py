import sys
from collections import defaultdict

# 파일을 확장자 별로 딕셔너리에 정리
def clean_up_files(files):
    extensions = defaultdict(int)

    for file in files:
        extension = file.split('.')[1]
        if extension not in extensions:
            extensions[extension] = 1
        else:
            extensions[extension] += 1

    return extensions

# 파일 이름, 개수 출력
def print_answer(tuple):
    for t in tuple:
        print(t[0], t[1])

# main
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 파일의 개수
    files = [sys.stdin.readline().rstrip() for _ in range(N)] # 파일 이름
    result = clean_up_files(files) # 확장자 별로 정리
    answer = sorted(result.items()) # 사전 순으로 정렬
    print_answer(answer)