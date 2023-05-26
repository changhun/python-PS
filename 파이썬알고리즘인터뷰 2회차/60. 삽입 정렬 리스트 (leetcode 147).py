from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev_target = head
        target = head.next

        while target:
            prev = None
            cur = head
            while cur is not target:
                if cur.val >= target.val:
                    break
                prev, cur = cur, cur.next

            if prev and cur is not target:
                prev_target.next = target.next
                prev.next, target.next = target, cur
                target = prev_target.next
            elif not prev:
                prev_target.next = target.next
                target.next = cur
                head = target
                target = prev_target.next
            else:
                prev_target, target = prev_target.next, target.next

        return head


def list2ListNode(l:list)->ListNode:
    cur = dummy = ListNode

    for val in l:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

head = [-1,5,3,4,0]
head = list2ListNode(head)
print(head)
ret = Solution().insertionSortList(head)
print(ret)