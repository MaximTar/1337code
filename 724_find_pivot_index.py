# Note: This question is the same as 1991. Find the Middle Index in Array
from typing import List


class Solution:
    # def pivotIndex(self, nums: List[int]) -> int:
    #     left, right, ln = [0], [0], len(nums)
    #     for i in range(ln):
    #         left.append(left[i] + nums[i])
    #         right.insert(0, right[0] + nums[ln - i - 1])
    #     for i in range(ln):
    #         if left[i] == right[i + 1]:
    #             return i
    #     return -1

    # def pivotIndex(self, nums: List[int]) -> int:
    #     left, right, ln = [0], [0], len(nums)
    #     for i in range(ln):
    #         left.append(left[i] + nums[i])
    #         right.append(right[i] + nums[ln - i - 1])
    #     right.reverse()
    #     for i in range(ln):
    #         if left[i] == right[i + 1]:
    #             return i
    #     return -1

    # def pivotIndex(self, nums: List[int]) -> int:
    #     ln = len(nums)
    #     left, right = [0] * (ln + 1), [0] * (ln + 1)
    #     for i in range(ln):
    #         left[i + 1] = left[i] + nums[i]
    #         right[i + 1] = right[i] + nums[ln - i - 1]
    #     right.reverse()
    #     for i in range(ln):
    #         if left[i] == right[i + 1]:
    #             return i
    #     return -1

    # Hint: We can precompute prefix sums P[i] = nums[0] + nums[1] + ... + nums[i-1]
    # Then for each index, the left sum is P[i], and the right sum is P[P.length - 1] - P[i] - nums[i]
    def pivotIndex(self, nums: List[int]) -> int:
        ln = len(nums)
        cum_sums = [0] * (ln + 1)
        for i in range(ln):
            cum_sums[i + 1] = cum_sums[i] + nums[i]
        last = cum_sums[-1]
        for i in range(ln):
            cur = cum_sums[i]
            if cur == last - cur - nums[i]:
                return i
        return -1
