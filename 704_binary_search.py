from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            idx = left + (right - left) // 2
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                right = idx - 1
            else:
                left = idx + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:

        def bs(left, right):
            if left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                bs(left, right)

        left_0, right_0 = 0, len(nums) - 1
        bs(left_0, right_0)
        return -1
