from typing import List

'''
MEDIUM

You are given a 0-indexed m x n binary matrix mat and an integer cols, which denotes the number of columns you must choose.

A row is covered by a set of columns if each cell in the row that has a value of 1 also lies in one of the columns of the chosen set.

Return the maximum number of rows that can be covered by a set of cols columns.



Example 1:



Input: mat = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], cols = 2
Output: 3
Explanation:
As shown in the diagram above, one possible way of covering 3 rows is by selecting the 0th and 2nd columns.
It can be shown that no more than 3 rows can be covered, so we return 3.
Example 2:



Input: mat = [[1],[0]], cols = 1
Output: 2
Explanation:
Selecting the only column will result in both rows being covered, since the entire matrix is selected.
Therefore, we return 2.


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 12
mat[i][j] is either 0 or 1.
1 <= cols <= n
'''


class Solution:
    # TODO return and solve it!
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        if len(mat[0]) == cols:
            return len(mat)

        m, n = len(mat), len(mat[0])
        counter = {}
        for i in range(n):
            counter[i] = set()

        zeros = 0
        for irow in range(m):
            row = mat[irow]
            if all(cell == 0 for cell in row):
                zeros += 1
            else:
                for icell in range(n):
                    if row[icell] == 1:
                        counter[icell].add(irow)

        for sval in counter.values():
            pass

        print(zeros, counter)
