# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev, cur, next = None, head, head.next

        while cur:
            cur.next = prev

            prev = cur
            cur = next
            if next:
                next = next.next
            #prev, cur, next = cur, next, next.next
        return prev
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        # 다중 대입?이 가능하므로 next 레퍼런스?는 없어도 된다.
        prev, cur = None, head

        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_head
"""


list1 = ListNode(5, None)
list1 = ListNode(4, list1)
list1 = ListNode(3, list1)
list1 = ListNode(2, list1)
list1 = ListNode(1, list1)
ret = Solution().reverseList(list1)
while ret:
    print(ret.val)
    ret = ret.next
