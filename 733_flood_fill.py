from typing import List


class Solution:
    # 1 Recursive
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def xfs(i: int, j: int):
            if image[i][j] == color:
                return
            image[i][j] = color
            for di, dj in deltas:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < m and image[x][y] == starting_pixel:
                    xfs(x, y)

        n, m, starting_pixel = len(image), len(image[0]), image[sr][sc]
        xfs(sr, sc)
        return image

    # 2 Iterative
    def floodFill(self, image, sr, sc, color):
        n, m, starting_pixel = len(image), len(image[0]), image[sr][sc]
        queue = set()
        queue.add((sr, sc))
        deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while queue:
            i, j = queue.pop()
            if image[i][j] == color:
                continue
            image[i][j] = color
            for di, dj in deltas:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < m and image[x][y] == starting_pixel:
                    queue.add((x, y))
        return image
