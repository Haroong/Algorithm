def maxArea(height):
    answer = 0

    # set list index(two pointer)
    start, end = 0, len(height)-1

    # calculate maximum water container
    while start < end:
        answer = max(answer, (end - start) * min(height[start], height[end]))

        # check height
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1

    return answer
