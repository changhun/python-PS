from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

""" sol1 : recursive """
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(cur, prev):
            if cur.next:
                rev_head = reverse(cur.next, cur)
            else:
                rev_head = cur
            cur.next = prev
            return rev_head

        if not head:
            return None
        return reverse(head, None)
"""

""" sol2: iterative """
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            cur.next, cur, prev  = prev, cur.next, cur

        return prev