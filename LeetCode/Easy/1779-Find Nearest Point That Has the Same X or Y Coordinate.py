def nearestValidPoint(x, y, points):
    valid_point = []

    # filter points
    for idx, val in enumerate(points):
        if x == val[0] or y == val[1]:
            valid_point.append([val, idx])

    # valid point not exists
    if not valid_point:
        return -1

    # calculate manhattan distance
    manhattan_dist = []
    for p in valid_point:
        manhattan_dist.append([abs(x - p[0][0]) + abs(y - p[0][1]), p[1]])

    # get smallest index value
    answer = sorted(manhattan_dist, key=lambda idx: (idx[0], idx[1]))
    return answer[0][1]
