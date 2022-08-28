from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 31 ms / 16.3 MB
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        lst = []
        pointer = res = ListNode()
        while head:
            lst.append(head.val)
            head = head.next
        len_lst = len(lst) - 1
        for i in range(len_lst + 1):
            pointer.val = lst[len_lst - i]
            if i != len_lst:
                pointer.next = ListNode()
                pointer = pointer.next
        return res

    # https://leetcode.com/problems/reverse-linked-list/discuss/2497214/Reverse-a-Linked-List-Recursively
    # 41 ms	/ 20.4 MB
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head or not head.next:
    #         return head
    #     res = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #
    #     return res

    # https://leetcode.com/problems/reverse-linked-list/discuss/2491044/Easy-peasy-Python-Solution-using-3-Cursors
    # 48 ms / 15.5 MB
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head or not head.next:
    #         return head
    #
    #     back, mid, front = None, head, head.next
    #
    #     while front:
    #         mid.next = back
    #         back = mid
    #         mid = front
    #         front = front.next
    #
    #     mid.next = back
    #     return mid
