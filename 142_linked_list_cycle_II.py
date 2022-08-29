import copy
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # storing hashes
    # nice but needs memory for id's set
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ids = {id(head)}
        while head and head.next:
            head = head.next
            head_id = id(head)
            if head_id in ids:
                return head
            ids.add(head_id)
        return None

    # two pointers (Floyd's algorithm)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                while head != slow:
                    head, slow = head.next, slow.next
                return head

    # marking next with None
    # bad decision - needs a copy
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp_lst, tmp_node, counter = copy.deepcopy(head), ListNode(None), 0
        while tmp_lst is not None:
            if tmp_lst.next is None:
                return
            if tmp_lst.next == tmp_node:
                break
            nxt = tmp_lst.next
            tmp_lst.next = tmp_node
            tmp_lst = nxt
            counter += 1
        for _ in range(counter):
            head = head.next
        return head

    # Gosper's algorithm
    # https://web.archive.org/web/20160414011322/http://hackersdelight.org/hdcodetxt/loopdet.c.txt
    # not sure that transferred it optimally, but it works
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return None

        def nlz(x):
            if x == 0:
                return 32
            n = 0
            if x <= 0x0000FFFF:
                n = n + 16
                x = x << 16
            if x <= 0x00FFFFFF:
                n = n + 8
                x = x << 8
            if x <= 0x0FFFFFFF:
                n = n + 4
                x = x << 4
            if x <= 0x3FFFFFFF:
                n = n + 2
                x = x << 2
            if x <= 0x7FFFFFFF:
                n = n + 1
            return n

        def ntz(x):
            if x == 0:
                return 32
            n = 1
            if (x & 0x0000FFFF) == 0:
                n = n + 16
                x = x >> 16
            if (x & 0x000000FF) == 0:
                n = n + 8
                x = x >> 8
            if (x & 0x0000000F) == 0:
                n = n + 4
                x = x >> 4
            if (x & 0x00000003) == 0:
                n = n + 2
                x = x >> 2
            return n - (x & 1)

        n = 0
        T = [None] * 33
        T[0] = head
        Xn = head

        while Xn.next:
            n += 1
            Xn = Xn.next
            kmax = 31 - nlz(n)
            for i in range(kmax + 1):
                k = i
                if Xn == T[k]:
                    break
            else:
                T[ntz(n + 1)] = Xn
                continue
            break
        else:
            return None

        m = ((((n >> k) - 1) | 1) << k) - 1
        try:
            lambda_ = n - m
            lgl = 31 - nlz(lambda_ - 1)
            mu_l = m - max(1, 1 << lgl) + 1

            proposed_set = set()
            for i in range(m + 1):
                if i >= mu_l:
                    proposed_set.add(head)
                head = head.next
            for _ in range(lambda_):
                head = head.next
                if head in proposed_set:
                    return head
        except ValueError:
            for _ in range(m):
                head = head.next

            return head
