# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

""" sol1: recursive """
"""
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 or not list2:
            return list1 or list2

        if list2.val < list1.val:
            list1, list2 = list2, list1

        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
"""

""" sol2: iterative """
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 or not list2:
            return list1 or list2

        cur = dummy = ListNode()
        while list1 and list2:
            if list2.val < list1.val:
                list1, list2 = list2, list1
            cur.next, cur, list1 = list1, list1, list1.next
        cur.next = list2
        ans = dummy.next
        del dummy
        return ans






def list2ListNode(l):
    if not l:
        return None
    node = ListNode(l[0], list2ListNode(l[1:]))
    return node

list1 = [1,2,4]
list2 = [1,3,4]
list1 = list2ListNode(list1)
list2 = list2ListNode(list2)

ret = Solution().mergeTwoLists(list1, list2)
print(ret)