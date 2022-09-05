from math import comb


class Solution:
    # 1
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    # 2 From discussions
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)
