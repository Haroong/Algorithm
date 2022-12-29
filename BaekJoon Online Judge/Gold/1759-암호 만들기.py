import sys

# 입력 받기
L, C = map(int, sys.stdin.readline().split())
characters = sorted(sys.stdin.readline().split())

vowel = ['a', 'e', 'i', 'o', 'u']
result = []

# 최소 한 개의 모음이 존재하는지
def vowel_condition():
    if any(v in vowel for v in result):
        return True
    
# 최소 두 개 이상의 자음이 존재하는지
def consonant_condition():
    count = 0

    for r in result:
        if r not in vowel:
            count += 1
        
    if count >= 2:
        return True


# 비밀번호 후보 찾기
def find_password():
    if len(result) == L:
        if vowel_condition() and consonant_condition():
            print(''.join(result))
        return
    
    for c in characters:
        if not result or c not in result and c > result[-1]:
            result.append(c)
            find_password()
            result.pop()


find_password()