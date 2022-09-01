# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right, lbv = 1, n, 0
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right, lbv = mid - 1, mid
            else:
                left = mid + 1
        return lbv
