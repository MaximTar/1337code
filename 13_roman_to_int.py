class Solution:
    def __init__(self):
        self.romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

    # def romanToInt(self, s: str) -> int:
    #     pc, res = 1, 0
    #     for c in reversed(s):
    #         rc = self.romans[c]
    #         res += rc if rc >= pc else -rc
    #         pc = rc
    #     return res

    def romanToInt(self, s: str) -> int:
        res = 0
        for c in reversed(s):
            num = self.romans[c]
            res += -num if 3 * num < res else num
        return res
