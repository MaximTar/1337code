class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num > 0:
            num = num / 2 if num % 2 == 0 else num - 1
            res += 1
        return res

    # could be useful later
    # def numberOfSteps(self, num: int) -> int:
    #     memo_dict = {0: 0, 1: 1}
    #
    #     if num not in memo_dict:
    #         memo_dict[num] = 1 + num % 2 + self.numberOfSteps(num // 2)
    #
    #     # Return the answer
    #     return memo_dict[num]

    # https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/discuss/2480025/Python-1-liner
    # def numberOfSteps(self, num: int) -> int:
    #     return bin(num)[2:].count('1') + len(bin(num)[2:]) - 1
