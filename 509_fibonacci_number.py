class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        f_0, f_1 = 0, 1
        for _ in range(n - 1):
            f_0, f_1 = f_1, f_0 + f_1
        return f_1
