#!/usr/bin/python3

"""Given a m x n matrix mat and an integer k,
return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.

"""

class  Solution():
    def  matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])

        prefixSum = [[0] * (n+1) for _ in range(m + 1)]


        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefixSum[i][j] = mat[i - 1][j - 1]  + prefixSum[i-1][j] + prefixSum[i][j - 1] - prefixSum[i - 1] [j -1]

            answer = [[0] * (n) for _ in range(m)]

            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    end_i = min(m, i + k)
                    end_j = min(n, j + k)
                    start_i =  max(1, i - k)
                    start_j = max(1, j - k)

                    answer[i -1][j -1] = prefixSum[end_i][end_j]- prefixSum[start_i - 1][end_j] - prefixSum[end_i][start_j - 1]
                    + prefixSum[start_i - 1][start_j - 1]

        return answer
