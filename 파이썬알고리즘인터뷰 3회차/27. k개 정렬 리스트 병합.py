from typing import Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Ans1
"""
class WrapperNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        tail = dummy_head
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, WrapperNode(node))

        while heap:
            wrapper_node = heapq.heappop(heap)
            tail.next = wrapper_node.node
            tail = tail.next
            if tail.next:
                heapq.heappush(heap, WrapperNode(tail.next))
        return dummy_head.next
"""

# Ans2

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        tail = dummy_head
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        while heap:
            min_val, i, min_node = heapq.heappop(heap)
            tail.next = min_node
            tail = tail.next
            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, i, min_node.next))
        return dummy_head.next


# Test code
# head = ListNode(2)
# head.next = ListNode(1)
# head.next.next = ListNode(3)
#
# cur = head
# hp = []
# while cur:
#     heapq.heappush(hp, (cur.val, cur))
#     cur = cur.next
#
# while hp:
#     min_val, node = heapq.heappop(hp)
#     print(node.val)
