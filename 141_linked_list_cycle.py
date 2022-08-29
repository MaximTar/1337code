from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # marking next with None
    # Runtime: 46 ms, faster than 99.67% of Python3 online submissions for Linked List Cycle.
    # Memory Usage: 16.6 MB, less than 99.49% of Python3 online submissions for Linked List Cycle.
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tmp = ListNode(None)
        while head is not None:
            if head.next is None:
                return False
            if head.next == tmp:
                return True
            nxt = head.next
            head.next = tmp
            head = nxt
        return False

    # storing hashes
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ids = {id(head)}
        while head and head.next:
            head = head.next
            head_id = id(head)
            if head_id in ids:
                return True
            ids.add(head_id)
        return False

    # two pointers (Floyd's cycle-finding algorithm)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    # by constraint
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        counter, constraint = 0, 10 ** 4
        while head.next:
            if counter > constraint:
                return True
            head = head.next
            counter += 1
        return False

    # marking val with None
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head is not None:
            if head.next is None:
                return False
            if head.val is None:
                return True
            head.val = None
            head = head.next
        return False
