from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for c in s:
            try:
                letters[c] += 1
            except KeyError:
                letters[c] = 1
        length, odd = 0, False
        for value in letters.values():
            if not odd and value % 2 != 0:
                odd = True
            length += 2 * (value // 2)
        if odd:
            length += 1
        return length

    def longestPalindrome(self, s: str) -> int:
        letters = Counter(s)
        length, odd = 0, False
        for value in letters.values():
            if not odd and value % 2 != 0:
                odd = True
            length += 2 * (value // 2)
        if odd:
            length += 1
        return length
