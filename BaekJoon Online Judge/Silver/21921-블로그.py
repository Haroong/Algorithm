import sys

def max_blog_visitors(stats, streak_day):
    count = 1 # 방문자가 최대로 많았던 기간 횟수
    streak_sum = sum(stats[:streak_day])
    blog_visitor_stats = streak_sum

    for i in range(streak_day, len(stats)):
        streak_sum += stats[i] - stats[i-streak_day]

        if streak_sum > blog_visitor_stats:
            blog_visitor_stats = streak_sum
            count = 1 
        elif  streak_sum == blog_visitor_stats:
            count += 1
    
    return blog_visitor_stats, count


def print_answer(res):
    max_visitors = res[0] # x일 동안 가장 많이 들어온 방문자 수
    count = res[1] # 최대 방문자 수의 기간
    
    if max_visitors == 0:
        print('SAD')
    else:
        print(max_visitors)
        print(count)


if __name__ == '__main__':
    N, X = map(int, sys.stdin.readline().split()) # 블로그 운영 일 수, 연속된 일자
    stats = list(map(int, sys.stdin.readline().split())) # 하루 방문자 수
    result = max_blog_visitors(stats, X)
    print_answer(result)