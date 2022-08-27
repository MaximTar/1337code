from typing import List
# from numpy import cumsum


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

    # def runningSum(self, nums: List[int]) -> List[int]:
    #     return cumsum(nums)
