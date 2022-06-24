import sys

list_password, answer = [], []
vowels = ['a', 'e', 'i', 'o', 'u']

while True:  # 입력 받기
    inp = sys.stdin.readline().strip()
    list_password.append(inp)

    if inp == 'end':
        break


def checkCondition1(password):
    if not set(password).intersection(password, vowels):
        return False


def checkCondition2(password):
    cntV, cntC = 0, 0  # 연속된 모음, 자음 개수

    for p in password:
        if p in vowels:  # 모음
            cntV += 1
            if cntC > 0:
                cntC = 0
        else:  # 자음
            cntC += 1
            if cntV > 0:
                cntV = 0

        if cntV == 3 or cntC == 3:
            return False


def checkCondition3(password):
    prev = password[0]
    for p in password[1:]:
        if p == prev:  # 같은 글자가 연속적으로 위치
            if (p == 'e' and prev == 'e' or p == 'o' and prev == 'o'):
                continue  # ee, oo 허용
            else:
                return False
        else:
            prev = p


def addMessage(password, flag):  # 체크한 비밀번호에 대한 판별
    if flag == True:
        msg = f'<{password}> is acceptable.'
    else:
        msg = f'<{password}> is not acceptable.'

    answer.append(msg)


for password in list_password[:-1]:  # 입력받은 비밀번호에 대한 품질 체크
    flag = True

    if checkCondition1(password) == False:
        flag = False
    elif checkCondition2(password) == False:
        flag = False
    elif checkCondition3(password) == False:
        flag = False

    addMessage(password, flag)  # 적합한 비밀번호

print(*answer, sep='\n')
