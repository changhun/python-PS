from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # return prev, left_node, right_node
        def get_start_last(head, left, right) -> (ListNode, ListNode, ListNode):
            prev, cur = head, head.next
            if left == 1:
                prev = None
            left_node = right_node = head
            for i in range(2, right + 1):
                if i + 1 == left:
                    prev = cur
                if i == left:
                    left_node = cur
                if i == right:
                    right_node = cur
                cur = cur.next
            return prev, left_node, right_node

        def reverse(cur, last_node):
            if cur is last_node:
                return cur
            reversed_head = reverse(cur.next, last_node)
            cur.next.next = cur
            cur.next = None
            return reversed_head

        prev, left_node, right_node = get_start_last(head, left, right)
        next = right_node.next
        reversed_head = reverse(left_node, right_node)
        left_node.next = next
        if prev:
            prev.next = reversed_head
            return head
        else:
            return reversed_head



tail = node = ListNode(5, None)
node = ListNode(4, node)
node = ListNode(3, node)
node = ListNode(2, node)
node = ListNode(1, node)
reversed_head = Solution().reverseBetween(node, 2, 4)
print(reversed_head.val)

def reverse(cur, last_node):
    if cur is last_node:
        return cur
    reversed_head = reverse(cur.next, last_node)
    cur.next.next = cur
    cur.next = None
    return reversed_head


"""
reversed_head = reverse(node, tail)
while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next
"""

def get_start_last(head, left, right) -> (ListNode, ListNode, ListNode):
    prev, cur = head, head.next
    if left == 1:
        prev = None
    left_node = right_node = head
    for i in range(2, right + 1):
        if i+1 == left:
            prev = cur
        if i == left:
            left_node = cur
        if i == right:
            right_node = cur
        cur = cur.next
    return prev, left_node, right_node

#prev, left_node, right_node = get_start_last(node, 1, 5)
prev, left_node, right_node = get_start_last(node, 2, 4)
#print(left_node.val)


tail = node = ListNode(5, None)
node = ListNode(3, node)
reversed_head = Solution().reverseBetween(node, 1, 2)
print(reversed_head.val)