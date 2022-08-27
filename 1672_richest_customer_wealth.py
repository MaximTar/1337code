from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for i in range(len(accounts)):
            accounts[i] = sum(accounts[i])
        return max(accounts)

    # def maximumWealth(self, accounts: List[List[int]]) -> int:
    #     return max(list(map(lambda x: sum(x), accounts)))
