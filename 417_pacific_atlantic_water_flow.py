from typing import List, Set, Tuple


class Solution:
    # 1, X first search, head-on
    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #
    #     heights_length, row_length = len(heights), len(heights[0])
    #     both_oceans_cells = []
    #
    #     def xfs(q, s, v):
    #         if q:
    #             n, i = q.pop()
    #             if (n, i) not in v:
    #                 if n == 0 or i == 0:
    #                     # s.add('p')  # pacific
    #                     s.add(1)  # pacific
    #                 if n == heights_length - 1 or i == row_length - 1:
    #                     # s.add('a')  # atlantic
    #                     s.add(2)  # atlantic
    #
    #                 # if ('p' in s and 'a' in s) or [n, i] in both_oceans_cells:
    #                 if (1 in s and 2 in s) or [n, i] in both_oceans_cells:
    #                     return True
    #
    #                 current_height = heights[n][i]
    #                 if n < heights_length - 1 and heights[n + 1][i] <= current_height:
    #                     q.add((n + 1, i))
    #                 if i < row_length - 1 and heights[n][i + 1] <= current_height:
    #                     q.add((n, i + 1))
    #                 if n > 0 and heights[n - 1][i] <= current_height:
    #                     q.add((n - 1, i))
    #                 if i > 0 and heights[n][i - 1] <= current_height:
    #                     q.add((n, i - 1))
    #                 visited.add((n, i))
    #             if xfs(q, s, v):
    #                 return True
    #             else:
    #                 return False
    #         else:
    #             return False
    #
    #     for row_number in range(heights_length):
    #         for row_idx in range(row_length):
    #             status, visited, queue = set(), set(), set()
    #             queue.add((row_number, row_idx))
    #             if xfs(queue, status, visited):
    #                 both_oceans_cells.append([row_number, row_idx])
    #
    #     return both_oceans_cells

    # 2, more elegant, from the other end
    MOVES = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def pacificAtlantic(self, heights: List[List[int]]) -> Set[Tuple[int, int]]:
        def xfs(i: int, j: int, visited: set):
            visited.add((i, j))
            for di, dj in self.MOVES:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < m and (x, y) not in visited and heights[i][j] <= heights[x][y]:
                    xfs(x, y, visited)

        n, m = len(heights), len(heights[0])

        atlantic_visited = set()
        pacific_visited = set()

        for i in range(n):
            xfs(i, 0, pacific_visited)
            xfs(i, m - 1, atlantic_visited)

        for j in range(m):
            xfs(0, j, pacific_visited)
            xfs(n - 1, j, atlantic_visited)

        return atlantic_visited & pacific_visited
