from collections import Counter


class Solution:
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     rnc, mc = Counter(ransomNote), Counter(magazine)
    #     for letter, counts in rnc.items():
    #         if letter not in mc.keys() or counts > mc[letter]:
    #             return False
    #     return True

    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     for c in ransomNote:
    #         if c not in magazine:
    #             return False
    #         magazine = magazine.replace(c, '', 1)
    #     return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rnc, mc = Counter(ransomNote), Counter(magazine)
        return rnc & mc == rnc
