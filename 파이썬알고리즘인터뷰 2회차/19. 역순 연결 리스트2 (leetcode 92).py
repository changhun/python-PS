from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        prev, cur = None, head
        for index in range(1, left):
            prev, cur = cur, cur.next
        prev_left_node = prev
        left_node = cur

        if not cur.next:
            return head
        prev, cur = cur, cur.next
        for i in range(left+1, right+1):
            #prev, cur, cur.next = cur, cur.next, prev
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        if prev_left_node:
            prev_left_node.next = prev
        else:
            head = prev
        left_node.next = cur


        return head


def list2LinkedList(l):
    if not l:
        return None
    return ListNode(l[0], list2LinkedList(l[1:]))


head = [1,2,3,4,5]
left = 2
right = 4

head = [3,5]
left = 1
right = 1
head = list2LinkedList(head)
ret = Solution().reverseBetween(head, left, right)
print(ret)
while head:
    print(head.val, end=' ')
    head = head.next