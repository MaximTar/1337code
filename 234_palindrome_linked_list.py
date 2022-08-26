# better solutions
# https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/
# https://dev.to/seanpgallivan/solution-palindrome-linked-list-5721
# https://www.techiedelight.com/check-if-linked-list-is-palindrome/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur, lst = head, []
        while cur:
            lst.append(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if lst.pop() != cur.val:
                return False
            cur = cur.next
        return True
