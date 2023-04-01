# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode(0, None)
        c = 0
        while l1 and l2:
            _sum = l1.val + l2.val + c
            c = _sum // 10
            cur.next = ListNode(_sum % 10, None)
            cur = cur.next
            l1, l2 = l1.next, l2.next

        if l2:
            l1, l2 = l2, l1

        while l1:
            _sum = l1.val + c
            c = _sum // 10
            cur.next = ListNode(_sum % 10, None)
            cur, l1 = cur.next, l1.next

        if c > 0:
            cur.next = ListNode(c, None)

        # head 객체 지우고 싶은데 어떻게 해?
        return head.next

