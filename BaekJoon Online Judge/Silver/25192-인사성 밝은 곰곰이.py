import sys

def count_emoticon(logs):
    result = 0
    index = 1
    s = set()

    while True:
        if index == len(logs): # 마지막까지 집합에 추가된 길이만큼 더해줌
            result += len(s)
            break
        elif logs[index] == 'ENTER':
            result += len(s)
            index += 1
            s = set() # 집합 초기화
        else: 
            s.add(logs[index]) # 집합에 곰곰티콘을 사용한 사람 추가
            index += 1

    return result


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 채팅방 로그 개수
    chat_logs = [sys.stdin.readline().rstrip() for _ in range(N)]
    answer = count_emoticon(chat_logs)
    print(answer)