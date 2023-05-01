import sys
from collections import deque, defaultdict

# 양방향 그래프 생성
def set_friendship_graph(total, friendship):
    result = [[] for _ in range(total + 1)]

    for a, b in friendship:
        result[a].append(b)
        result[b].append(a)

    return result

# 각 사람에 대한 케빈 베이컨의 수를 계산
def get_number_of_kevin_bacon(person, graph):
    queue = deque([person])
    visited = set({person})
    depth = 1
    result = 0

    while queue:
        loop = len(queue)

        for _ in range(loop):
            current = queue.popleft()
            
            for friend in graph[current]: # 현재 사람과 연결된 사람 탐색
                if friend not in visited and friend != person:
                    visited.add(friend)
                    queue.append(friend)
                    result += depth
        
        depth += 1

    return result

# 인싸 반환
def find_person_of_minimum_depth(dictionary):
    return sorted(dictionary.items(), key=lambda x:x[1])[0][0]

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split()) # 유저의 수, 친구 관계의 수
    friendship = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    graph = set_friendship_graph(N, friendship)
    friend_dictionary = defaultdict(int)
    
    for person in range(1, N + 1):
        friend_dictionary[person] = get_number_of_kevin_bacon(person, graph)

    answer = find_person_of_minimum_depth(friend_dictionary)
    print(answer)