from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        cur = head.next
        last = head
        last.next = None # this is the key point which makes the end sorted list is null

        while cur:
            next = cur.next
            prev = dummy
            while prev.next and prev.next.val <= cur.val:
                prev = prev.next

            cur.next, prev.next = prev.next, cur
            cur = next

        head = dummy.next
        del dummy
        return head

"""
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        cur = head.next
        last = head
        last.next = None # this is the key point which makes the end sorted list is null

        while cur:
            next = cur.next
            prev = dummy
            #while prev.next and prev.next is not cur and prev.next.val <= cur.val:
            while prev.next and prev.next.val <= cur.val:
                prev = prev.next

            # if cur should be positioned at the last node of previous sorted list
            #if not prev.next:
            #    cur.next = None # this is done in the following line. (cur.next = prev.next)

            cur.next, prev.next = prev.next, cur
            cur = next

        head = dummy.next
        del dummy
        return head
"""