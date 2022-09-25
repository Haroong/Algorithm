import itertools

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        originRow, originCol = len(mat), len(mat[0])

        if originRow * originCol != r * c:
            return mat
        else:
            # row traverse in matrix order
            numList = list(itertools.chain(*mat))

            idx, temp, answer = 0, [], []

            # add numbers to r * c matrix
            for _ in range(r):
                for _ in range(c):
                    temp.append(numList[idx])
                    idx += 1
                answer.append(temp)
                temp = [] # reset temp list

            return answer
