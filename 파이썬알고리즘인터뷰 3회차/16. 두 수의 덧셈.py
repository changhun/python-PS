from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addTwoNumbersWithCarrier(l1, l2, c):
            if not l1 and not l2:
                if c == 0:
                    return None
                else:
                    return ListNode(c)

            if not l1:
                l1, l2 = l2, l1

            if not l2:
                c, l1.val = (c + l1.val) // 10, (c + l1.val) % 10
                l1.next = addTwoNumbersWithCarrier(l1.next, l2, c)
                return l1

            c, l1.val = (c + l1.val + l2.val) // 10, (c + l1.val + l2.val) % 10
            l1.next = addTwoNumbersWithCarrier(l1.next, l2.next, c)
            return l1
        return addTwoNumbersWithCarrier(l1, l2, 0)

def list2ListNode(l: list):
    head = ListNode(l[0])
    cur = head
    for val in l[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

l1 = [2,4,3]
l2 = [5,6,4]
l1 = list2ListNode(l1)
l2 = list2ListNode(l2)
cur = l1
while cur:
    print(cur.val)
    cur = cur.next

cur = Solution().addTwoNumbers(l1, l2)
while cur:
    print(cur.val)
    cur = cur.next