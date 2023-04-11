import sys

def bubble_sort(elements, count):
    swap, loop = 0, 0

    while loop < len(elements) :
        for j in range(len(elements) - 1):
            if elements[j] > elements[j + 1]:
                temp = elements[j + 1]
                elements[j + 1] = elements[j]
                elements[j] = temp
                swap += 1

            if swap == count:
                return elements[j], elements[j + 1]
            
        loop += 1
    
    return -1

def print_answer(ret):
    if ret == -1:
        print(ret)
    else:
        print(*ret, sep=' ')

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split()) # 배열의 크기, 교환 횟수
    elements = list(map(int, sys.stdin.readline().split()))
    ret = bubble_sort(elements, K)
    print_answer(ret)