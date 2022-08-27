class Solution:
    def __init__(self):
        self.memo_dict = {0: ['1'], 1: ['2']}

    def reorderedPowerOf2(self, n: int) -> bool:
        digits = sorted(str(n))
        i = 0
        while len(self.memo_dict[i]) <= len(digits):
            if self.memo_dict[i] == digits:
                return True
            i += 1
            if i not in self.memo_dict:
                self.memo_dict[i] = sorted(str(2 ** i))
        return False
