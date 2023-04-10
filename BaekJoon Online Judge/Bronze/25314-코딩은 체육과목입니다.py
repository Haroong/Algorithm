import sys

def get_integer_data_structure_name(n):
    bytes_name = []
    count = n // 4
    for _ in range(count):
        bytes_name.append('long')

    bytes_name.append('int')

    return ' '.join(bytes_name)    

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    answer = get_integer_data_structure_name(N)
    print(answer)