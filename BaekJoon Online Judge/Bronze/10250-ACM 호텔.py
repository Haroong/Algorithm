import sys


def set_room_number(w, h):
    result = ''
    result += f'{h}'
    if w < 10:
        result += f'0{w}'
    else:
        result += f'{w}'

    return result


def assign_hotel_room(height, weight, nth):
    count = 0
    result = 0

    for w in range(1, weight + 1):
        for h in range(1, height + 1):
            count += 1
            if (count == nth):
                result = set_room_number(w, h)
                return result


if __name__ == '__main__':
    answer = []

    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        H, W, N = map(int, sys.stdin.readline().split())
        room = assign_hotel_room(H, W, N)
        answer.append(room)

    print(*answer, sep='\n')
