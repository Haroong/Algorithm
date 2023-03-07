import sys
from collections import defaultdict

# 회전 초밥이기 때문에 앞의 초밥들을 뒤에 추가해줌
def convert_to_circular_sushi(sushi, k):
    added_sushi = sushi
    added_sushi.extend(sushi[0:k-1])
    
    return added_sushi

# 쿠폰 초밥이 딕셔너리 키에 존재하는지 여부 반환
def is_coupon_in_dictionary(dictionary, coupon):
    if coupon in dictionary:
        return True
    else:
        return False

# 딕셔너리의 값이 0인 키를 제거한다
def remove_empty_key(dictionary):
    return {key: value for key, value in dictionary.items() if value != 0}


# 최대로 먹을 수 있는 초밥 종류의 개수 반환
def count_max_sushi_types(sushi, streak, coupon):
    count = 0
    sushi_types = defaultdict(int) # 초밥 종류

    
    # 맨 처음에 연속으로 먹는 초밥 종류 확인
    for i in range(0, streak):
        if i == len(sushi):
            break

        if sushi[i] in sushi_types:
            sushi_types[sushi[i]] += 1
        else:
            sushi_types[sushi[i]] = 1
        
    if is_coupon_in_dictionary(sushi_types, coupon):
        count = max(count, len(sushi_types.keys()))
    else:
        count = max(count, len(sushi_types.keys()) + 1) # 쿠폰 초밥을 서비스로 제공

    if streak < len(sushi): # 더 먹을 수 있는 초밥이 존재하면
        # 나머지 초밥들을 슬라이딩 윈도우로 체크
        for j in range(streak, len(sushi)):
            sushi_types[sushi[j - streak]] -= 1
            
            if sushi[j] in sushi_types:
                sushi_types[sushi[j]] += 1
            else:
                sushi_types[sushi[j]] = 1

            sushi_types = remove_empty_key(sushi_types) # 값인 0인 키 제거

            if is_coupon_in_dictionary(sushi_types, coupon):
                count = max(count, len(sushi_types.keys()))
            else:
                count = max(count, len(sushi_types.keys()) + 1) # 쿠폰 초밥을 서비스로 제공

    return count

# main
if __name__ == '__main__':
    N, d, k, c = map(int, sys.stdin.readline().split()) # 접시의 개수, 초밥 종류 개수, 연속해서 먹는 접시 개수, 쿠폰 접시 번호
    sushi = [int(sys.stdin.readline().rstrip()) for _ in range(N)] # 회전 초밥
    sushi = convert_to_circular_sushi(sushi, k)
    answer = count_max_sushi_types(sushi, k, c) # 최대로 먹을 수 있는 초밥 종류 개수
    print(answer)