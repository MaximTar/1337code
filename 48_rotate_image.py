from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        # reverse rows
        for i in range(size):
            matrix[i], matrix[size - i - 1] = matrix[size - i - 1], matrix[i]
        # or just matrix.reverse()
        # transpose
        for i in range(size):
            for j in range(i, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
