from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.reverse()
        previous, current = 0, cost[0]
        for i in range(1, len(cost)):
            previous, current = current, min(cost[i] + previous, cost[i] + current)
        return min(previous, current)
