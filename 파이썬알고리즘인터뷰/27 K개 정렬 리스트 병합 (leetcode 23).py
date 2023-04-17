# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
import heapq

""" ver1
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        head = cur = ListNode()

        q = []
        for l in lists:
            if l:
                heapq.heappush(q, (l.val, l))

        while q:
            top_value, top_node = heapq.heappop(q)
            cur.next = top_node
            cur = top_node
            if top_node.next:
                heapq.heappush(q, (top_node.next.val, top_node.next))

        return head.next
"""

""" ver2 """
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        head = cur = ListNode()

        q = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))

        while q:
            top_value, index = heapq.heappop(q)
            cur.next = lists[index]
            cur = lists[index]
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(q, (lists[index].val, index))

        return head.next
