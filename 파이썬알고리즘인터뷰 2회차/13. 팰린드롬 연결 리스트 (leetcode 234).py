from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def checkPalindrome(head: ListNode, size: int) -> (bool, ListNode):
            if size == 1:
                return True, head.next
            if size == 2:
                return head.val == head.next.val, head.next.next

            ret, last = checkPalindrome(head.next, size - 2)
            if not ret:
                return False, last.next
            return head.val == last.val, last.next

        len = 0
        cur = head
        while cur:
            len += 1
            cur = cur.next
        if len == 0:
            return True
        ret, tmp = checkPalindrome(head, len)
        return ret