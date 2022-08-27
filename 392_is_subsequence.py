class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        idx, last_idx = 0, -1
        for cs in s:
            t = t[idx:]
            if not t:
                return False
            for it in range(len(t)):
                if cs == t[it]:
                    idx, last_idx = it + 1, idx
                    break
                if it == len(t) - 1:
                    return False
        return True

    # https://leetcode.com/problems/is-subsequence/discuss/1811508/Python-Javascript-Easy-solution-with-very-clear-Explanation/1411952
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     i, j = 0, 0
    #     while i < len(s) and j < len(t):
    #         if s[i] == t[j]:
    #             i += 1
    #         j += 1
    #     return i == len(s)
