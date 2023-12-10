import sys


def set_shortcut_format(index, option, shortcut):
    result = ''

    for i, v in enumerate(option):
        if i == index:
            result += f'[{shortcut}]'
        else:
            result += v

    return result


def get_group_word_index(word, target):
    count = 0

    for index, value in enumerate(word):
        if target == count:
            return index
        if value == ' ':
            count += 1


def check_if_first_alphabet_can_shortcut(option):
    result = ''
    global shortcuts

    for index, value in enumerate(option.split()):  # 띄어쓰기로 분리
        v = value[0]
        if v != ' ' and v.upper() not in shortcuts:
            shortcuts.add(v.upper())
            result = set_shortcut_format(
                get_group_word_index(option, index), option, v)
            return result


def find_possible_shortcut_in_any_index(option):
    result = option
    global shortcuts

    for index, value in enumerate(option):
        for o in value:
            if o != ' ' and o.upper() not in shortcuts:
                shortcuts.add(o.upper())
                return set_shortcut_format(index, option, value)

    return result


def check_keyboard_shortcut(option):
    # 단어의 첫 글자로 단축키 지정이 가능한지 확인
    first_words = check_if_first_alphabet_can_shortcut(option)
    if first_words != None:
        return first_words

    # 전체 인덱스 내에서 단축키로 지정 가능한 알파벳이 존재하는지 확인
    return find_possible_shortcut_in_any_index(option)


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    shortcuts = set()  # 알파벳 대문자로 단축키 집합 저장
    answer = [check_keyboard_shortcut(
        sys.stdin.readline().rstrip()) for _ in range(N)]
    print(*answer, sep='\n')
