import sys

# 삭제 처리된 난쟁이들 제거
def remove_fake_dwarfs(dwarfs):
    return [d for d in dwarfs if d != -1]

# 일곱 명의 진짜 난쟁이들을 찾는다
def find_real_dwarfs(dwarfs):
    result = dwarfs
    total_sum = sum(dwarfs)

    for i, v1 in enumerate(dwarfs):
        rm_first = total_sum - v1 # 현재 난쟁이를 가짜라고 가정

        for j, v2 in enumerate(dwarfs):
            if j != i and rm_first - v2 == 100:
                result[i] = -1 # 삭제 처리
                result[j] = -1
                return remove_fake_dwarfs(result)

# main
if __name__ == '__main__':
    dwarfs = [int(sys.stdin.readline().rstrip()) for _ in range(9)] # 아홉 난쟁이의 모자에 쓰인 숫자
    res = find_real_dwarfs(dwarfs)
    print(*res, sep='\n')