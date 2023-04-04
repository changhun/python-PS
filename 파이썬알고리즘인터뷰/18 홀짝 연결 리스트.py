# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

""" recursive
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 인자로 받는 l 은 None 이 아님을 보장한다. (이렇게 정의 했으므로 보장해야한다.)
        def split(l: ListNode) -> (ListNode, ListNode, ListNode):
            if not l.next:
                return l, None, l

            next = l.next
            l1, l2, l1_last = None, None, l
            if next.next:
                l1, l2, l1_last = split(next.next)
            l.next = l1
            next.next = l2
            return l, next, l1_last

        if not head:
            return head
        l1, l2, l1_last = split(head)
        l1_last.next = l2
        return l1
"""

""" iterative 
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        l2 = head.next

        pprev, prev = head, head.next
        cur = prev.next
        while cur:
            pprev.next = cur
            prev.next = cur.next
            pprev, prev = cur, cur.next
            if not cur.next:
                break
            cur = cur.next.next

        pprev.next = l2
        return head
"""
""" iterative2 """

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd_cur = head
        even_cur = even_head = head.next

        while even_cur and even_cur.next:
            odd_cur.next = even_cur.next
            even_cur.next = even_cur.next.next
            odd_cur = odd_cur.next
            even_cur = even_cur.next

        odd_cur.next = even_head
        return head

head = ListNode(5, None)
head = ListNode(4, head)
head = ListNode(3, head)
head = ListNode(2, head)
head = ListNode(1, head)

ret = Solution().oddEvenList(head)