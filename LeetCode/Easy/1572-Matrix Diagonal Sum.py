def diagonalSum(mat):
    answer = 0
    n = len(mat)
    mid = n // 2
    center = mat[mid][mid]

    for i in range(n):
        # primary diagonal
        answer += mat[i][i]

        # secondary diagonal
        answer += mat[i][n-1-i]

    # odd length
    if n % 2 == 1:
        answer -= center

    return answer
