import string
from collections import Counter
from typing import List


class Solution:
    # 1 Head-on / Bad Solution (Time Limit Exceeded)
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     cp = Counter(p)
    #     lp = len(p)
    #     ps = set(p)
    #     res = []
    #     for i in range(len(s) - lp + 1):
    #         if s[i] in ps and Counter(s[i:i + lp]) == cp:
    #             res.append(i)
    #     return res

    # 2 Likewise https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/1738052/A-very-deep-EXPLANATION-oror-Solved-without-using-HashTable
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp, ls = len(p), len(s)
        result = []

        if lp > ls:
            return result

        s_letters = dict.fromkeys(string.ascii_lowercase, 0)
        p_letters = dict.fromkeys(string.ascii_lowercase, 0)

        for c in p:
            p_letters[c] += 1

        for i in range(lp):
            s_letters[s[i]] += 1

        if p_letters == s_letters:
            result.append(0)

        for i in range(lp, ls):
            s_letters[s[i]] += 1
            s_letters[s[i - lp]] -= 1
            if p_letters == s_letters:
                result.append(i - lp + 1)

        return result
