from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(head, size: int) -> int:
            if size == 1:
                head.next = None
                return head

            half_size = size//2
            second = head
            for i in range(half_size):
                second = second.next

            first = mergeSort(head, half_size)
            second = mergeSort(second, size - half_size)

            dummy = ListNode()
            merged_last = dummy
            while first and second:
                if first.val <= second.val:
                    merged_last.next = first
                    first = first.next
                else:
                    merged_last.next = second
                    second = second.next
                merged_last = merged_last.next

            merged_last.next = first or second
            return dummy.next

        if not head:
            return head

        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        return mergeSort(head, size)

        def merge(first, second):
            if not first or not second:
                return first or second
            if second.val < first.val:
                first, second = second, first
            first.next = merge(first.next, second)
            return first
"""

""" sol2: merge with recursive"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(first, second):
            if not first or not second:
                return first or second
            if second.val < first.val:
                first, second = second, first
            first.next = merge(first.next, second)
            return first

        def mergeSort(head, size: int) -> int:
            if size == 1:
                head.next = None
                return head

            half_size = size // 2
            second = head
            for i in range(half_size):
                second = second.next

            first = mergeSort(head, half_size)
            second = mergeSort(second, size - half_size)
            return merge(first, second)

        if not head:
            return head

        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        return mergeSort(head, size)


def list2ListNode(l):
    last = dummy = ListNode()

    for val in l:
        last.next = ListNode(val)
        last = last.next
    return dummy.next


l = [4,2,1,3]
node = list2ListNode(l)
"""
while node:
    print(node.val)
    head = node.next
"""
node = Solution().sortList(node)
while node:
    print(node.val)
    node = node.next
