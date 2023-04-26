import sys

def count_armor(required, materials):
    result = 0
    set_materials = set(materials)

    for material in materials:
        need = required - material
        if need in set_materials and need != material:
            result += 1
            set_materials.remove(need)
            set_materials.remove(material)

    return result

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip()) # 재료 개수
    M = int(sys.stdin.readline().rstrip()) # 갑옷 제작에 필요한 재료의 합
    materials = list(map(int, sys.stdin.readline().split())) # 재료의 고유 값
    answer = count_armor(M, materials)
    print(answer)