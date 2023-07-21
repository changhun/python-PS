from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        seq = 0

        while seq < left - 1:
            cur = cur.next
            seq += 1

        before_left = cur
        first = cur.next

        prev = first
        cur = first.next
        seq = left + 1

        while seq < right:
            cur.next, cur, prev = prev, cur.next, cur
            seq += 1

        next = None
        if seq <= right:
            next = cur.next
            cur.next = prev
            before_left.next = cur
            first.next = next
        return dummy.next


def l2ListNode(l):
    cur = head = ListNode(l[0])
    for val in l[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head



head = [5]
left = 1
right = 1
head = [1,2,3,4,5]
left, right = 2, 4
head = [3, 5]
left, right = 1, 1
head = l2ListNode(head)
ans = Solution().reverseBetween(head, left, right)
while ans:
    print(ans.val)
    ans = ans.next
