class Solution:
    # first attempt
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        f_1, f_2, res = 0, 1, 2
        for _ in range(n - 2):
            f_1, f_2 = f_2, f_1 + f_2
            res += f_2
        return res

    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        f_1, f_2 = 2, 3
        for _ in range(n - 3):
            f_1, f_2 = f_2, f_1 + f_2
        return f_2
