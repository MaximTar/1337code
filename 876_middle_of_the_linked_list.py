from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     double = head
    #     while double and double.next:
    #         head = head.next
    #         double = double.next.next
    #     return head

    # if memory is more important than time
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = self.get_len(head) / 2
        while mid > 0:
            head = head.next
            mid -= 1
        return head

    def get_len(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
