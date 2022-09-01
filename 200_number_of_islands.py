from typing import List


class Solution:
    # is it breadth or depth first search?
    def numIslands(self, grid: List[List[str]]) -> int:

        grid_length, row_length = len(grid), len(grid[0])

        def xfs(q):
            if q:
                n, i = q.pop()
                grid[n][i] = "0"
                if n < grid_length - 1 and grid[n + 1][i] == "1":
                    q.append([n + 1, i])
                if i < row_length - 1 and grid[n][i + 1] == "1":
                    q.append([n, i + 1])
                if n > 0 and grid[n - 1][i] == "1":
                    q.append([n - 1, i])
                if i > 0 and grid[n][i - 1] == "1":
                    q.append([n, i - 1])
                xfs(q)

        queue = []

        counter = 0
        for row_number in range(grid_length):
            for row_idx in range(row_length):
                if grid[row_number][row_idx] == "1":
                    counter += 1
                    queue.append([row_number, row_idx])
                    xfs(queue)

        return counter
