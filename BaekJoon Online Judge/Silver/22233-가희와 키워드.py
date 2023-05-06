import sys

def get_notepad_keyword_after_posting(total_keyword, posted_keyword):
    for word in posted_keyword:
        if word in total_keyword:
            total_keyword.remove(word)

    result = len(total_keyword)

    return result

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split()) # 메모장에 있는 키워드 개수, 블로그에 작성한 포스팅 개수
    total_keyword = set([sys.stdin.readline().rstrip() for _ in range(N)])
    answer = []

    for _ in range(M):
        posted_keyword = list(sys.stdin.readline().rstrip().split(','))
        answer.append(get_notepad_keyword_after_posting(total_keyword, posted_keyword))

    print(*answer, sep='\n')