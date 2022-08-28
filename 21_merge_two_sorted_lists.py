from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # wrong - returns list, not linked list
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     if not list1:
    #         return list2
    #     if not list2:
    #         return list1
    #
    #     if list1.val < list2.val:
    #         list3 = [list1.val]
    #         list1 = list1.next
    #     else:
    #         list3 = [list2.val]
    #         list2 = list2.next
    #
    #     while list1:
    #         if list2:
    #             if list1.val < list2.val:
    #                 list3.append(list1.val)
    #                 list1 = list1.next
    #             else:
    #                 list3.append(list2.val)
    #                 list2 = list2.next
    #         else:
    #             list3.append(list1.val)
    #             list1 = list1.next
    #     while list2:
    #         list3.append(list2.val)
    #         list2 = list2.next
    #
    #     return list3

    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     if not list1:
    #         return list2
    #     if not list2:
    #         return list1
    #
    #     if list1.val < list2.val:
    #         pointer = list3 = ListNode(val=list1.val)
    #         list1 = list1.next
    #     else:
    #         pointer = list3 = ListNode(val=list2.val)
    #         list2 = list2.next
    #
    #     while list1:
    #         if list2:
    #             if list1.val < list2.val:
    #                 pointer.next = ListNode(val=list1.val)
    #                 list1 = list1.next
    #             else:
    #                 pointer.next = ListNode(val=list2.val)
    #                 list2 = list2.next
    #         else:
    #             pointer.next = list1
    #             break
    #         pointer = pointer.next
    #     if list2:
    #         pointer.next = list2
    #
    #     return list3

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if not list2 else list2

        pointer = list3 = ListNode()

        while list1:
            if list2:
                if list1.val < list2.val:
                    pointer.next, list1 = list1, list1.next
                else:
                    pointer.next, list2 = list2, list2.next
            else:
                pointer.next = list1
                break
            pointer = pointer.next
        if list2:
            pointer.next = list2

        return list3.next
